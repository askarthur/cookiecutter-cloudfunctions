"""Module to cleanup generate repository post generation."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove file at given filepath."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    # AUTHORS
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")

    # LICENSE
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE")

    # GitHub Actions
    if "{{ cookiecutter.use_github_actions_for_ci }}" != "y":
        remove_file(".github/workflows/code_quality_checks.yml")

    # CI Checks
    if "{{ cookiecutter.use_flake8 }}" != "y":
        remove_file(".flake8")

    if "{{ cookiecutter.use_mypy }}" != "y":
        remove_file("mypy.ini")

    if "{{ cookiecutter.use_yamllint }}" != "y":
        remove_file("yamllint-config.yml")
