# EmbryoBridge: a unified but task-aware model

EmbryoBridge is a proposed architecture, not a reported result. Its purpose is to turn the literature review into a falsifiable research program.

## Shared representation

Each cell is encoded as `z = E(x, gene_modules, missing_mask)`. The encoder combines low-rank expression with pathway/regulon summaries and retains a mask for genes absent from a spatial panel. A shared stochastic decoder maps latent cells back to the exact board gene order and preserves correlated residuals.

At the population level, the model represents:

- a distribution over latent cell states;
- mixture mass for coarse states or learned components;
- optional relational geometry;
- condition descriptors: developmental time or perturbed gene.

## Three transition operators

### Development operator

A time-conditioned unbalanced transport flow evolves both state locations and mixture mass. A discrete branch variable supports differentiation. Training combines an OT-derived conditional target with distribution matching and reconstruction.

### Morphogenesis operator

A fused relational coupling proposes cross-stage correspondences. Global scale is predicted separately. A sparse equivariant graph field produces local deformations and updates expression-neighborhood context.

### Perturbation operator

A gene descriptor is built from signed regulatory neighborhoods, protein/pathway features and optional pretrained embeddings. It parameterizes a state-dependent response field with strong shrinkage toward zero.

## Loss design

The training objective should mirror questions, not copy raw metric weights across incompatible scales:

- pseudobulk direction and ranked change;
- multiscale distribution matching in a fixed representation;
- gene-pair dependence or variogram preservation;
- relational shape, scale and neighborhood-expression consistency for T2;
- sparse signed delta and magnitude calibration for T3;
- reconstruction and regularization.

Loss weights are selected on released-stage pseudo-holdouts. The official scorer remains the source of truth, while a local proxy is only a model-selection instrument.

## What is genuinely shared

The encoder, missing-gene treatment, gene-module priors, stochastic population decoder and experiment interface are shared. The transition operators are structurally related conditional fields but have different inputs and inductive biases. This boundary is scientifically meaningful and can be tested by freezing or sharing each component.

## Falsification criteria

Abandon or simplify the proposal if:

- unbalanced transport does not improve state coverage over a composition-aware low-rank baseline;
- the T2 equivariant head improves normalized shape but harms physical scale or local expression organization;
- T3 graph conditioning fails to beat a signed linear propagation baseline in gene-disjoint external validation;
- foundation embeddings do not improve matched-head controls across seeds;
- shared training causes negative transfer on any task without a compensating multi-task benefit.

The likely winning system may be an ensemble of simpler task-specific models. A unified architecture is valuable only if the data support it.
