# Challenge-to-model map

The model should be selected from the scoring problem backward, rather than from architecture popularity forward.

## Task contracts

| Task | Released training conditions | Hidden prediction | Ranked questions |
|---|---|---|---|
| T1 | heart-centred scRNA-seq at E8.5 and E9.5 | expression populations at later stages | differential genes, change direction, cell-state distribution, gene-gene co-variation |
| T2 | 3D MERFISH stage ladders for heart and whole embryo | expression and 3D coordinates at interpolated or extrapolated stages | expression change, cell-state distribution, shape/scale, local spatial organisation |
| T3 | wild-type development and Mab21l2 knockout at E9.5 | Gata4 or β-catenin knockout population at E8.75 | response genes, direction, magnitude, cell-state distribution |

Sources: [T1](https://virtualembryo.ai/challenge/tasks/temporal), [T2](https://virtualembryo.ai/challenge/tasks/spatial), [T3](https://virtualembryo.ai/challenge/tasks/perturbation), and the [evaluation pages](https://virtualembryo.ai/challenge/evaluation).

## Consequences for modeling

### The output is a distribution

No task asks for a single average profile or matched cell-by-cell prediction. A good pseudobulk with collapsed cellular diversity loses the population and covariance terms. Generators must preserve joint residual structure; adding independent noise gene by gene is not sufficient.

### Developmental samples are unpaired

Each stage comes from different embryos and destructive measurements. Cell index is not an identity across time. Regression losses that pair arbitrary cells impose false supervision. Distributional objectives, optimal transport couplings and state-level summaries are more appropriate.

### T2 coordinates are relational

Embryos are imaged in local frames. Absolute coordinate mean-squared error is ill posed across samples. T2 requires methods built from internal distances, local neighborhoods, equivariant geometry or an explicit alignment step. Physical scale must remain separate from normalized shape because both are evaluated.

### T3 is a delta problem

Absolute mutant expression remains close to matched wild type. The informative target is the wild-type-to-knockout response. Models should predict a sparse, signed and calibrated change, while separately modeling changes in the population mixture.

## Information limits

T1 has only one observed transition interval. Many future vector fields explain E8.5 to E9.5 equally well, so a flexible neural ODE is not automatically identifiable. T3 has only one observed knockout, so randomly splitting its cells cannot validate unseen-gene generalization. T2 interpolation is better constrained than heart extrapolation and should be treated as a different experimental regime.

These limits motivate shrinkage, biological priors, compliant external supervision and explicit uncertainty. They also define the claims that local validation cannot support.
