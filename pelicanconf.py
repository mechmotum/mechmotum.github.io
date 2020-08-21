#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import yaml

LABNAME = 'Laboratorium of Marvelous Mechanical Motum'

# TODO : Theme puts the author's name below the logo, should put sitename (i.e.
# it assumes this is a blog).
AUTHOR = LABNAME
SITENAME = LABNAME
SITEURL = ''
SOURCEURL = 'https://github.com/mechmotum/mechmotum.github.io'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# This sets the default pages to be top level items and articles to be under
# /blog/.
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'
MENUITEMS = [('Blog', '/blog/')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

try:
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ''
else:
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = config_data['PLUGIN_PATHS']

## THEME

# Alchemy theme settings
SITESUBTITLE = 'E pur si muove'
SITEIMAGE = 'https://objects-us-east-1.dream.io/mechmotum.github.io/bear-bicycle-480x480.png'
DESCRIPTION = ''
# pelican-alchemy removed the original theme.css, so bring it back.
THEME_CSS_OVERRIDES = ['theme/css/origtheme.css']

#GOOGLE_ANALYTICS = ''
#DISQUS_SITENAME = ''

## PLUGINS

PLUGINS = ['render_math', 'extract_toc']
