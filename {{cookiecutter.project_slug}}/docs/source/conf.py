import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath("../../src"))
import {{ cookiecutter.project_slug }}

# -- Project information -----------------------------------------------------

project = "{{ cookiecutter.project_slug }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.user_full_name }}"
author = "{{ cookiecutter.user_full_name }}"
release = {{ cookiecutter.project_slug }}.__version__

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

# Add any paths that contain templates here, relative to this directory.
master_doc = "index"
templates_path = ["_templates"]
exclude_patterns = []

modindex_common_prefix = ["{{cookiecutter.project_slug}}."]
# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_sourcelink = False
html_show_sphinx = False
