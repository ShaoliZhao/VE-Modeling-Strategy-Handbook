import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_repository.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(VALIDATOR)


class RepositoryTests(unittest.TestCase):
    def test_repository_is_internally_consistent(self):
        self.assertEqual(VALIDATOR.validate(), [])

    def test_catalog_has_task_coverage(self):
        import csv
        with (ROOT / "references" / "papers.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        for task in ("T1", "T2", "T3"):
            self.assertGreaterEqual(sum(task in row["primary_tasks"].split("|") for row in rows), 5)


if __name__ == "__main__":
    unittest.main()
