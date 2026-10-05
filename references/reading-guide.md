# Reading guide

The catalog is broader than anyone needs for a first implementation. This guide identifies the papers that change a concrete design decision. IDs refer to `papers.csv`.

## T1: from snapshots to future populations

1. **P01 · Waddington-OT** — establishes unbalanced transport for developmental snapshots and explicit growth/death estimates. Read it to understand why unpaired populations need a coupling and why mass should not be forced to match.
2. **P03 · scNODE** — one of the closest published formulations of unobserved-time expression generation. Its reported degradation with extrapolation distance is directly relevant.
3. **P07 · GENOT** — supplies stochastic, entropic transport maps and flow matching. It is useful for one-to-many transitions, but does not solve developmental extrapolation by itself.
4. **P20 · scMix** and **P28 · latent GP + OT** — recent time-interval-aware alternatives. Both deserve comparison against a low-capacity trend because T1 exposes only one official transition interval.
5. **P05 · CellRank 2** — useful for fate and branch priors; it is not a full expression generator.

## T2: expression and geometry together

1. **P04 · moscot** — the central reference for scalable temporal and spatial OT in single-cell genomics.
2. **P07 · GENOT** — relevant when source and target spaces have relational rather than directly comparable geometry.
3. **P08 · E(n)-equivariant GNNs** — a clean architectural basis for local coordinate updates without a common frame. Its reflection equivariance must be understood when laterality matters.
4. **P21/P25 · MIOFlow** — population dynamics on a learned manifold, including recent spatial extensions.
5. **P27 · unified geometric framework** — a highly relevant 2026 preprint; treat its comparative claims as provisional until independently reproduced.

## T3: unseen genes with almost no task-specific supervision

1. **P17, P18 and P24 · perturbation benchmarks** — read these first. They explain why global fit or systematic variation can make a complex model look better than its gene-specific prediction actually is.
2. **P12 · CellOracle** — provides an interpretable context-specific GRN and in-silico perturbation framework. Its TF-centered assumptions do not cover every signaling protein.
3. **P11 · GEARS** — the main graph-conditioned unseen-perturbation reference. Its training regime contains far more perturbations than the challenge provides.
4. **P09 · CellOT** — appropriate for learning the observed WT-to-Mab21l2 distributional map, but not sufficient to identify a different target gene.
5. **P19 · State** and **P26 · CisTransCell** — promising context and gene-feature transfer approaches. Both need strict source and species audits; P26 remains a preprint.

## Foundation-model decision

Read **P13–P16** after a working non-foundation baseline exists. The useful question is not whether the pretrained model embeds cells attractively, but whether it improves a fixed downstream distributional or perturbation head under gene-disjoint, context-disjoint and stage-disjoint evaluation.

## What not to infer

- Success on interpolation does not establish long-range extrapolation.
- Success on drug response does not establish unseen genetic knockout response.
- A visually coherent latent space does not establish calibrated gene-level change.
- A transport coupling is an inferred statistical relation, not observed lineage tracing.
- Pretraining scale does not replace protected-stage and genotype provenance review.
