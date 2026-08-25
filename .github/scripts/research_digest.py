#!/usr/bin/env python3
"""Weekly research digest for an awesome list.

Scans Hacker News (Algolia), GitHub Search, Product Hunt (optional token)
and RSS feeds for new projects/tools matching digest_config.json, dedupes
against URLs already in the repo's markdown and past 'research' issues,
optionally re-ranks top candidates with an OpenAI-compatible LLM, and prints
a markdown digest to stdout. Logs go to stderr; the script always exits 0.
"""
import json
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from html import unescape
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "digest_config.json"
URL_RE = re.compile(r"https?://[^\s\)>\]\"'<]+")
TIMEOUT = 25


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as fh:
        cfg = json.load(fh)
    cfg.setdefault("hn_queries", [])
    cfg.setdefault("github_queries", [])
    cfg.setdefault("rss_feeds", [])
    cfg.setdefault("keywords", [])
    cfg.setdefault("min_hn_points", 3)
    cfg.setdefault("min_github_stars", 5)
    cfg.setdefault("days_back", 14)
    cfg.setdefault("max_llm_candidates", 25)
    cfg.setdefault("max_per_source", 12)
    return cfg


def log(msg):
    print(msg, file=sys.stderr)


def get_json(url, headers=None):
    req = Request(url, headers={"User-Agent": "awesome-research-digest", **(headers or {})})
    with urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8", "replace"))


def days_ago_iso(days):
    return (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")


def fetch_hn(query, since_epoch, min_points):
    params = {
        "query": query,
        "tags": "story",
        "hitsPerPage": "20",
        "numericFilters": f"created_at_i>{since_epoch},points>={min_points}",
    }
    data = get_json("https://hn.algolia.com/api/v1/search_by_date?" + urlencode(params))
    out = []
    for hit in data.get("hits", []):
        url = hit.get("url") or ""
        if not url.startswith("http"):
            continue
        out.append({
            "url": url,
            "title": hit.get("title") or "",
            "description": "",
            "source": "Hacker News",
            "signal": f"{hit.get('points', 0)} pts",
            "score": float(hit.get("points", 0)),
        })
    return out


def fetch_github(query, since_date, min_stars):
    q = f"{query} created:>{since_date}"
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = get_json(
        "https://api.github.com/search/repositories?" + urlencode({"q": q, "sort": "stars", "order": "desc", "per_page": "20"}),
        headers=headers,
    )
    out = []
    for item in data.get("items", []):
        stars = int(item.get("stargazers_count", 0))
        if stars < min_stars:
            continue
        out.append({
            "url": item.get("html_url", ""),
            "title": item.get("full_name", ""),
            "description": item.get("description") or "",
            "source": "GitHub",
            "signal": f"{stars} stars",
            "score": stars / 10.0,
        })
    return out


def fetch_rss(feed_url, keywords):
    try:
        req = Request(feed_url, headers={"User-Agent": "awesome-research-digest"})
        with urlopen(req, timeout=TIMEOUT) as resp:
            root = ET.fromstring(resp.read())
    except Exception as exc:
        log(f"rss failed {feed_url}: {exc}")
        return []
    items = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")
    out = []
    low_kws = [k.lower() for k in keywords]
    for it in items:
        def txt(tag, attr=None):
            el = it.find(tag) if attr is None else it.find(tag)
            if el is None:
                return ""
            return unescape(el.text or el.get(attr, "")).strip()
        title = txt("title")
        link = txt("link") or txt("{http://www.w3.org/2005/Atom}link", "href")
        desc = txt("description") or txt("summary")
        blob = f"{title} {desc}".lower()
        if not link.startswith("http"):
            continue
        hits = [k for k in low_kws if k in blob]
        if not hits:
            continue
        out.append({
            "url": link.split("?utm")[0],
            "title": title,
            "description": desc,
            "source": "RSS",
            "signal": f"matched: {', '.join(hits[:3])}",
            "score": 2.0 * len(hits),
        })
    return out


def fetch_producthunt(keywords, since_date):
    token = os.environ.get("PRODUCTHUNT_TOKEN")
    if not token:
        return []
    query = (
        '{ posts(first: 25, postedAfter: "%s", order: VOTES) { edges { node { '
        "name tagline url votesCount websiteUrl } } } }" % since_date
    )
    try:
        req = Request(
            "https://api.producthunt.com/v2/api/graphql",
            data=json.dumps({"query": query}).encode(),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
                "User-Agent": "awesome-research-digest",
            },
            method="POST",
        )
        with urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read().decode())
        nodes = [e["node"] for e in data["data"]["posts"]["edges"]]
    except Exception as exc:
        log(f"product hunt failed: {exc}")
        return []
    low_kws = [k.lower() for k in keywords]
    out = []
    for n in nodes:
        blob = f"{n.get('name','')} {n.get('tagline','')}".lower()
        hits = [k for k in low_kws if k in blob]
        if not hits:
            continue
        out.append({
            "url": n.get("websiteUrl") or n.get("url", ""),
            "title": n.get("name", ""),
            "description": n.get("tagline", ""),
            "source": "Product Hunt",
            "signal": f"{n.get('votesCount', 0)} votes",
            "score": float(n.get("votesCount", 0)) / 5.0,
        })
    return out


