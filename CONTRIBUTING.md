# Contributing

Additions should improve scientific decision-making rather than increase list length. A model entry needs a primary paper or official implementation, a clear task connection, assumptions and at least one failure mode. Preprints must remain labelled as preprints.

Do not add leaderboard claims without a public reproducible source, or describe results from another biological setting as Virtual Embryo validation.

Run:

```bash
python3 scripts/validate_repository.py
python3 -m unittest discover -s tests -v
```
