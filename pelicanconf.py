#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lee Johnson'
SITENAME = 'Tech Journal'
SITESUBTITLE = u'Journal on automation technology and beyond'
SITEURL = ''
#SITEURL = 'http://localhost:8000'

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ["md", "ipynb"]
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'render_math',
    'liquid_tags',
    # auto-summarizing articles
    'summary'
    # use summaries for RSS, not full articles
    'feed_summary',
    # 'nb_markup',
    # 'ipynb.liquid',
]
IGNORE_FILES = ['.ipynb_checkpoints']

LIQUID_TAGS = ["img", "literal", "video", "youtube", "vimeo", "include_code", "notebook"]

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'
# EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'lj020326'
GITHUB_USERNAME = 'lj020326'
LINKEDIN_USERNAME = 'leejjohnson'
STACKOVERFLOW_ADDRESS = 'https://stackexchange.com/users/3319937/purplemouse'
AUTHOR_WEBSITE = 'https://dettonville.org'
AUTHOR_BLOG = 'http://leeblog.org'
AUTHOR_CV = "http://leeblog.org/downloads/docs/CV.pdf"
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds
FEED_USE_SUMMARY = True

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

# Footer info

LICENSE_URL = "https://github.com/lj020326/leeblog.org/blob/master/LICENSE"
LICENSE = "MIT"

## ref: https://github.com/pelican-plugins/liquid-tags
from io import open
EXTRA_HEADER = open('_nb_header.html', encoding='utf-8').read()