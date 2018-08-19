#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ian Rose'
SITENAME = u'Blueschisting'
SITESUBTITLE = u'Thoughts on planetary science, fluid dynamics, transit, and scientific computing'
SITEURL=''
PROFILE_IMAGE_URL='/images/escape_of_the_core.png'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'
ARTICLE_PATHS=['articles']
STATIC_PATHS=[
        'data',
        'interactive_earth',
        'articles/coding/images',
        'articles/dimensional_analysis/images',
        'articles/transit/images',
        'images',
        'agu_2015_talk',
        'visualization'
        ]
READERS = {'html':None }
MARKUP = ('md', 'ipynb')
IGNORE_FILES=['*ipynb_checkpoints*']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_ORDER_BY = 'reversed-date'


DEFAULT_PAGINATION = 10
INDEX_SAVE_AS = '/blog_index.html'
MENUITEMS=[
           ('Ian Rose', '/pages/about.html'),
           ('blog', '/blog_index.html')
          ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME='pelican-blueschisting'
PLUGIN_PATHS=['pelican-plugins',]
PLUGINS = ['summary', \
           'render_math',\
           'pelican-ipynb.markup',\
           'autopages',
           'liquid_tags']
CATEGORY_PAGE_PATH = PATH + '/categories'
IPYNB_USE_META_SUMMARY = True

GITHUB_ADDRESS = 'http://github.com/ian-r-rose'
TWITTER_ADDRESS = 'http://twitter.com/IanRRose'
