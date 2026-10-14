"""Static repository validation for the lung-cancer notebook."""
from __future__ import annotations

import ast
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
NOTEBOOK = REPO_ROOT / "Lung Cancer.ipynb"
FORBIDDEN_PATH_MARKERS = ("/home/", "/content/", "\\users\\", "j:\\", "e:\\")


def validate_notebook(path: Path = NOTEBOOK) -> list[str]:
    errors: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"Notebook not found: {path}"]
    except json.JSONDecodeError as exc:
        return [f"Invalid notebook JSON: {exc}"]

    if not isinstance(notebook.get("cells"), list):
        return ["Notebook does not contain a cells list"]

    for index, cell in enumerate(notebook["cells"]):
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "code":
            try:
                ast.parse(source, filename=f"{path.name}:cell-{index}")
            except SyntaxError as exc:
                errors.append(f"Cell {index} has syntax error: {exc}")
        if cell.get("outputs"):
            errors.append(f"Cell {index} contains stale outputs")
        if cell.get("execution_count") is not None:
            errors.append(f"Cell {index} contains a stale execution count")
        lowered = source.lower()
        for marker in FORBIDDEN_PATH_MARKERS:
            if marker in lowered:
                errors.append(f"Cell {index} contains a local absolute path marker: {marker}")

    all_source = "\n".join("".join(c.get("source", [])) for c in notebook["cells"])
    if "FileNotFoundError" not in all_source or "LUNG_CANCER_DATA" not in all_source:
        errors.append("Notebook is missing the explicit data-missing guard")
    return errors


def main() -> int:
    errors = validate_notebook()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Validated {NOTEBOOK.name}: syntax, clean outputs, and path guard OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
