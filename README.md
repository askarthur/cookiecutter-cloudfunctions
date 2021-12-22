# Cookiecutter Google Function

![Code Quality Checks](https://github.com/askarthur/cookiecutter-cloudfunctions/workflows/Code%20Quality%20Checks/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Google Function. Powered by Poetry, and GitHub actions.

## Quickstart
Install the latest Cookiecutter if you haven't installed it yet (this requires
`Cookiecutter 1.4.0` or higher):

`$ pip install -U cookiecutter>=1.4.0`

Generate a Python project:

`$ cookiecutter https://github.com/askarthur/cookiecutter-cloudfunctions.git`

## Features
This template has the following features:
  - [`pytest`](https://github.com/pytest-dev/pytest): Unit and coverage testing
  - [`flake8`](https://github.com/PyCQA/flake8) and [`pylint`](https://github.com/PyCQA/pylint): Python style checks
  - [`black`](https://github.com/psf/black): Auto-formatted code
  - [`mypy`](https://github.com/python/mypy): Type checking
  - [`Poetry`](https://github.com/python-poetry/poetry): Depedency managemnt and packaging
  - [`GitHub Actions`](https://github.com/features/actions): Automated CI checks, auto-release to PyPi, and automated version bumping (no more Travis needed)

## Documentation
For further documentation on how to create and connect to your repository as well as deploy to GCP, visit the official [docs](https://askarthur.github.io/cookiecutter-cloudfunctions/)
