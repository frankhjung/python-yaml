# Example Python 3 Project - Processing YAML

Simple [Python 3](https://docs.python.org/3/) example project.

## uv Quick Start

To get started with this project locally, you can use [uv](https://docs.astral.sh/uv/) to manage dependencies and virtual environments.

### Install uv

Install `uv` if you haven't already:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*(For other installation methods, refer to the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/).)*

### Sync the project dependencies

Sync the project dependencies:

```bash
uv sync
```

This will automatically create a virtual environment (`.venv`) and install all necessary dependencies defined in [pyproject.toml](pyproject.toml).

### Run commands within the environment

Run commands within the environment using `uv run`:

```bash
uv run make test
```

## Updating Outdated Packages

To check for and update packages to their latest compatible versions according to [pyproject.toml](pyproject.toml), run:

```bash
uv lock --upgrade
```

If you want to update a specific package, use:

```bash
uv lock --upgrade-package <package_name>
```

After updating the lockfile, sync the environment:

```bash
uv sync
```

## Documentation

* [Package reStructuredText](README.rst)
* [GitHub Pages](https://frankhjung.github.io/python-yaml/index.html)
* [GitLab pages](https://docs.gitlab.com/ce/user/project/pages/getting_started_part_one.html)

## Pipelines

* [GitHub](https://frankhjung.github.io/python-yaml/index.html)
* [GitLab](https://gitlab.com/theMarloGroup/training/students/fjung/python-yaml/pipelines)
