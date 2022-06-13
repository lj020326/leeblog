#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lee Johnson'
SITENAME = 'Tech Journal'
SITESUBTITLE = u'Journal on automation technology and beyond'
SITEURL = ''
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

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ["md", "ipynb"]
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins', './plugins/pelican-plotly']
# PLUGIN_PATHS = ['./plugins', './pelican-plugins']
# PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',
    'liquid_tags',   # for notebooks
    'render_math',
    'pelican-plotly',
    'sitemap'
]
IGNORE_FILES = ['.ipynb_checkpoints']

LIQUID_TAGS = ["img", "literal", "video", "youtube", "vimeo", "include_code", "notebook"]

LIQUID_CONFIGS = (
("IGNORE_FILES", ".ipynb_checkpoints", ""),
("CODE_DIR", "downloads/code", ""),
("NOTEBOOK_DIR", "", ""),
("IPYNB_SKIP_CSS", "True", ""),
)

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'
#IPYNB_FIX_CSS = True
IPYNB_SKIP_CSS = True

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about.html'
TWITTER_USERNAME = 'lj020326'
GITHUB_USERNAME = 'lj020326'
LINKEDIN_USERNAME = 'leejjohnson'
LINKED_IN = 'https://www.linkedin.com/in/leejjohnson/'
STACKOVERFLOW_ADDRESS = 'https://stackexchange.com/users/3319937/purplemouse'
AUTHOR_WEBSITE = 'https://dettonville.org'
AUTHOR_BLOG = 'http://leeblog.org'
AUTHOR_CV = "http://leeblog.org/downloads/docs/CV.pdf"
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds
FEED_USE_SUMMARY = True

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico']

## Sitemap info
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}


# Footer info

LICENSE_URL = "https://github.com/lj020326/leeblog.org/blob/master/LICENSE"
LICENSE = "MIT"

## ref: https://github.com/pelican-plugins/liquid-tags
from io import open
EXTRA_HEADER = open('_nb_header.html', encoding='utf-8').read()
