# Awesome Volunteer Computing [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**volunteer computing** — practice of donating idle computing power to help solve real-world scientific and humanitarian problems.

Early pioneers like **[GIMPS](https://www.mersenne.org/)** and **[distributed.net](https://www.distributed.net/)** paved the way for modern platforms that aggregate these resources into powerful virtual supercomputers, enabling research otherwise impossible.

> Below is a curated list of awesome platforms, projects, and tools for volunteer computing

---

## 📚 Contents

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
- [Articles & Videos](#articles--videos)
- [Contributing](#contributing)

---

## ⚙️ Platforms & Infrastructure

Volunteer computing systems people can join or build on top of.

### 🧬 Hybrid or Multi-Platform

- 🌸 **[Petals](https://petals.dev/)** ([Repo](https://github.com/bigscience-workshop/petals)) [![GitHub stars](https://img.shields.io/github/stars/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/stargazers) [![GitHub forks](https://img.shields.io/github/forks/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/network) [![GitHub last commit](https://img.shields.io/github/last-commit/bigscience-workshop/petals)](https://github.com/bigscience-workshop/petals/commits/main) – Peer-to-peer network that runs large language models (LLMs) like BLOOM across distributed GPUs and contributors' machines.
- 🧱 **[Exo](https://github.com/exo-explore/exo)** [![GitHub stars](https://img.shields.io/github/stars/exo-explore/exo)](https://github.com/exo-explore/exo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/exo-explore/exo)](https://github.com/exo-explore/exo/network) [![GitHub last commit](https://img.shields.io/github/last-commit/exo-explore/exo)](https://github.com/exo-explore/exo/commits/main) – Run your own AI cluster at home with everyday devices. Unifies existing devices (iPhone, iPad, Android, Mac, NVIDIA, Raspberry Pi) into one powerful distributed GPU for running various AI models including LLaMA, Mistral, and LlaVA
- 🤖 **[autoresearch@home](https://github.com/mutable-state-inc/autoresearch-at-home)** ([Website](https://www.ensue-network.ai/autoresearch)) [![GitHub stars](https://img.shields.io/github/stars/mutable-state-inc/autoresearch-at-home)](https://github.com/mutable-state-inc/autoresearch-at-home/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mutable-state-inc/autoresearch-at-home)](https://github.com/mutable-state-inc/autoresearch-at-home/network) [![GitHub last commit](https://img.shields.io/github/last-commit/mutable-state-inc/autoresearch-at-home)](https://github.com/mutable-state-inc/autoresearch-at-home/commits/main) – A collaborative, SETI@home-style fork of autoresearch where multiple agents on different GPUs share results to improve language models through the Ensue shared memory network.
- 🧠🧱 **[MultiCortex EXO](https://github.com/cabelo/multicortex-exo)** [![GitHub stars](https://img.shields.io/github/stars/cabelo/multicortex-exo)](https://github.com/cabelo/multicortex-exo/stargazers) [![GitHub forks](https://img.shields.io/github/forks/cabelo/multicortex-exo)](https://github.com/cabelo/multicortex-exo/network) [![GitHub last commit](https://img.shields.io/github/last-commit/cabelo/multicortex-exo)](https://github.com/cabelo/multicortex-exo/commits/main) – A portable system that can be booted from a USB flash drive, with the fantastic Exo project pre-installed. It allows any computer to become a node for creating a decentralized AI framework. It allows pooling of computing power from multiple devices, leveraging CPUs, GPUs, NPUs, and other accelerators.  

### 💻 Desktop-Native

- 🧩 **[BOINC](https://boinc.berkeley.edu/)** ([Repo](https://github.com/BOINC/boinc)) [![GitHub stars](https://img.shields.io/github/stars/BOINC/boinc)](https://github.com/BOINC/boinc/stargazers) [![GitHub forks](https://img.shields.io/github/forks/BOINC/boinc)](https://github.com/BOINC/boinc/network) [![GitHub last commit](https://img.shields.io/github/last-commit/BOINC/boinc)](https://github.com/BOINC/boinc/commits/main) – The gold standard in open-source volunteer computing, powering dozens of scientific research projects.
- 🖥️ **[GridRepublic](https://www.gridrepublic.org/)** – A user-friendly frontend for managing BOINC projects and participation.
- 💡 **[Charity Engine](https://www.charityengine.com/)** – Turns donated computing power into charitable donations or rewards for users.
- 🧪 **[XtremWeb](http://www.xtremweb.net/)** [![Legacy](https://img.shields.io/badge/-Legacy-red)](https://medium.com/iex-ec/iex-ec-adopts-xtremweb-hep-the-open-source-software-for-desktop-grid-computing-b5ad9836a54b) – Research platform for global distributed computing used by academic institutions.

### 📱 Mobile-Based

- 📲 **[DreamLab](https://www.vodafone.com/vodafone-foundation/focus-areas/dreamlab-app)** [![Legacy](https://img.shields.io/badge/-Legacy-red)](https://en.wikipedia.org/wiki/DreamLab_(app)) – Vodafone Foundation's mobile app that powers medical and nutritional research while your phone charges.

### 🌐 Browser-Based

- 🕸️ **[distri.js.org](https://distri.js.org/)** ([Repo](https://github.com/ethan-dorta/Distri.js)) [![GitHub stars](https://img.shields.io/github/stars/ethan-dorta/Distri.js)](https://github.com/ethan-dorta/Distri.js/stargazers) [![GitHub forks](https://img.shields.io/github/forks/ethan-dorta/Distri.js)](https://github.com/ethan-dorta/Distri.js/network) [![GitHub last commit](https://img.shields.io/github/last-commit/ethan-dorta/Distri.js)](https://github.com/ethan-dorta/Distri.js/commits/main) – A minimalist JavaScript framework enabling distributed computing inside any modern web browser using Web Workers.
- 🐼 **[Pando](https://github.com/pando-project/pando)** [![GitHub stars](https://img.shields.io/github/stars/pando-project/pando)](https://github.com/pando-project/pando/stargazers) [![GitHub forks](https://img.shields.io/github/forks/pando-project/pando)](https://github.com/pando-project/pando/network) [![GitHub last commit](https://img.shields.io/github/last-commit/pando-project/pando)](https://github.com/pando-project/pando/commits/main) – A personal volunteer computing platform for the Web, allowing easy setup for personal or shared computations via JavaScript. ([See Paper](https://arxiv.org/vc/arxiv/papers/1804/1804.01482v1.pdf))

---

## 🛠️ For Developers

Libraries, SDKs, and tools for building or contributing to volunteer computing systems.

- 🧰 **[BOINC Development Resources](https://boinc.berkeley.edu/trac/wiki/SoftwareDevelopment)** ([Repo](https://github.com/BOINC/boinc-dev-doc)) [![GitHub stars](https://img.shields.io/github/stars/BOINC/boinc-dev-doc)](https://github.com/BOINC/boinc-dev-doc/stargazers) [![GitHub forks](https://img.shields.io/github/forks/BOINC/boinc-dev-doc)](https://github.com/BOINC/boinc-dev-doc/network) [![GitHub last commit](https://img.shields.io/github/last-commit/BOINC/boinc-dev-doc)](https://github.com/BOINC/boinc-dev-doc/commits/main) – Comprehensive guide covering the SDK, APIs, server/client setup, and creating BOINC-compatible applications.
- 🌸 **[Flower](https://github.com/adap/flower)** [![GitHub stars](https://img.shields.io/github/stars/adap/flower)](https://github.com/adap/flower/stargazers) [![GitHub forks](https://img.shields.io/github/forks/adap/flower)](https://github.com/adap/flower/network) [![GitHub last commit](https://img.shields.io/github/last-commit/adap/flower)](https://github.com/adap/flower/commits/main) – A federated learning framework that enables training machine learning models across distributed devices while preserving data privacy. Supports PyTorch Lightning and other ML frameworks
- 🌳 **[webrtc-tree-overlay](https://github.com/elavoie/webrtc-tree-overlay)** [![GitHub stars](https://img.shields.io/github/stars/elavoie/webrtc-tree-overlay)](https://github.com/elavoie/webrtc-tree-overlay/stargazers) [![GitHub forks](https://img.shields.io/github/forks/elavoie/webrtc-tree-overlay)](https://github.com/elavoie/webrtc-tree-overlay/network) [![GitHub last commit](https://img.shields.io/github/last-commit/elavoie/webrtc-tree-overlay)](https://github.com/elavoie/webrtc-tree-overlay/commits/main) – A library for building scalable WebRTC P2P mesh networks in a tree overlay structure, useful for browser-based distributed applications.
- 🔧 **[Volunteer Grid Toolkit (VGT)](https://sourceforge.net/projects/vgt/)** [![Legacy](https://img.shields.io/badge/-Legacy-red)](https://sourceforge.net/projects/vgt/) – A toolkit for experimenting with volunteer grid computing concepts. *Note: Check project activity/relevance.*
- 🔗 **[GridCoin Developer Information](https://wiki.gridcoin.us/Developer-Information)** ([Repo](https://github.com/gridcoin-community/Gridcoin-Research)) [![GitHub stars](https://img.shields.io/github/stars/gridcoin-community/Gridcoin-Research)](https://github.com/gridcoin-community/Gridcoin-Research/stargazers) [![GitHub forks](https://img.shields.io/github/forks/gridcoin-community/Gridcoin-Research)](https://github.com/gridcoin-community/Gridcoin-Research/network) [![GitHub last commit](https://img.shields.io/github/last-commit/gridcoin-community/Gridcoin-Research)](https://github.com/gridcoin-community/Gridcoin-Research/commits/main) – Resources for integrating blockchain-based incentives (GridCoin) with distributed computing (primarily BOINC).

---

## 🧪 Volunteer Projects

Scientific and research projects powered by public computing contributions.

- 🔬 **[Folding@home](https://foldingathome.org/)** – Simulates protein folding to better understand diseases like cancer and Alzheimer's. ([Repo](https://github.com/FoldingAtHome) | [Wikidata](https://www.wikidata.org/wiki/Q386283))
- 🧬 **[Rosetta@home](https://boinc.bakerlab.org/)** – Predicts protein structures and supports synthetic biology innovation. ([Repo](https://github.com/RosettaCommons/rosetta) | [Wikidata](https://www.wikidata.org/wiki/Q898343))
- 🌱 **[World Community Grid](https://www.worldcommunitygrid.org/)** – Runs humanitarian research on health, sustainability, and climate change. ([Wikidata](https://www.wikidata.org/wiki/Q826776))
  - 🔬 **[GPUGRID.net](https://gpugrid.net/)** ([Wikidata](https://www.wikidata.org/wiki/Q5872957)) – Molecular dynamics and protein simulations on GPUs for drug discovery and biomedical research.
- 🌌 **[Einstein@Home](https://einsteinathome.org/)** ([Wikidata](https://www.wikidata.org/wiki/Q1310156)) – Searches for gravitational waves and pulsars in massive astrophysical datasets.
- 👽 **[SETI@home](https://setiathome.berkeley.edu/)** ([Wikidata](https://www.wikidata.org/wiki/Q330835)) [![Legacy](https://img.shields.io/badge/-Legacy-red)](https://seti.berkeley.edu/hibernation/) – Based at UC Berkeley, a scientific experiment to Search for Extraterrestrial Intelligence (SETI)
- 💥 **[LHC@home](https://lhcathome.web.cern.ch/)** ([Repo](https://github.com/lfield/lhcathome)) [![GitHub stars](https://img.shields.io/github/stars/lfield/lhcathome)](https://github.com/lfield/lhcathome/stargazers) [![GitHub forks](https://img.shields.io/github/forks/lfield/lhcathome)](https://github.com/lfield/lhcathome/network) [![GitHub last commit](https://img.shields.io/github/last-commit/lfield/lhcathome)](https://github.com/lfield/lhcathome/commits/main) – Simulates CERN's Large Hadron Collider experiments to advance particle physics.
- 🧮 **[PrimeGrid](https://www.primegrid.com/)** ([Wikidata](https://www.wikidata.org/wiki/Q7243301)) – Searches for various types of prime numbers including Generalized Fermat, Cullen, Woodall, and mega primes.
- 🔢 **[SRBase](https://srbase.my-firewall.org/sr5/)** – Mathematical research solving Sierpinski/Riesel conjectures and finding large prime numbers.
- 🎲 **[yoyo@home](https://www.rechenkraft.net/yoyo/)** ([Wikidata](https://www.wikidata.org/wiki/Q3573013)) – Multi-project platform including ECM factorization, M Queens puzzle, and distributed.net OGR computations.
- 🔢 **[NumberFields@home](https://numberfields.asu.edu/NumberFields/)** – Algebraic number theory research searching for fields with special mathematical properties.
- 🌍 **[Climateprediction.net](https://www.climateprediction.net/)** ([Wikidata](https://www.wikidata.org/wiki/Q1101446)) – Climate modeling research studying weather patterns, climate change, and environmental impacts.
- 🧠 **[Science United](https://scienceunited.org/)** – BOINC platform supporting multiple research areas with user-selected project categories.
- 🧮 **[The Ramanujan Machine](https://www.ramanujanmachine.com/)** – AI-driven discovery of new mathematical formulas and conjectures using volunteer computing.
- 🔭 **[UCLA SETI (Zooniverse)](https://www.zooniverse.org/projects/ucla-seti-group/are-we-alone-in-the-universe)** – Citizen science project classifying radio signals to search for extraterrestrial intelligence.
- 💊 **[SIDock@home](https://www.sidock.si/sidock/)** – Biomedical research focusing on drug discovery and molecular docking simulations.
- 🖥️ **[iThena](https://root.ithena.net/usr/)** – Computer science research on distributed computing algorithms and systems.
- 🔢 **[LODA](https://boinc.loda-lang.org/loda/)** – Mathematics project using LODA language to find integer sequences and patterns.
- 🧪 **[DENIS@Home](https://denis.usj.es/denisathome/)** – Medical physiology research from San Jorge University studying human physiological systems.
- 🔢 **[GIMPS](https://www.mersenne.org/)** ([Wikidata](https://www.wikidata.org/wiki/Q330607)) – Great Internet Mersenne Prime Search, discovered the largest known prime in 2024 (41M digits).
- 📊 **[distributed.net](https://www.distributed.net/)** – Cryptographic challenges and optimal Golomb ruler searches, completed OGR-28 in 2022.

#### 📘 [Wikipedia: List of Volunteer Computing Projects](https://en.wikipedia.org/wiki/List_of_volunteer_computing_projects) – A comprehensive and categorized list of past and present volunteer computing projects.

---

## 📚 Research & Papers

Academic insights and deep technical dives into distributed volunteer computing.

- 📄 **[BOINC: A Platform for Volunteer Computing](https://arxiv.org/pdf/1903.01699)** (D. Anderson, 2019) – Describes the architecture, features, and implementation of the widely used BOINC middleware.
- 📈 **[The Computational and Storage Potential of Volunteer Computing](https://www.researchgate.net/publication/4241887_The_Computational_and_Storage_Potential_of_Volunteer_Computing)** (D. Anderson & G. Fedak, 2006) – Analyzes measurements from ~330k hosts to assess the capacity of volunteer computing beyond CPU power.
- ⚙️ **[Research on the Task Assignment Problem with Maximum Benefits in Volunteer Computing Platforms](https://www.mdpi.com/2073-8994/12/5/862)** (L. Wang et al., 2020) – Explores task scheduling strategies for maximizing benefits in VCPs considering deadlines.
- 👥 **[Retaining volunteers in volunteer computing projects](https://www.researchgate.net/publication/45461278_Retaining_volunteers_in_volunteer_computing_projects)** (D. Nov, O. Arazy, D. Anderson, 2011) – Investigates factors influencing volunteer retention and contribution levels.
- 💡 **[Personal Volunteer Computing](https://arxiv.org/vc/arxiv/papers/1804/1804.01482v1.pdf)** (S. Cahon et al., 2018) – Proposes a more personal, web-based approach to volunteer computing and introduces the Pando platform.
- ❤️ **[Volunteer computing: A model of factors determining contribution to community-based scientific research](https://dl.acm.org/doi/abs/10.1145/1772690.1772766)** (O. Nov, D. Anderson, O. Arazy, 2010) – Develops and tests a model of user motivation based on SETI@home survey data and activity logs.
- 📄 **[Improving the Productivity of Volunteer Computing" (Toth, 2008)](https://digital.wpi.edu/concern/etds/kk91fk601?locale=en)** – Examines task retrieval policies and techniques to increase productivity.

---

## 👥 Communities & Forums

Places to ask questions, meet contributors, or follow development.

- 💬 [BOINC Message Boards](https://boinc.berkeley.edu/dev/forum_index.php)
- 📢 [Reddit: r/BOINC](https://www.reddit.com/r/BOINC/)
- 🗨️ [BOINC Discord](https://discord.gg/boinc)
- *(Project-specific forums, like Folding@home's, also exist)*

---

## 📺 Articles & Videos

Resources to learn more about the real-world impact and concepts of volunteer computing.

- 📰 [What is Volunteer Computing? – TechRadar](https://www.techradar.com/news/what-is-volunteer-computing) – General overview article.
- 🌐 [Volunteer computing - Wikipedia](https://en.wikipedia.org/wiki/Volunteer_computing) – Comprehensive encyclopedia article.
- 📹 CERN Explainer: [What is volunteer computing? | LHC@home](https://lhcathome.web.cern.ch/about/volunteer-computing) – Explanation from the perspective of a major project.
- 🎓 Khan Academy: [Citizen science (article)](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:computing-innovations/xcae6f4a7ff015e7d:crowdsourcing-innovations/a/citizen-science) – Discusses volunteer computing as a form of citizen science.

---

## 🔗 Related Concepts

Areas closely related to or overlapping with volunteer computing.

- **Citizen Science:** Public participation in scientific research, often involving data collection or analysis. Volunteer computing is sometimes considered a sub-field.
    - [Zooniverse](https://www.zooniverse.org/): Popular platform for web-based citizen science projects (classification, transcription).
    - [SciStarter](https://scistarter.org/): Hub for discovering citizen science projects.
- **Distributed Computing:** General term for systems where components are located on different networked computers, communicating and coordinating actions.
- **Grid Computing:** Often involves more formal resource sharing agreements and infrastructure, typically within or between organizations, compared to the public volunteer model.
- **Federated Learning:** A machine learning technique that trains algorithms across multiple decentralized edge devices or servers holding local data samples, without exchanging them. Shares principles with volunteer computing regarding utilizing distributed resources.

---

## 🤝 Contributing

Found a project we missed? Want to improve descriptions or links? Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started.

---

## 📄 License

[CC0 1.0 Universal (Public Domain Dedication)](LICENSE)

> Inspired by [awesome](https://awesome.re), a community-driven standard for curated knowledge.