def repo_urls():
    urls = set()
    for md in SCRIPT_DIR.parents[1].rglob("*.md"):
        if ".github" in md.parts:
            continue
        try:
            urls.update(u.rstrip(".,;") for u in URL_RE.findall(md.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            pass
    return urls


def prior_issue_urls():
    gh = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not gh:
        return set()
    try:
        out = subprocess.run(
            ["gh", "issue", "list", "--label", "research", "--state", "all", "--limit", "80", "--json", "title,body"],
            capture_output=True, text=True, timeout=45,
        )
        return set(u.rstrip(".,;") for u in URL_RE.findall(out.stdout or ""))
    except Exception as exc:
        log(f"prior issue lookup skipped: {exc}")
        return set()


def llm_rank(candidates, cfg):
    key = os.environ.get("LLM_API_KEY")
    if not key or not candidates:
        return {}, False
    base = os.environ.get("LLM_BASE_URL", "https://models.github.ai/inference").rstrip("/")
    model = os.environ.get("LLM_MODEL", "openai/gpt-4o-mini")
    slim = [{"url": c["url"], "title": c["title"], "description": c["description"][:300], "source": c["source"]} for c in candidates]
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": (
                "You are the curator of the following awesome list:\n"
                f"{cfg['list_description']}\n\n"
                "For each candidate URL decide whether it belongs on this list. "
                'Respond ONLY with a JSON array: [{"url":"...","relevance":"high|medium|low","reason":"max 15 words"}]'
            )},
            {"role": "user", "content": json.dumps(slim)},
        ],
        "temperature": 0,
    }
    try:
        req = Request(
            f"{base}/chat/completions",
            data=json.dumps(body).encode(),
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
            method="POST",
        )
        with urlopen(req, timeout=90) as resp:
            content = json.loads(resp.read().decode())["choices"][0]["message"]["content"]
        parsed = json.loads(content[content.index("["): content.rindex("]") + 1])
        return {p.get("url"): p for p in parsed if isinstance(p, dict)}, True
    except Exception as exc:
        log(f"llm ranking skipped: {exc}")
        return {}, False


def esc(text, limit=160):
    text = unescape(str(text)).replace("|", "\\|").replace("\n", " ")
    return text[: limit - 1] + "…" if len(text) > limit else text


def table(rows, verdicts):
    lines = [
        "| Candidate | Source | Signal | Verdict | Why |",
        "|---|---|---|---|---|",
    ]
    for c in rows:
        v = verdicts.get(c["url"], {})
        lines.append(
            f"| [{esc(c['title'])}]({c['url']}) | {c['source']} | {esc(c['signal'], 40)} "
            f"| {v.get('relevance', 'unrated')} | {esc(v.get('reason', c['description']), 120)} |"
        )
    return "\n".join(lines)


def main():
    cfg = load_config()
    since_date = days_ago_iso(cfg["days_back"])
    since_epoch = int((datetime.now(timezone.utc) - timedelta(days=cfg["days_back"])).timestamp())
    known = repo_urls() | prior_issue_urls()
    log(f"dedupe baseline: {len(known)} known URLs")

    buckets = []
    for q in cfg["hn_queries"]:
        buckets += fetch_hn(q, since_epoch, cfg["min_hn_points"])
    for q in cfg["github_queries"]:
        buckets += fetch_github(q, since_date, cfg["min_github_stars"])
    for feed in cfg["rss_feeds"]:
        buckets += fetch_rss(feed, cfg["keywords"] + [q.lower() for q in cfg["hn_queries"]])
    buckets += fetch_producthunt(cfg["keywords"], since_date)

    seen, unique = set(), []
    known_norm = {u.rstrip("/") for u in known}
    for c in buckets:
        norm = c["url"].rstrip("/")
        if norm in seen or norm in known_norm:
            continue
        seen.add(norm)
        unique.append(c)

    unique.sort(key=lambda c: c["score"], reverse=True)
    unique = unique[: cfg["max_llm_candidates"]]
    verdicts, used_llm = llm_rank(unique, cfg)

    rank = {"high": 0, "medium": 1, "low": 2}
    high = [c for c in unique if verdicts.get(c["url"], {}).get("relevance") == "high"]
    medium = [c for c in unique if verdicts.get(c["url"], {}).get("relevance") == "medium"]
    rest = [c for c in unique if c not in high and c not in medium]

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [f"# Research digest — {today}", ""]
    lines.append(f"Scanned the last {cfg['days_back']} days: {len(buckets)} raw findings, {len(unique)} new candidates after dedupe."
                 + (" Ranked by LLM." if used_llm else " _No LLM key configured — heuristic ranking only._"))
    lines.append("")
    if high:
        lines += ["## High relevance", "", table(high, verdicts), ""]
    if medium:
        lines += ["## Maybe worth a look", "", table(medium, verdicts), ""]
    if rest:
        lines += ["## Other candidates", "", table(rest, verdicts), ""]
    if not unique:
        lines += ["No new candidates found this week. All clear."]
    report = "\n".join(lines).strip() + "\n"

    out_path = os.environ.get("DIGEST_OUT")
    if out_path:
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        Path(out_path).write_text(report, encoding="utf-8")
    gha_out = os.environ.get("GITHUB_OUTPUT")
    if gha_out:
        with open(gha_out, "a", encoding="utf-8") as fh:
            fh.write(f"candidates={len(unique)}\n")

    sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
