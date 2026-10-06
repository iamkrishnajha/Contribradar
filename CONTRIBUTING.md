# Contributing to ContribRadar

Thank you for your interest in contributing to ContribRadar!

ContribRadar is an open-source project focused on helping developers discover meaningful opportunities to improve software projects.

## Before contributing

Please:

1. Read the README.
2. Search existing issues before opening a new one.
3. For larger changes, open an issue first to discuss the idea.
4. Keep pull requests focused on one clear improvement.
5. Add or update tests when changing behavior.
6. Update documentation when necessary.

## Development setup

Clone the repository and install it locally:

```bash
python -m pip install -e .
python -m pip install pytest
pytest -q
contribradar scan .
contribradar scan . --json
