# Task strategies

## T1: branching population extrapolation

Start with a decomposition rather than a monolithic flow:

1. encode cells in a low-rank expression and gene-module space;
2. model state composition separately from within-state expression;
3. estimate the E8.5→E9.5 transition with unbalanced OT;
4. fit a time-conditioned stochastic flow to the conditional transport distribution;
5. decode complete cells with joint residual sampling.

The key extension is a branch variable or mixture component that allows one source region to produce several descendant modes. A non-autonomous field `f(z, t, branch, context)` is preferable to an autonomous ODE because developmental speed and direction need not stay constant. However, the single observed interval means branch creation must be constrained by compliant external developmental data or explicit lineage priors.

The primary ablations are fixed versus predicted composition, balanced versus unbalanced transport, autonomous versus time-conditioned dynamics, and joint versus gene-independent residuals.

## T2: relational interpolation and morphogenetic extrapolation

Treat interpolation and extrapolation as separate regimes.

For whole-embryo interpolation, estimate a fused expression/geometry coupling between bracketing stages. Geometry should use within-embryo relations rather than raw coordinates. Generate the intermediate state from the stochastic coupling, then reconstruct coordinates through an aligned deformation or relational embedding. A deterministic OT barycenter may over-smooth cell states and tissue boundaries, so retain conditional variance.

For heart extrapolation, decompose coordinates into center, physical scale and normalized shape. Fit scale with a low-capacity trend, then model normalized local deformation using an SE(3)-equivariant neighborhood network conditioned on expression and time. This makes it possible to learn local organization without assuming a common imaging frame.

Evaluate expression, shape, scale and expression-position coupling independently. A plausible point cloud with shuffled expression should fail the local-organization diagnostic.

## T3: gene-conditioned signed response

Predict the perturbation delta, then add it to matched wild type:

`x_KO = nonnegative(x_WT + a(cell_state, stage) * delta_graph(gene) + residual_adapter)`

`delta_graph` comes from finite-depth propagation through a signed, typed and context-weighted regulatory graph. TF-target, signaling and protein-interaction edges should remain distinct. GO similarity and physical interaction do not supply activation/repression signs by themselves.

Use the observed Mab21l2 knockout to calibrate response scale, noise and context dependence, rather than copying its gene delta to the held-out target. Pretrain the gene-conditioned adapter only on external perturbation data that pass the competition's genotype and stage rules. Preserve the matched WT expression-coordinate pairs in the first version because T3 geometry is a required output but is not a ranked shape question.

Critical ablations are signed versus unsigned graph, target-gene features versus a generic KO token, graph-only versus residual adapter, and cell-state-specific versus global response.

## Recommended order of work

1. Reproduce the official floor and a shrinkage/low-rank baseline.
2. Build task-specific statistical models and diagnose which scoring group remains weak.
3. Add one deep component that targets that failure.
4. Add foundation-model representations only after the same downstream model works with PCA/AE.
5. Share parameters across tasks only when an ablation shows transfer rather than negative interference.
