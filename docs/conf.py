# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
if os.getenv('SPELLCHECK'):
    extensions += 'sphinxcontrib.spelling',
    spelling_show_suggestions = True
    spelling_lang = 'en_US'

source_suffix = '.rst'
master_doc = 'index'
project = 'knitlib'
year = '2015'
author = 'Sebastian Oliva'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.0.1'

#import sphinx_py3doc_enhanced_theme
#html_theme = "sphinx_py3doc_enhanced_theme"
#html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

pygments_style = 'trac'
templates_path = ['.']
html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = True
html_sidebars = {
   '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme_options = {
        'githuburl': 'https://github.com/fashiontec/knitlib/'
    }
