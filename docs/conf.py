# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import logging
import os.path
import re
import subprocess


logger = logging.getLogger('rtd-samples')


def get_git_branch():
    """Get the git branch this repository is currently on"""
    path_to_here = os.path.abspath(os.path.dirname(__file__))

    # Invoke git to get the current branch which we use to get the theme
    try:
        p = subprocess.Popen(['git', 'branch'], stdout=subprocess.PIPE, cwd=path_to_here)

        # This will contain something like "* (HEAD detached at origin/MYBRANCH)"
        # or something like "* MYBRANCH"
        branch_output = p.communicate()[0]

        # This is if git is in a normal branch state
        match = re.search(r'\* (?P<branch_name>[^\(\)\n ]+)', branch_output)
        if match:
            return match.groupdict()['branch_name']

        # git is in a detached HEAD state
        match = re.search(r'\(HEAD detached at origin/(?P<branch_name>[^\)]+)\)', branch_output)
        if match:
            return match.groupdict()['branch_name']
    except Exception:
        logger.exception(u'Could not get the branch')

    # Couldn't figure out the branch probably due to an error
    return None


# -- Project information -----------------------------------------------------

project = u'Argo API - Doc'
copyright = u'2020, Gabriel Bustamante'
author = u'Gabriel Bustamante'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u''


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# Maps git branches to Sphinx themes
default_html_theme = 'sphinx_rtd_theme'
branch_to_theme_mapping = {
    # 3rd party themes
    'master': default_html_theme,

    # Sphinx built-in themes
    'alabaster': 'alabaster',
    'classic': 'classic',
    'sphinxdoc': 'sphinxdoc',
    'scrolls': 'scrolls',
    'agogo': 'agogo',
    'traditional': 'traditional',
    'nature': 'nature',
    'haiku': 'haiku',
    'pyramid': 'pyramid',
    'bizstyle': 'bizstyle',
}
current_branch = get_git_branch()

if current_branch:
    sphinx_html_theme = branch_to_theme_mapping.get(current_branch, default_html_theme)
    print(u'Got theme {} from branch {}'.format(sphinx_html_theme, current_branch))
else:
    sphinx_html_theme = default_html_theme
    print(u'Error getting current branch - using default theme')

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = sphinx_html_theme

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'RTDSphinxThemeSampledoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RTDSphinxThemeSample.tex', project,
     u'Read the Docs, Inc \\& contributors', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'rtdsphinxthemesample', project,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RTDSphinxThemeSample', project,
     author, 'RTDSphinxThemeSample', 'One line description of project.',
     'Miscellaneous'),
]
