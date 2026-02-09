# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'The Whiznium Knowledge Base'
copyright = '2026, MPSI Technologies GmbH'
author = 'Alexander Wirthmueller'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
										'KB2.md', 'KB4.md', 'KB5.md', 'KB9.md',
										'KB10.md', 'KB11.md', 'KB12.md', 'KB13.md', 'KB14.md', 'KB15.md', 'KB16.md', 'KB17.md', 'KB18.md', 'KB19.md',
										'KB20.md', 'KB21.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {"collapse_navigation": False}
html_static_path = ['_static']
