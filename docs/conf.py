# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
os.environ['BASE_URL'] = 'https://api.flightradar24.com/api/v1'
os.environ['FLIGHT_RADAR_KEY'] = 'dummy_key'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FlightRadar24 Python SDK'
copyright = '2025, Amir Muminovic'
author = 'Amir Muminovic'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton',
    'sphinxcontrib.autodoc_pydantic',
]

autosummary_generate = True
autodoc_typehints = 'description'

autodoc_pydantic_model_show_json = True
autodoc_pydantic_settings_show_json = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
