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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Mech-Mind User Guide'
copyright = '2020, Mech-Mind'
author = 'Mech-Mind'
version = '1.0'

language = 'en_GB'
locale_dirs = ['../translated/']
gettext_uuid = True
gettext_compact = False     # to generate .pot files



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'

html_logo = '_static/mech-mind-logo.png'


# -- Options for LaTeX output --------------------------------------------------

latex_elements={
    'preamble': '''
    \\hypersetup{unicode=true}
    \\usepackage{CJKutf8}
    \\AtBeginDocument{\\begin{CJK}{UTF8}{gbsn}}
    \\AtEndDocument{\\end{CJK}}
    ''',
}

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Mech-Mind User Manual', 'Mech-Mind docs Documentation',
     [author], 1)
]

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Mech-Mind User Manual', 'Mech-Mind docs Documentation',
     author, 'index', 'Mech-Mind User Manual Project.',
     'User Manual'),
]

def setup(app):
    app.add_css_file('css/custom.css')