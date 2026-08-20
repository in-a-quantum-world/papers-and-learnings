# 📚 Papers & Learnings

*Reading an academic paper every day, and keeping my findings.*

A structured archive of every paper, article, and resource I've read and saved — exported from my [Raindrop.io](https://raindrop.io) collections, preserved here with original save-dates, tags, notes, and (where available) the full PDFs.

Each collection folder contains a `README.md` listing every item with the date I saved it, my tags and notes, plus a **Learnings** section where I distil what I took away from that body of reading.

**95 items · 20 collections · exported 2026-08-12**

## Collections

| Collection | Items | Focus |
|---|---|---|
| [defenseTech](defense-tech/) | 11 | Autonomous soaring, drone flight control, and the defense-tech landscape (PX4, Skynode, AI-enabled warfare analysis). |
| [ML Research](ml-research/) | 7 | Foundational ML research: scaling laws, flow matching, PINNs, AlphaGeometry, quantization. |
| [intrinsic](intrinsic/) | 6 | Robot manipulation and imitation learning: diffusion policies, behavioural cloning, ALOHA/ACT, MimicGen, RL with human-in-the-loop. |
| [Quantum Computing](quantum-computing/) | 6 | Quantum computing platforms, photonics (Quandela), and the state of the field. |
| [ML tools](ml-tools/) | 5 | Practical tools and platforms: Gymnasium, OpenCV, Palantir AIP, tutorials. |
| [Robotics, simulations](robotics-simulations/) | 5 | Physical AI, simulation (Isaac Sim), humanoids, and robotics challenges. |
| [MuJoCo LabelBox](mujoco-labelbox/) | 4 | Soft/continuum robot modelling and control: PDE control, neural ODEs, Lie algebraic methods. |
| [Neurotech](neurotech/) | 4 | Brain emulation, EEG-to-text, neural emulators. |
| [Quant Prep](quant-prep/) | 4 | Quant interview prep: probability, Jane Street questions, resources. |
| [AGI](agi/) | 2 | AGI alignment and futures: agency preservation, forecasting. |
| [AI News](ai-news/) | 2 | Notable AI news and reports. |
| [Courses](courses/) | 2 | Courses and structured learning material. |
| [Deep Learning](deep-learning/) | 2 | Deep learning textbooks (Goodfellow et al., Prince). |
| [Neural Computing](neural-computing/) | 2 | Biological/neural computing: Cortical Labs and researchers in the space. |
| [Founder Blog](founder-blog/) | 1 | Founder blogs and personal sites worth revisiting. |
| [Hackathons](hackathons/) | 1 | Hackathons and competitions. |
| [Investments, Finance](investments-finance/) | 1 | Investing and finance tools. |
| [Quantum Computing for Finance](quantum-finance/) | 1 | Where quantum computing meets quantitative finance. |
| [Startups, YC](startups-yc/) | 1 | Startup ecosystem and accelerators. |
| [Unsorted](unsorted/) | 28 | Everything not yet filed into a collection — papers, challenges, applications, and reading. |

## How this repo is built

- Source of truth: my Raindrop.io account (raw export in [`tools/`](tools/)).
- Paper PDFs are auto-downloaded by a [GitHub Actions workflow](.github/workflows/fetch-pdfs.yml) from a [manifest](tools/pdf-manifest.csv) of open-access sources (arXiv, PMLR, PLOS, …), so the papers are preserved even if links rot.
- Paywalled items (IEEE, ResearchGate) are kept as links only.
