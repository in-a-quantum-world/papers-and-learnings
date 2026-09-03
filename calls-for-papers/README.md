# Calls for Papers

> Open calls, submission portals and deadline trackers for ML/robotics conferences and workshops — the "what could I actually submit to" shelf, as opposed to the "what should I read" ones.

*5 items · collection started 2026-09-03*

## ⏳ Deadlines

Checked 2026-09-03. **Always confirm on the source page — workshop deadlines move, usually later.**

| Call | Deadline (AoE) | Notification | Format | Status |
|---|---|---|---|---|
| [World Models in Physical AI](https://www.worldmodels-physicalai.com/cfp.html) — NeurIPS 2026, Sydney | **2026-09-05** | 2026-09-29 | ≤8 pages + refs, non-archival | 🔴 **Open — 2 days** |
| [Robot Learning with World Models](https://robowm-ws.github.io/) — NeurIPS 2026, Sydney | 2026-09-02 | 2026-09-25 | 8 pages (full) / 2–4 (short), non-archival | ⚫ Closed — watch for 2027 |

NeurIPS 2026 accepted **102 workshops** across Sydney (48, Dec 11–12), Paris (28, Dec 12–13) and
Atlanta (26, Dec 12–13). The suggested workshop submission date was 2026-08-29, so most other
workshop deadlines have now passed — but each workshop sets and advertises its own, and extensions
are common. The full list is in the [NeurIPS workshops
announcement](https://blog.neurips.cc/2026/08/10/announcing-the-neurips-2026-workshops/); use the
AI Workshop Tracker below to catch the ones still open.

## Contents

### [World Models in Physical AI — NeurIPS 2026 Workshop (CFP)](https://www.worldmodels-physicalai.com/cfp.html)

- **Saved:** 2026-09-03 · **Tags:** `CFP` `NeurIPS 2026` `world models` `physical AI` `open`
- **Submit via:** [OpenReview — NeurIPS.cc/2026/Workshop/WM_PAI](https://openreview.net/group?id=NeurIPS.cc/2026/Workshop/WM_PAI)
- **My note:** Deadline **2026-09-05 AoE**, already extended a week from the original 2026-08-29. Up to 8 pages excluding references, **non-archival** — so accepting here doesn't burn the work for a later archival venue, which makes it a low-risk first submission. Notification 2026-09-29, camera-ready November, workshop 12 or 13 December in Sydney. Solicits: representations and architectures (latent vs. pixel models, 3D dynamics), world models for action (model-based RL, planning), generative simulation (data generation, sim-to-real), evaluation (physical correctness, robustness, benchmarks), scaling and foundation world models, and safety/reliability. Organised largely out of NVIDIA (Jenny Schmalfuss, German Ros, Despoina Paschalidou, Jose M. Alvarez) plus Roberto Martín-Martín (UT Austin); speakers include Danijar Hafner, Katerina Fragkiadaki and Max Jiang. The evaluation and sim-to-real tracks sit right on top of the [mujoco-labelbox](../mujoco-labelbox/) and [intrinsic](../intrinsic/) collections.

### [Robot Learning with World Models — NeurIPS 2026 Workshop](https://robowm-ws.github.io/)

- **Saved:** 2026-09-03 · **Tags:** `CFP` `NeurIPS 2026` `robot learning` `world models` `closed`
- **My note:** *Deadline was 2026-09-02 AoE — closed as of today.* Logged as a venue to track for next year, and because the accepted papers will be posted publicly (non-archival) and are worth reading. Full papers up to 8 pages, short papers 2–4, NeurIPS or ICLR format; notification 2026-09-25; workshop 11 or 12 December, Sydney. Topics: "World Action Models", reasoning over imagined scenarios, multi-modal sensing beyond vision, physical accuracy, and evaluation benchmarks. Note it accepts **2–4 page short papers** — a much lower bar than a full workshop paper, worth remembering as an entry route for the 2027 edition.

### [AI Workshop Tracker](https://aiworkshoptracker.com/)

- **Saved:** 2026-09-03 · **Tags:** `tracker` `deadlines` `workshops` `tool`
- **My note:** The single most useful thing here — aggregates deadlines, past editions and accepted papers for AI/ML/robotics workshops across COLM, CoRL, CVPR, ECCV, ICLR, ICML, ICRA, IROS and NeurIPS. As of 2026-09-03 it lists 938 workshop editions, 20,606 papers and **119 open calls**, browsable by conference, year or topic (agents, computer vision, safety & alignment, robotics, 20+ categories). Flags deadline extensions. Has email alerts filtered by conference and topic — worth subscribing rather than checking manually, since the whole failure mode with workshops is finding out two days late.

### [OpenReview](https://openreview.net/about)

- **Saved:** 2026-09-03 · **Tags:** `platform` `peer review` `submissions`
- **My note:** The submission and review platform most ML venues run on — where the actual paper upload happens once a CFP points you at a venue group. Run as a nonprofit out of Andrew McCallum's lab at UMass Amherst; papers and submissions are free to read, and for many venues you can read the reviews themselves. Useful beyond submitting: reading the review threads on accepted and rejected papers at a venue is the cheapest way to learn what its reviewers actually reward.

### [IEEE Conferences & Events Search](https://conferences.ieee.org/conferences_events/)

- **Saved:** 2026-09-03 · **Tags:** `IEEE` `conferences` `directory` `robotics`
- **My note:** IEEE's own directory for finding its conferences and events — the route to ICRA, IROS, CASE and the rest of the robotics/automation calendar, which mostly sit outside the NeurIPS/ICML orbit the trackers above focus on. *Couldn't load this one to verify details — the site blocks automated fetches (HTTP 418), so check the search and filtering options yourself.*

---

## 📝 Learnings

<!-- Add your takeaways from this collection here: key ideas, connections between papers, what changed your thinking. -->

**How the workshop route works, as I understand it so far:**

- Workshop papers are short (2–8 pages) and usually **non-archival**, meaning accepting one does not
  stop me submitting the full version to an archival conference or journal later. That makes them a
  genuinely low-risk way in, unlike a main-track submission.
- Short-paper tracks (2–4 pages) are the lowest bar of all and exist at several workshops.
- Deadlines cluster hard: NeurIPS workshops mostly landed on or near 2026-08-29 this year. Missing
  the cluster means waiting for the next conference cycle, so the alerts matter more than the browsing.

**Where my existing work might fit:** the physical-AI and evaluation angles in
[mujoco-labelbox](../mujoco-labelbox/) and [intrinsic](../intrinsic/) map onto the world-model
workshops above; the evaluation-validity and memory-contamination thread in
[ai-safety](../ai-safety/) maps onto safety & alignment workshop tracks — which the AI Workshop
Tracker lists as one of its browsable topics.
