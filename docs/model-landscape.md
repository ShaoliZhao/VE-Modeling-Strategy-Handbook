# Model landscape

Priority labels are recommendations for an experimental sequence: **A** first-line, **B** conditional extension, **C** research option. They are not published competition rankings.

## Statistical and probabilistic models

| Model family | T1 | T2 | T3 | Useful role | Main failure mode |
|---|---:|---:|---:|---|---|
| shrinkage pseudobulk and low-rank regression | A | A | A | strong low-data baseline; decomposes mean and residual changes | cannot create unsupported branches or unseen gene effects |
| hierarchical mixture/compositional model | A | A | B | separates state proportions from within-state expression | annotation drift and dissection differences can mimic biology |
| Gaussian process or spline trend | C | B | C | smooth interpolation with uncertainty | two T1 stages cannot identify flexible curvature |
| balanced optimal transport | B | A | B | aligns unpaired populations | forces mass conservation and does not itself forecast |
| unbalanced optimal transport | A | A | B | permits appearing/disappearing population mass | inferred mass change is not automatically proliferation |
| fused Gromov-Wasserstein transport | C | A | C | combines expression with within-sample geometry | coupling still needs a generative coordinate reconstruction |
| signed network propagation / linear response | C | C | A | interpretable unseen-gene perturbation direction | networks are incomplete and often lack context or sign |

## Deep generative models

| Model family | Best fit | Why it may help | What must be changed for this challenge |
|---|---|---|---|
| VAE + neural ODE (scNODE) | T1 | continuous latent-time generation | add non-autonomous time conditioning, composition dynamics and branch support |
| dynamic OT flow (TrajectoryNet, MIOFlow) | T1/T2 | learns population dynamics from snapshots | test extrapolation separately; avoid treating an inferred path as ground truth |
| entropic OT flow matching (GENOT) | T1/T2 | stochastic one-to-many transport and cross-space matching | add developmental conditioning, mass change and task decoder |
| conditional diffusion / Schrödinger bridge | T1/T2 | expressive multimodal distributions | data demand and endpoint dependence make long extrapolation risky |
| E(n)/SE(3)-equivariant graph network | T2 | local 3D interactions without a shared global frame | use sparse local graphs; handle scale and handedness explicitly |
| CellOT | T3 source response | distributional WT-to-perturbation map | a map for Mab21l2 does not identify Gata4 or β-catenin effects |
| GEARS | T3 | gene graph provides an unseen-perturbation descriptor | needs richer external perturbation supervision than the official single KO |
| CPA/scGen | T3 baseline | compact context/perturbation factorization | a learned embedding for one intervention cannot span unseen genes alone |
| State-style transition model | T3 | cross-context perturbation pretraining | species, tissue, gene panel and source leakage require direct validation |

## Foundation models and LLMs

Geneformer, scGPT, scFoundation and UCE can provide gene or cell embeddings. The defensible experiment is a frozen encoder or small adapter feeding the same population model used by PCA and a standard autoencoder. Compare matched downstream heads, trainable parameter counts and compute budgets.

Potential benefits are better gene relationships, transfer across datasets and more stable low-data representations. Major risks are human-to-mouse transfer, incomplete gene vocabularies, treating unmeasured MERFISH genes as zero, opaque pretraining sources and observational embeddings that do not encode causal responses.

General text LLMs are appropriate for literature retrieval, evidence extraction, code generation and autonomous experiment orchestration. They should not directly invent numerical cell populations or unsigned regulatory edges. Every extracted biological claim needs a source and evidence type.

## Evidence that changes the priority order

Recent studies report that deep perturbation predictors do not consistently outperform simple linear baselines and that evaluation can reward systematic variation rather than perturbation-specific prediction. This does not rule out deep models; it makes strong baselines and gene-disjoint evaluation mandatory. See `P17`, `P18` and `P24` in the paper catalog.
