"""Sphinx configuration file for the Flask Boilerplate documentation.

This file contains the configuration settings for generating the project's documentation
using Sphinx. It defines the project metadata, theme, extensions, and other settings
required to build the documentation.

For more information on Sphinx configuration, see:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import os
import sys
from datetime import datetime

# Add the project's root directory to the Python path
sys.path.insert(0, os.path.abspath("../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Flask Boilerplate"
author = "Cedric Grun"
copyright = f"{datetime.now().year}, {author}"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Add Sphinx extensions
extensions = [
    "sphinx.ext.autodoc",  # Automatically generate documentation from docstrings
    "sphinx.ext.napoleon",  # Support for Google-style and NumPy-style docstrings
    "sphinx.ext.viewcode",  # Add links to the source code
    "sphinx.ext.coverage",  # Check documentation coverage
    "sphinx.ext.githubpages",  # Publish documentation to GitHub Pages
    "sphinx_rtd_theme",
    "sphinx_autodoc_typehints",
]

# Add paths to templates
templates_path = ["_templates"]

# List of file patterns to exclude from documentation
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Use the RTD (Read the Docs) theme
html_theme = "sphinx_rtd_theme"

# Add paths to static files
html_static_path = ["_static"]

# Customize the sidebar
html_sidebars = {
    "**": [
        "globaltoc.html",
        "relations.html",
        "sourcelink.html",
        "searchbox.html",
    ]
}
# -- Extension configuration -------------------------------------------------

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}

# Napoleon settings (for Google/NumPy docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# Coverage settings
coverage_show_missing_items = True
