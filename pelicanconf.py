#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Ramon D. Iglesias'
SITENAME = u'Huevosabio'
SITEURL = ''

PATH = 'content'
PLUGIN_PATH = ["/home/ubuntu/pelican_plugins/pelican-plugins"]
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal','liquid_tags.youtube']

THEME = '/home/ubuntu/pelican_themes/pelican-octopress-theme'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/huevosabio'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
