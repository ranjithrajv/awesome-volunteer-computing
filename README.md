# Awesome Volunteer Computing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="banner.svg" alt="Awesome Volunteer Computing" width="650">
</p>

**volunteer computing** — practice of donating idle computing power to help solve real-world scientific and humanitarian problems.

Early pioneers like GIMPS and distributed.net paved the way for modern platforms that aggregate these resources into powerful virtual supercomputers, enabling research otherwise impossible.

> Below is a curated list of awesome platforms, projects, and tools for volunteer computing

---

## 📚 Contents

<!--lint disable awesome-list-item-->
- [Platforms & Infrastructure](#platforms--infrastructure)
  - [Hybrid or Multi-Platform](#hybrid-or-multi-platform)
  - [Desktop-Native](#desktop-native)
  - [Mobile-Based](#mobile-based)
  - [Browser-Based](#browser-based)
- [For Developers](#for-developers)
- [Volunteer Projects](#volunteer-projects)
- [Research & Papers](#research--papers)
- [Communities & Forums](#communities--forums)
- [Related Concepts](#related-concepts)
- [Related & Historical Projects](#related--historical-projects)
- [Articles & Videos](#articles--videos)
<!--lint enable awesome-list-item-->

---

## 🚀 New to Volunteer Computing

Volunteer computing lets you contribute to cutting-edge science using hardware you already own. Here's how to get started:

<!--lint disable awesome-list-item-->
1. **Pick a project** - Scroll down to Volunteer Projects and choose one that interests you (protein folding, prime numbers, or astrophysics).
2. **Install the software** - Most projects use BOINC (desktop) or run entirely in your browser.
3. **Let it run** - Your computer works on small research tasks when idle. No impact on your daily use.
4. **Join a community** - Connect with other volunteers on r/BOINC or the BOINC Discord.
<!--lint enable awesome-list-item-->

> **Tip:** Start with Science United — it automatically assigns your computer to projects that need help most.

---

## ⚙️ Platforms & Infrastructure

Volunteer computing systems people can join or build on top of.

### 🧬 Hybrid or Multi-Platform

- 🌸 **[Petals](https://petals.dev/)** ([Repo](https://github.com/bigscience-workshop/petals)) [![GitHub stars](https://img.shields.io/github/stars/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/network) [![GitHub last commit](https://img.shields.io/github/last-commit/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/commits/main) - Peer-to-peer network that runs large language models (LLMs) like BLOOM across distributed GPUs and contributors' machines.
- 🧱 **[Exo](https://github.com/exo-explore/exo)** [![GitHub stars](https://img.shields.io/github/stars/exo-explore/exo)](https://github.com/exo-explore/exo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/exo-explore/exo)](https://github.com/exo-explore/exo/network) [![GitHub last commit](https://img.shields.io/github/last-commit/exo-explore/exo)](https://github.com/exo-explore/exo/commits/main) - Run your own AI cluster at home with everyday devices. Unifies existing devices (iPhone, iPad, Android, Mac, NVIDIA, Raspberry Pi) into one powerful distributed GPU for running various AI models including LLaMA, Mistral, and LlaVA.
  - 🧠🧱 **[MultiCortex EXO](https://github.com/cabelo/multicortex-exo)** [![GitHub stars](https://img.shields.io/github/stars/cabelo/multicortex-exo)](https://github.com/cabelo/multicortex-exo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/cabelo/multicortex-exo)](https://github.com/cabelo/multicortex-exo/network) [![GitHub last commit](https://img.shields.io/github/last-commit/cabelo/multicortex-exo)](https://github.com/cabelo/multicortex-exo/commits/main) - A portable system that can be booted from a USB flash drive, with the fantastic Exo project pre-installed. It allows any computer to become a node for creating a decentralized AI framework. It allows pooling of computing power from multiple devices, leveraging CPUs, GPUs, NPUs, and other accelerators.
- 🤖 **[autoresearch@home](https://github.com/mutable-state-inc/autoresearch-at-home)** ([Website](https://www.ensue-network.ai/autoresearch)) [![GitHub stars](https://img.shields.io/github/stars/mutable-state-inc/autoresearch-at-home)](https://github.com/mutable-state-inc/autoresearch-at-home/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mutable-state-inc/autoresearch-at-home)](https://github.com/mutable-state-inc/autoresearch-at-home/network) [![GitHub last commit](https://img.shields.io/github/last-commit/mutable-state-inc/autoresearch-at-home)](https://github.com/mutable-state-inc/autoresearch-at-home/commits/main) - A collaborative, SETI@home-style fork of autoresearch where multiple agents on different GPUs share results to improve language models through the Ensue shared memory network.
- 🌐 **[AI Horde](https://aihorde.net/)** ([Repo](https://github.com/Haidra-Org/AI-Horde)) [![GitHub stars](https://img.shields.io/github/stars/Haidra-Org/AI-Horde)](https://github.com/Haidra-Org/AI-Horde/stargazers) [![GitHub forks](https://img.shields.io/github/forks/Haidra-Org/AI-Horde)](https://github.com/Haidra-Org/AI-Horde/network) [![GitHub last commit](https://img.shields.io/github/last-commit/Haidra-Org/AI-Horde)](https://github.com/Haidra-Org/AI-Horde/commits/main) - Crowdsourced volunteer GPU cluster for free AI image and text generation. Kudos-based incentive system. By Haidra, a registered non-profit in Luxembourg. Published at SciTS 2024 (IEEE International Conference on eScience).
- 🐝 **[Hivemind](https://github.com/learning-at-home/hivemind)** [![GitHub stars](https://img.shields.io/github/stars/learning-at-home/hivemind)](https://github.com/learning-at-home/hivemind/stargazers) [![GitHub forks](https://img.shields.io/github/forks/learning-at-home/hivemind)](https://github.com/learning-at-home/hivemind/network) [![GitHub last commit](https://img.shields.io/github/last-commit/learning-at-home/hivemind)](https://github.com/learning-at-home/hivemind/commits/main) - PyTorch library for decentralized deep learning over the internet. Enables training models across volunteer GPUs without central coordination. Powers Petals and other distributed ML projects. NeurIPS 2021 demonstration.

### 💻 Desktop-Native

- 🧩 **[BOINC](https://boinc.berkeley.edu/)** ([Repo](https://github.com/BOINC/boinc)) [![GitHub stars](https://img.shields.io/github/stars/BOINC/boinc)](https://github.com/BOINC/boinc/stargazers) [![GitHub forks](https://img.shields.io/github/forks/BOINC/boinc)](https://github.com/BOINC/boinc/network) [![GitHub last commit](https://img.shields.io/github/last-commit/BOINC/boinc)](https://github.com/BOINC/boinc/commits/main) - The gold standard in open-source volunteer computing, powering dozens of scientific research projects.
  - 🖥️ **[GridRepublic](https://www.gridrepublic.org/)** - A user-friendly frontend for managing BOINC projects and participation.
  - 💡 **[Charity Engine](https://www.charityengine.com/)** - Turns donated computing power into charitable donations or rewards for users.
  - 🧩 **[Fresco](https://github.com/AufarZakiev/Fresco)** [![GitHub stars](https://img.shields.io/github/stars/AufarZakiev/Fresco)](https://github.com/AufarZakiev/Fresco/stargazers) [![GitHub forks](https://img.shields.io/github/forks/AufarZakiev/Fresco)](https://github.com/AufarZakiev/Fresco/network) [![GitHub last commit](https://img.shields.io/github/last-commit/AufarZakiev/Fresco)](https://github.com/AufarZakiev/Fresco/commits/main) - Modern cross-platform BOINC Manager alternative built with Tauri and Vue. ~5 MB binary with dark mode, auto-update, and remote client support.
  - 🔢 **[NFS@home](https://escatter11.fullerton.edu/nfs/)** - Number field sieve factorization project. Factored RSA-240 (240 digits) in 2019. Hosted at Cal State Fullerton.
  - 🔢 **[YAFU](https://yafu.myfirewall.org/yafu/)** - Integer factorization on BOINC. Active development with latest news in June 2026.
  - 🌠 **[Asteroids@home](https://www.asteroidsathome.net/)** - Asteroid shape and spin determination from photometric observations using volunteer computing.

### 📱 Mobile-Based

- 📲 **[DreamLab](https://www.vodafone.com/vodafone-foundation/focus-areas/dreamlab-app)** - Vodafone Foundation's mobile app that powers medical and nutritional research while your phone charges.

### 🌐 Browser-Based

- 🐼 **[Pando](https://github.com/pando-project/pando)** [![GitHub stars](https://img.shields.io/github/stars/pando-project/pando)](https://github.com/pando-project/pando/stargazers) [![GitHub forks](https://img.shields.io/github/forks/pando-project/pando)](https://github.com/pando-project/pando/network) [![GitHub last commit](https://img.shields.io/github/last-commit/pando-project/pando)](https://github.com/pando-project/pando/commits/main) - A personal volunteer computing platform for the Web, allowing easy setup for personal or shared computations via JavaScript. ([See Paper](https://arxiv.org/vc/arxiv/papers/1804/1804.01482v1.pdf))
- 🌐 **[Wasimoff](https://github.com/wasimoff/wasimoff)** [![GitHub stars](https://img.shields.io/github/stars/wasimoff/wasimoff)](https://github.com/wasimoff/wasimoff/stargazers) [![GitHub forks](https://img.shields.io/github/forks/wasimoff/wasimoff)](https://github.com/wasimoff/wasimoff/network) [![GitHub last commit](https://img.shields.io/github/last-commit/wasimoff/wasimoff)](https://github.com/wasimoff/wasimoff/commits/main) - WebAssembly-based browser volunteer computing framework. Tasks run in isolated Web Workers with zero-setup participation. Published at IEEE PerCom Workshops 2024 and ACM Middleware 2024 demos.

---

## 🛠️ For Developers

Libraries, SDKs, and tools for building or contributing to volunteer computing systems.

- 🧰 **[BOINC Development Resources](https://boinc.berkeley.edu/trac/wiki/SoftwareDevelopment)** ([Repo](https://github.com/BOINC/boinc-dev-doc)) [![GitHub stars](https://img.shields.io/github/stars/BOINC/boinc-dev-doc)](https://github.com/BOINC/boinc-dev-doc/stargazers) [![GitHub forks](https://img.shields.io/github/forks/BOINC/boinc-dev-doc)](https://github.com/BOINC/boinc-dev-doc/network) [![GitHub last commit](https://img.shields.io/github/last-commit/BOINC/boinc-dev-doc)](https://github.com/BOINC/boinc-dev-doc/commits/main) - Comprehensive guide covering the SDK, APIs, server/client setup, and creating BOINC-compatible applications.
- 🌸 **[Flower](https://github.com/adap/flower)** [![GitHub stars](https://img.shields.io/github/stars/adap/flower)](https://github.com/adap/flower/stargazers) [![GitHub forks](https://img.shields.io/github/forks/adap/flower)](https://github.com/adap/flower/network) [![GitHub last commit](https://img.shields.io/github/last-commit/adap/flower)](https://github.com/adap/flower/commits/main) - A federated learning framework that enables training machine learning models across distributed devices while preserving data privacy. Supports PyTorch Lightning and other ML frameworks.
- 🌳 **[webrtc-tree-overlay](https://github.com/elavoie/webrtc-tree-overlay)** [![GitHub stars](https://img.shields.io/github/stars/elavoie/webrtc-tree-overlay)](https://github.com/elavoie/webrtc-tree-overlay/stargazers) [![GitHub forks](https://img.shields.io/github/forks/elavoie/webrtc-tree-overlay)](https://github.com/elavoie/webrtc-tree-overlay/network) [![GitHub last commit](https://img.shields.io/github/last-commit/elavoie/webrtc-tree-overlay)](https://github.com/elavoie/webrtc-tree-overlay/commits/main) - A library for building scalable WebRTC P2P mesh networks in a tree overlay structure, useful for browser-based distributed applications.
- 🔗 **[GridCoin Developer Information](https://wiki.gridcoin.us/Developer-Information)** ([Repo](https://github.com/gridcoin-community/Gridcoin-Research)) [![GitHub stars](https://img.shields.io/github/stars/gridcoin-community/Gridcoin-Research)](https://github.com/gridcoin-community/Gridcoin-Research/stargazers) [![GitHub forks](https://img.shields.io/github/forks/gridcoin-community/Gridcoin-Research)](https://github.com/gridcoin-community/Gridcoin-Research/network) [![GitHub last commit](https://img.shields.io/github/last-commit/gridcoin-community/Gridcoin-Research)](https://github.com/gridcoin-community/Gridcoin-Research/commits/main) - Resources for integrating blockchain-based incentives (GridCoin) with distributed computing (primarily BOINC).
- 🔗 **[Lattica](https://github.com/GradientHQ/lattica)** [![GitHub stars](https://img.shields.io/github/stars/GradientHQ/lattica)](https://github.com/GradientHQ/lattica/stargazers) [![GitHub forks](https://img.shields.io/github/forks/GradientHQ/lattica)](https://github.com/GradientHQ/lattica/network) [![GitHub last commit](https://img.shields.io/github/last-commit/GradientHQ/lattica)](https://github.com/GradientHQ/lattica/commits/main) - Decentralized cross-NAT communication framework for distributed AI. Features NAT traversal, CRDT-based data store, and DHT content discovery. ([Paper](https://doi.org/10.48550/arxiv.2510.00183))

---

## 🧪 Volunteer Projects

Scientific and research projects powered by public computing contributions.

- 🔬 **[Folding@home](https://foldingathome.org/)** - Simulates protein folding to better understand diseases like cancer and Alzheimer's. ([Repo](https://github.com/FoldingAtHome) | [Wikidata](https://www.wikidata.org/wiki/Q386283))
  - 📰 [AI for Cryptic Pockets](https://old.foldingathome.org/2026/05/28/ai-for-cryptic-pockets/) - Attention-enabled PocketMiner predicts cryptic pockets and allosteric coupling for drug discovery.
  - 📰 [AI and Folding@home](https://foldingathome.org/2026/03/05/ai-and-foldinghome/) - Overview of how AI accelerates Folding@home research in structure prediction, data analysis, and software development.
  - 📄 [AE-PocketMiner paper](https://doi.org/10.64898/2026.05.21.726899) - Graph neural network with attention for predicting cryptic pockets and allosteric communication (bioRxiv, 2026).
- 🧬 **[Rosetta@home](https://boinc.bakerlab.org/)** - Predicts protein structures and supports synthetic biology innovation. ([Repo](https://github.com/RosettaCommons/rosetta) | [Wikidata](https://www.wikidata.org/wiki/Q898343))
- 🌱 **[World Community Grid](https://www.worldcommunitygrid.org/)** - Runs humanitarian research on health, sustainability, and climate change. ([Wikidata](https://www.wikidata.org/wiki/Q826776))
  - 🔬 **[GPUGRID.net](https://gpugrid.net/)** ([Wikidata](https://www.wikidata.org/wiki/Q5872957)) - Molecular dynamics and protein simulations on GPUs for drug discovery and biomedical research.
- 🌌 **[Einstein@Home](https://einsteinathome.org/)** ([Wikidata](https://www.wikidata.org/wiki/Q1310156)) - Searches for gravitational waves and pulsars in massive astrophysical datasets.
  - 📄 [Three new gamma-ray pulsars in the inner galaxy](https://arxiv.org/abs/2509.21307) - New pulsars discovered via Einstein@home volunteer computing (Sep 2025).
- 💥 **[LHC@home](https://lhcathome.web.cern.ch/)** ([Repo](https://github.com/lfield/lhcathome)) [![GitHub stars](https://img.shields.io/github/stars/lfield/lhcathome)](https://github.com/lfield/lhcathome/stargazers) [![GitHub forks](https://img.shields.io/github/forks/lfield/lhcathome)](https://github.com/lfield/lhcathome/network) [![GitHub last commit](https://img.shields.io/github/last-commit/lfield/lhcathome)](https://github.com/lfield/lhcathome/commits/main) - Simulates CERN's Large Hadron Collider experiments to advance particle physics.
- 🧮 **[PrimeGrid](https://www.primegrid.com/)** ([Wikidata](https://www.wikidata.org/wiki/Q7243301)) - Searches for various types of prime numbers including Generalized Fermat, Cullen, Woodall, and mega primes.
- 🔢 **[SRBase](https://srbase.my-firewall.org/sr5/)** - Mathematical research solving Sierpinski/Riesel conjectures and finding large prime numbers.
- 🎲 **[yoyo@home](https://www.rechenkraft.net/yoyo/)** ([Wikidata](https://www.wikidata.org/wiki/Q3573013)) - Multi-project platform including ECM factorization, M Queens puzzle, and distributed.net OGR computations.
- 🔢 **[NumberFields@home](https://numberfields.asu.edu/NumberFields/)** - Algebraic number theory research searching for fields with special mathematical properties.
- 🌍 **[Climateprediction.net](https://www.climateprediction.net/)** ([Wikidata](https://www.wikidata.org/wiki/Q1101446)) - Climate modeling research studying weather patterns, climate change, and environmental impacts.
- 🧠 **[Science United](https://scienceunited.org/)** - BOINC platform supporting multiple research areas with user-selected project categories.
- 🧮 **[The Ramanujan Machine](https://www.ramanujanmachine.com/)** - AI-driven discovery of new mathematical formulas and conjectures using volunteer computing.
- 🔭 **[UCLA SETI (Zooniverse)](https://www.zooniverse.org/projects/ucla-seti-group/are-we-alone-in-the-universe)** - Citizen science project classifying radio signals to search for extraterrestrial intelligence.
- 💊 **[SIDock@home](https://www.sidock.si/sidock/)** - Biomedical research focusing on drug discovery and molecular docking simulations.
- 🖥️ **[iThena](https://root.ithena.net/usr/)** - Computer science research on distributed computing algorithms and systems.
- 🔢 **[LODA](https://boinc.loda-lang.org/loda/)** - Mathematics project using LODA language to find integer sequences and patterns.
- 🧪 **[DENIS@Home](https://denis.usj.es/denisathome/)** - Medical physiology research from San Jorge University studying human physiological systems.
- 🔢 **[GIMPS](https://www.mersenne.org/)** ([Wikidata](https://www.wikidata.org/wiki/Q330607)) - Great Internet Mersenne Prime Search, discovered the largest known prime in 2024 (41M digits).
- 📊 **[distributed.net](https://www.distributed.net/)** - Cryptographic challenges and optimal Golomb ruler searches, completed OGR-28 in 2022.

#### Wikipedia: List of Volunteer Computing Projects

A comprehensive and categorized list of past and present volunteer computing projects on [Wikipedia](https://en.wikipedia.org/wiki/List_of_volunteer_computing_projects).

---

## 📚 Research & Papers

Academic insights and deep technical dives into distributed volunteer computing.

- 📄 **[BOINC: A Platform for Volunteer Computing](https://arxiv.org/pdf/1903.01699)** (D. Anderson, 2019) - Describes the architecture, features, and implementation of the widely used BOINC middleware.
- 📈 **[The Computational and Storage Potential of Volunteer Computing](https://www.researchgate.net/publication/4241887_The_Computational_and_Storage_Potential_of_Volunteer_Computing)** (D. Anderson & G. Fedak, 2006) - Analyzes measurements from ~330k hosts to assess the capacity of volunteer computing beyond CPU power.
- ⚙️ **[Research on the Task Assignment Problem with Maximum Benefits in Volunteer Computing Platforms](https://www.mdpi.com/2073-8994/12/5/862)** (L. Wang et al., 2020) - Explores task scheduling strategies for maximizing benefits in VCPs considering deadlines.
- 👥 **[Retaining volunteers in volunteer computing projects](https://www.researchgate.net/publication/45461278_Retaining_volunteers_in_volunteer_computing_projects)** (D. Nov, O. Arazy, D. Anderson, 2011) - Investigates factors influencing volunteer retention and contribution levels.
- 💡 **[Personal Volunteer Computing](https://arxiv.org/vc/arxiv/papers/1804/1804.01482v1.pdf)** (S. Cahon et al., 2018) - Proposes a more personal, web-based approach to volunteer computing and introduces the Pando platform.
- ❤️ **[Volunteer computing: A model of factors determining contribution to community-based scientific research](https://dl.acm.org/doi/abs/10.1145/1772690.1772766)** (O. Nov, D. Anderson, O. Arazy, 2010) - Develops and tests a model of user motivation based on SETI@home survey data and activity logs.
- 📄 **["Improving the Productivity of Volunteer Computing" (Toth, 2008)](https://digital.wpi.edu/concern/etds/kk91fk601?locale=en)** - Examines task retrieval policies and techniques to increase productivity.
- 📄 **[AIArena: Scalable and Secure Decentralized AI Training](https://doi.org/10.1145/3701716.3715484)** (ACM, 2025) - Blockchain-based decentralized AI training with 600+ training nodes and 63K delegators.
- 📄 **[Lattica: Decentralized Cross-NAT Communication](https://doi.org/10.48550/arxiv.2510.00183)** (arXiv, 2025) - Framework for distributed AI with NAT traversal, CRDT-based data store, and DHT content discovery.
- 📄 **[Boltz-1: Open-source biomolecular structure prediction](https://doi.org/10.1101/2024.11.19.624167)** (bioRxiv, 2024) - First open-source model matching AlphaFold3 accuracy. ([Repo](https://github.com/jwohlwend/boltz))
- 📄 **[Cislunar Orbit Stability Census via VC](https://doi.org/10.20944/preprints202604.0498.v2)** (Preprints, 2026) - Uses BOINC and deep learning for 1M orbit stability analysis.
- 📄 **[Distributed Deep Learning Using VC-Like Paradigm](https://arxiv.org/abs/2103.08894)** (arXiv, 2021) - 70-90% cost reduction using volunteer computing paradigm for distributed deep learning.

---

## 👥 Communities & Forums

Places to ask questions, meet contributors, or follow development.

- 💬 [BOINC Message Boards](https://boinc.berkeley.edu/dev/forum_index.php)
- 📢 [Reddit: r/BOINC](https://www.reddit.com/r/BOINC/)
- 🗨️ [BOINC Discord](https://discord.gg/boinc)
<!--lint disable awesome-list-item-->
- *(Project-specific forums, like Folding@home's, also exist)*
<!--lint enable awesome-list-item-->

---

## 🔍 Related & Historical Projects

Projects that are no longer active or are closely related to volunteer computing.

<!--lint disable awesome-list-item-->
- 🔭 **[SETI@home](https://setiathome.berkeley.edu/)** ([Wikidata](https://www.wikidata.org/wiki/Q46533)) - Search for Extraterrestrial Intelligence using volunteer computing. Ran 1999-2020, analyzing radio signals from space.
  - 📰 [SETI@home publishes final data results](https://news.berkeley.edu/2025/06/12/seti-home-publishes-final-data-results/) - 21 years of citizen science: 12B signals analyzed, 100 candidate signals identified (Berkeley News, 2025).
  - 📄 [SETI@home Data Analysis Paper](https://iopscience.iop.org/article/10.3847/1538-3881/ade5ab) - Final scientific analysis of SETI@home signal data (The Astronomical Journal, 2025).
  - 📄 [SETI@home Data Acquisition Paper](https://iopscience.iop.org/article/10.3847/1538-3881/ade5a7) - Technical overview of SETI@home's distributed data processing architecture (The Astronomical Journal, 2025).
<!--lint enable awesome-list-item-->

---

## 📺 Articles & Videos

Resources to learn more about the real-world impact and concepts of volunteer computing.

- 📰 [What is Volunteer Computing? - TechRadar](https://www.techradar.com/news/what-is-volunteer-computing) - General overview article.
- 🌐 [Volunteer computing - Wikipedia](https://en.wikipedia.org/wiki/Volunteer_computing) - Comprehensive encyclopedia article.
- 📹 [CERN Explainer: What is volunteer computing? - LHC@home](https://lhcathome.web.cern.ch/about/volunteer-computing) - Explanation from the perspective of a major project.
- 🎓 [Khan Academy: Citizen science (article)](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:computing-innovations/xcae6f4a7ff015e7d:crowdsourcing-innovations/a/citizen-science) - Discusses volunteer computing as a form of citizen science.
- 📰 [Petals supports 405B via volunteer GPU swarm](https://runtimewire.com/article/petals-405b-model-volunteer-gpu-swarm) - Petals now supports Llama 3.1 405B through decentralized volunteer GPUs (Jul 2026).

---

## 🔗 Related Concepts

Areas closely related to or overlapping with volunteer computing.

<!--lint disable awesome-list-item-->
- **Citizen Science** - Public participation in scientific research, often involving data collection or analysis. Volunteer computing is sometimes considered a sub-field.
  - [Zooniverse](https://www.zooniverse.org/) - Popular platform for web-based citizen science projects (classification, transcription).
  - [SciStarter](https://scistarter.org/) - Hub for discovering citizen science projects.
- **Distributed Computing** - General term for systems where components are located on different networked computers, communicating and coordinating actions.
- **Grid Computing** - Often involves more formal resource sharing agreements and infrastructure, typically within or between organizations, compared to the public volunteer model.
- **Federated Learning** - A machine learning technique that trains algorithms across multiple decentralized edge devices or servers holding local data samples, without exchanging them. Shares principles with volunteer computing regarding utilizing distributed resources.
- **DePIN (Decentralized Physical Infrastructure Networks)** - Blockchain-based paradigm for coordinating real-world hardware (compute, storage, bandwidth) via token incentives. Overlaps with volunteer computing in utilizing distributed, crowd-sourced resources.
<!--lint enable awesome-list-item-->

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ranjithrajv/awesome-volunteer-computing&type=Date)](https://star-history.com/#ranjithrajv/awesome-volunteer-computing&Date)

---

## 🤝 Contributing

Found a project we missed? Want to improve descriptions or links? Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.
