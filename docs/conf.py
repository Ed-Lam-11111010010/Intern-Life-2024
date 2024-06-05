# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

project = "Edwin's Intern Life"
copyright = '2024, edwinlamc'
author = 'edwinlamc'
release = '2024'

# The full version, including alpha/beta/rc tags
release = '1.0'

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

extensions = [
    'sphinx_markdown_tables',
    'recommonmark'
]

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
html_logo = 'logo.png'
html_theme_options ={'logo_only': True,'display_version': False}
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']