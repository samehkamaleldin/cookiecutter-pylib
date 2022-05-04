======================
CookieCutter PyLib
======================

`cookiecutter` template for a Python package.

* GitHub repo: https://github.com/samehkamaleldin/cookiecutter-pylib/
* Free software: BSD license

Features
--------

* Project setup/packaging is handled with ``poetry`` and ``pyproject.toml`` file.
* Testing setup with ``tox`` and ``pytest/coverage`` and Linting with ``flake8``.
* Github Actions workflow for CI is ready on push and pull request.
* Github templates for issue and PR are ready.
* ``tox`` testing: Setup to easily test for Python 3.6, 3.7, 3.8
* ``Sphinx`` docs: Documentation ready for generation with ``read_the_docs`` theme.

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/samehkamaleldin/cookiecutter-pylib.git

When the project creation project is finished, you can now move to the project directorry and do the following:

* Update the conda environment configuration ``env.yml`` and initialize it. (``conda env create -f env.yml``)
* Configure and install requirements as from the ``project.toml`` file with poetry. (``poetry install``)
