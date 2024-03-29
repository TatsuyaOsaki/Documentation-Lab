# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Tatsuya Osaki'
copyright = '2022, Tatsuya Osaki'
author = 'Tatsuya Osaki'

# The full version, including alpha/beta/rc tags
release = '2.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx_favicon",
    "sphinx_markdown_tables",
    "sphinx_design",
]
myst_enable_extensions = ["colon_fence"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['sphinx.ext.githubpages']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'furo'
html_theme = "pydata_sphinx_theme"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []
# html_static_path = ['docs/_static']


html_logo = "./picture/logo_documentation.png"
html_theme_options = {
    "logo": {
        "text": "Tatsuya Osaki",
    },
    "show_toc_level": 2,
    
    
    "icon_links": [
        {
            "name": "PyData",
            "url": "https://pydata.org",
            "icon": "https://pydata-sphinx-theme.readthedocs.io/en/stable/_static/pydata-logo.png",
            "type": "url",
            # Add additional attributes to the href link.
            # The defaults of target, rel, class, title and href may be overwritten.
            "attributes": {
                "target" : "_blank",
                "rel" : "noopener me",
                "class": "nav-link custom-fancy-css"
            }
        },
        
        {
        "name": "GitHub",
        "url": "https://github.com/TatsuyaOsaki/Documentation-Lab",  # required
        "icon": "fa-brands fa-square-github",
        # The type of image to be used (see below for details)
        "type": "fontawesome",
    }  
        
    ],
    
}
favicons = [
    "favicon-16x16.png",
    "favicon-32x32.png",
]

html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"]
}