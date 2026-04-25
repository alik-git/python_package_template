# AGENTS.md

Repo-specific guidance for agents working in this Python package template.

If this file conflicts with the code or repo docs, trust the code and docs,
then update `AGENTS.md`.

When unsure, ask a short question or make the smallest reversible change. Do
not invent local workflow assumptions.

## Start Here

- Read `README.md` first.
- Treat `pyproject.toml` as the source of truth for package metadata,
  dependencies, scripts, and tool configuration.
- Keep this repository generic. Do not add project-specific assumptions unless
  the user asks for them.

## Package Structure

- Reusable package logic lives under `src/mypackage/`.
- Public imports should be exposed intentionally from `src/mypackage/__init__.py`.
- CLI behavior belongs in `src/mypackage/cli.py`.
- Do not configure global logging in import-time library code. Configure it at
  the CLI or application boundary.
- Keep `src/mypackage/py.typed` so downstream type checkers recognize the
  installed package as typed.

## Development Workflows

- `uv` is the preferred fast local workflow:
  `uv sync --extra dev`.
- Keep `.python-version` aligned with `requires-python` and CI.
- Standard Python tooling must keep working:
  `python -m pip install -e ".[dev]"`.
- Conda may be used to create the outer Python environment, but package
  dependencies should still come from `pyproject.toml`.

## Validation

- Run the smallest relevant checks for the files you changed.
- For normal code changes, prefer:
  - `python -m ruff format --check .`
  - `python -m ruff check .`
  - `python -m mypy`
  - `python -m pytest`
- For packaging changes, also run:
  - `python -m build`
  - install the built wheel in a clean environment when practical
- For hygiene changes, run:
  - `python -m pre_commit run --all-files --show-diff-on-failure`

## PRs And Local Files

- Use `.github/PULL_REQUEST_TEMPLATE.md` for PR descriptions.
- Do not commit secrets, credentials, local runtime config, or scratch notes.
- Do not install local pre-commit hooks unless the user asks.
- `AGENTS.md` is tracked and should stay current.
