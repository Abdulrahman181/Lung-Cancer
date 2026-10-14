import json
import unittest
from pathlib import Path

from validate_repo import NOTEBOOK, validate_notebook


class RepositoryValidationTests(unittest.TestCase):
    def test_notebook_passes_static_validation(self):
        self.assertEqual(validate_notebook(NOTEBOOK), [])

    def test_notebook_has_no_outputs_or_execution_counts(self):
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
        for cell in notebook["cells"]:
            self.assertFalse(cell.get("outputs"), "Notebook outputs must stay clean")
            self.assertIsNone(cell.get("execution_count"))

    def test_required_project_files_exist(self):
        root = Path(__file__).resolve().parents[1]
        for name in ("README.md", "requirements.txt", ".gitignore"):
            self.assertTrue((root / name).is_file(), name)


if __name__ == "__main__":
    unittest.main()
