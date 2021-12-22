# Cookiecutter Google Function

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Google Function python project. Powered by Poetry, GitHub actions, and Google Cloud Platform.

## Introduction
Welcome to cookiecutter-cloudfunctions! This project was created because we wanted an easy-to-configure template for using Google Functions. In the current state, there aren't any cookiecutters focusing on deploying a Google Function using GitHub Actions and Cloud Build for continuous integration and continuous deployment (CI/CD). We hope this will allow developers to create, test, and deploy their pipeline(s) in an easy-to-use and easy-to-maintain way. 

## File structure
All code should go in the directory with your given project-name. The packaging works with a single file of code or multiple modules nested within sub-directories. Currently, we don't have a public example of multi-file setup but we're working on it.

## Features
This template has the following features:  

  - [`pytest`](https://github.com/pytest-dev/pytest): Unit and coverage testing  
  - [`flake8`](https://github.com/PyCQA/flake8) and [`pylint`](https://github.com/PyCQA/pylint): Python style checks  
  - [`black`](https://github.com/psf/black): Auto-formatted code  
  - [`mypy`](https://github.com/python/mypy): Type checking  
  - [`Poetry`](https://github.com/python-poetry/poetry): Depedency management  
  - [`GitHub Actions`](https://github.com/features/actions): Automated CI checks

This is a simple list, for a deep-dive into why and how each feature is used visit [feature explanation](advanced/feature_explanation.md). If already familiar or not interested, continue to [Getting started](getting-started/create_local_project.md).
