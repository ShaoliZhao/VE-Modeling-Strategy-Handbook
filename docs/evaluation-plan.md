# Evaluation plan

## Baseline ladder

| Stage | T1 | T2 | T3 |
|---|---|---|---|
| floor | copy last stage | copy last expression and geometry | matched WT identity |
| statistical | shrinkage trend + joint residuals | composition-aware interpolation + relational geometry | signed network propagation + shrinkage |
| distributional | unbalanced OT | fused GW / stochastic OT | CellOT on observed source response |
| deep | branching temporal flow | equivariant deformation field | graph-conditioned adapter |
| pretrained | frozen FM encoder with matched head | frozen FM + spatial head | compliant perturbation pretraining + small adapter |

## Honest pseudo-holdouts

T1 cannot reproduce E12.5-like long extrapolation from only two official stages. E8.5→E9.5 is a limited proxy. Stronger validation requires a compliant external time series with entire stages and embryos held out.

T2 can construct interpolation proxies from released ladders, such as predicting an internal released stage from its neighbors. Keep heart/embryo and interpolation/extrapolation reports separate.

T3 cannot validate unseen-gene generalization by splitting Mab21l2 cells. Use external perturbation data with entire genes held out, and separately hold out cell context or dataset. Report when a method has only same-gene reproducibility evidence.

## Required ablations

- distribution mean versus full cell population;
- fixed versus predicted composition;
- independent versus joint residual sampling;
- balanced versus unbalanced transport;
- deterministic versus stochastic coupling;
- T2 scale-only, shape-only and joint models;
- spatial expression shuffled across fixed coordinates;
- T3 signed, unsigned and randomized graphs;
- PCA, autoencoder, frozen foundation model and adapter with identical heads;
- shared versus task-specific encoder and decoder.

## Uncertainty and replication

Use biological embryos as the resampling unit whenever replicates exist. Cell bootstrap from one embryo measures sampling noise, not cross-embryo generalization. Report at least three training seeds for stochastic models and separate model-seed variance from scorer subsampling variance.

## Decision rules

Promote a component only if it improves the scoring group it targets, does not create a material regression elsewhere, and survives a relevant pseudo-holdout and seed analysis. Remove components that add compute without stable evidence. Never infer hidden target properties by algebraically probing leaderboard scores.
