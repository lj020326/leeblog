#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# SITEURL = 'http://lj020326.github.io'
SITEURL = 'https://leeblog.org'
RELATIVE_URLS = False

SHOW_FEED = True
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_USE_SUMMARY = True  # from the feed_summary plugin

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "lj020326-github-io"
GOOGLE_ANALYTICS = "UA-117727381-1"
