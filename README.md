# Python Package Template

A minimal, modern Python package template for quickly starting an importable
package with a small CLI, logging, tests, type checking, packaging checks, and
GitHub Actions.

This repository is intentionally generic. Rename `mypackage`, update
`pyproject.toml`, choose a license only if the project should be published or
open sourced, and then start replacing the starter function with real code.

## Start A New Package

1. Rename the import package:

   ```bash
   mv src/mypackage src/your_package_name
   ```

2. Update the package metadata and tool settings in
   [`pyproject.toml`](pyproject.toml):

   - `name`
   - `description`
   - `authors`
   - `maintainers`
   - `keywords`
   - `classifiers`
   - `[project.urls]`
   - `[project.scripts]`
   - Ruff `known-first-party`
   - mypy `files`
   - references to `mypackage` throughout this README

3. Update imports in:

   - `src/your_package_name/__init__.py`
   - `src/your_package_name/cli.py`
   - `tests/test_package.py`

4. Add package code under `src/your_package_name/` and expose the intended
   public API from `src/your_package_name/__init__.py`.

5. Add a license if the package will be public or open source. The files under
   [`templates/licenses`](templates/licenses) are templates only and do not
   license this repository.

   ```bash
   cp templates/licenses/MIT LICENSE
   ```

   or:

   ```bash
   cp templates/licenses/Apache-2.0 LICENSE
   ```

   Then replace the copyright placeholder and add the matching `license` value
   in `pyproject.toml`, either `MIT` or `Apache-2.0`.

## Install For Development

Recommended with `uv`:

```bash
uv sync --extra dev
```

This repository commits `.python-version` and `uv.lock` so the uv workflow uses
Python 3.11 by default and resolves reproducible dependency versions. After
changing dependencies, update the lockfile with:

```bash
uv lock
```

Standard Python fallback:

```bash
python -m pip install -e ".[dev]"
```

Conda can still own the outer environment if needed:

```bash
conda create -n mypackage python=3.11
conda activate mypackage
python -m pip install -e ".[dev]"
```

## Run Checks

With `uv`:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy
uv run pytest
uv run pre-commit run --all-files
uv build
```

With standard Python tools:

```bash
python -m ruff format --check .
python -m ruff check .
python -m mypy
python -m pytest
python -m pre_commit run --all-files
python -m build
```

## Use The Package

Python API:

```python
import mypackage

result = mypackage.do_useful_thing("world")
```

CLI:

```bash
mypackage
```

## Layout

```text
src/mypackage/
  __init__.py   # public import surface
  package.py    # reusable package logic
  cli.py        # command-line boundary
  py.typed      # marker for typed packages

tests/
  test_package.py
```

## CI

GitHub Actions runs:

- fast Ruff-only checks
- Ruff, mypy, pre-commit hygiene, and pytest
- package build and wheel smoke test with pip
- package build and wheel smoke test with uv

Local pre-commit hooks are not installed automatically. Running
`pre-commit install` is optional.
