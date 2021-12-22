# Feature Explanation

## Pytest
Pytest is the package used for unit and coverage testing within the cookiecutter. We've chosen it over `unittest` as we find it easier to use and understand the results of. In addition, we like the native fixture functionality of pytest and the `pytest-cov` extension (used for coverage testing).

## Flake8 and Pylint
Flake8 and Pylint are both linters developed by the Python Code Quality Authority ([PyCQA](https://github.com/PyCQA)). As pylint is typically more exhaustive we typically only use it for less fault-tolerant code. If you want a more relaxed linter (as we typically use with our repos), use flake8 to get good linting with slightly faster development speed. 

## Black
Black is my go-to code formatter. Although annoying in the beginning, we've grown to love black as it makes git diffs 100x easier. With strict and opionated formatting, it does all the tedious formatting you're too lazy to do and leaves your pull requests with only the important changes being highlighted.

## Mypy
Mypy is the official checker for type-hinting which was added in Python 3.6. we think type-hinting allows for way better readability of Python code. Additionally, it makes sure that variables being passed throughout your program are being correctly accounted for in terms of their type (passing a string of "1" when it should be 1 can cause issues down the line).

## Poetry
Poetry is the dependency manager and packager for the cookiecutter. As we've grown frusturated with older tools for Python packaging (setuptools, tox, etc.) we decided to give Poetry a try and it was 100% worth it. It comprises all the necessary settings into a single `pyproject.toml` file (instead of `setup.py/cfg`, `requirements.txt`, `MANIFEST.in`, etc.) which has growing use by the above packages (with pylint, pytest, and black already supporting). Poetry is one of the main reasons the CI files are short and sweet and the repository is not overrun with packaging files.

## Github Actions
GitHub Actions is still pretty new to the CI space and is probably the biggest split (with Poetry) we use from most Python repositories. The main reason for using GitHub Actions is it's free (up to 2,000/minutes a month) and it's where my code exists. A lot of open-source projects use TravisCI or other services which we think adds complexity to developing and maintaining a project.

## Development process
Although this isn't a *feature* per-se, we think it's important to address as it's how we built the cookiecutter structure. The main drive behind having the CI checks on the `main` and `development` branches is so these are typically "protected" from having bad code.
