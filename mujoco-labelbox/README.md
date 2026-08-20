# MuJoCo LabelBox

> Soft/continuum robot modelling and control: PDE control, neural ODEs, Lie algebraic methods.

*4 items · saved between 2026-07-19 and 2026-07-19 · from my [Raindrop.io](https://raindrop.io) collection*

## Contents

### [Estimating Dynamic Soft Continuum Robot States From Boundaries](https://arxiv.org/abs/2505.04491)

- **Saved:** 2026-07-19
- **PDF:** [`pdfs/estimating-dynamic-soft-continuum-robot-states-from.pdf`](pdfs/estimating-dynamic-soft-continuum-robot-states-from.pdf) *(fetched from arXiv)*
- **My note:** State estimation is one of the fundamental problems in robotics. For soft continuum robots, this task is particularly challenging because their states (poses, strains, internal wrenches, and velocities) are inherently infinite-dimensional functions due to their continuous deformability. Traditional sensing techniques, however, can only provide discrete measurements. Recently, a dynamic state estimation method known as a \textit{boundary observer} was introduced, which uses Cosserat rod theory to recover all infinite-dimensional states by measuring only the tip velocity. In this work, we present a dual design that instead relies on measuring the internal wrench at the robot's base. Despite the duality, this new approach offers a key practical advantage: it requires only a force/torque (FT) sensor embedded at the base and eliminates the need for external motion capture systems. Both observer types are inspired by principles of energy dissipation and can be naturally combined to enhance performance. We conduct a Lyapunov-based analysis to study the convergence rate of these boundary observers and reveal a useful property: as the observer gains increase, the convergence rate initially improves and then degrades. This convex trend enables efficient tuning of the observer gains. We also identify special cases where linear and angular states are fully determined by each other, which further relaxes sensing requirements. Experimental studies using a tendon-driven continuum robot validate the convergence of all observer variants under fast dynamic motions, the existence of optimal gains, robustness against unknown external forces, and the algorithm's real-time computational performance.

### [Deep Reinforcement Learning-Based Motion Planning and PDE Control...](https://arxiv.org/abs/2506.08639)

- **Saved:** 2026-07-19
- **PDF:** [`pdfs/deep-reinforcement-learning-based-motion-planning-and-pde.pdf`](pdfs/deep-reinforcement-learning-based-motion-planning-and-pde.pdf) *(fetched from arXiv)*
- **Excerpt:** This article presents a motion planning and control framework for flexible robotic manipulators, integrating deep reinforcement learning (DRL) with a nonlinear partial differential equation (PDE) controller. Unlike conventional approaches that focus solely on control, we demonstrate that the desired

### [Modular Lie Algebraic PDE Control of Multibody Flexible Manipulators](https://arxiv.org/abs/2605.06709)

- **Saved:** 2026-07-19
- **PDF:** [`pdfs/modular-lie-algebraic-pde-control-of-multibody-flexible.pdf`](pdfs/modular-lie-algebraic-pde-control-of-multibody-flexible.pdf) *(fetched from arXiv)*
- **Excerpt:** This paper presents a subsystem-based adaptive control framework for serial flexible manipulators with an arbitrary number of links, in which the elastic deformation PDE of each link is carried through the entire control design without spatial discretization or modal truncation. All dynamic quantiti

### [Knowledge-based Neural Ordinary Differential Equations for...](https://arxiv.org/abs/2408.07776)

- **Saved:** 2026-07-19
- **PDF:** [`pdfs/knowledge-based-neural-ordinary-differential-equations-for.pdf`](pdfs/knowledge-based-neural-ordinary-differential-equations-for.pdf) *(fetched from arXiv)*
- **Excerpt:** Soft robots have many advantages over rigid robots thanks to their compliant and passive nature. However, it is generally challenging to model the dynamics of soft robots due to their high spatial dimensionality, making it difficult to use model-based methods to accurately control soft robots. It of

---

## 📝 Learnings

<!-- Add your takeaways from this collection here: key ideas, connections between papers, what changed your thinking. -->

*(to be written)*
