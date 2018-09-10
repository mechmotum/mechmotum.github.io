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
else:
    THEME = config_data['THEME_PATH']
# svbhack settings
# https://github.com/gfidente/pelican-svbhack/
#GOOGLE_ANALYTICS = ''
USER_LOGO_URL = 'https://objects-us-east-1.dream.io/mechmotum.github.io/bear-bicycle-480x480.png'
#DISQUS_SITENAME = ''
TAGLINE = 'E pur si muove'
