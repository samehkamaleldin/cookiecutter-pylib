# {{cookiecutter.project_slug}}
{{cookiecutter.project_short_description}}

![ci workflow](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/ci.yml/badge.svg)
![black](https://img.shields.io/badge/code%20style-black-000000.svg)
![license](https://img.shields.io/badge/license-{{cookiecutter.open_source_license}}-blue)

## Usage
To use {{ cookiecutter.project_name }} in a project:
``` python
import {{ cookiecutter.project_slug }}
```

## Installation
Install from source using poetry as follows:
``` sh
poetry install
```

## Building documentation
To build documentation using `sphinx`, run the following commands inside the `docs` directory:
``` sh
make html
```

## License
{{ cookiecutter.project_name }} is licensed under the {{ cookiecutter.open_source_license }} license.
