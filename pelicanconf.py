#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Rose'
SITENAME = u'Geomusings'
SITESUBTITLE = u'Thoughts on planetary science, fluid dynamics, and scientific computing'
SITEURL='ian-r-rose.github.io'
PROFILE_IMAGE_URL='/images/ian_rose.jpg'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'


DEFAULT_LANG = u'en'
STATIC_PATHS=['interactive_earth', 'images']
READERS = {'html':None }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = 10

MENUITEMS=[('blog', '/'), ('interactive earth', '/interactive_earth/index.html')]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='pelican-crowsfoot'
#THEME='pelican-octopress-theme'
PLUGIN_PATHS=['pelican-plugins',]
PLUGINS = ['summary', \
           'liquid_tags.img',\
           'liquid_tags.include_code', \
           'liquid_tags.notebook',\
           'liquid_tags.literal']

GITHUB_ADDRESS = 'http://github.com/ian-r-rose'
TWITTER_ADDRESS = 'http://twitter.com/IanRRose'
