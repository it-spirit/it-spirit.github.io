#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'it-spir.it'
SITENAME = u'it-spir.it'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/it_spirit'),
    ('Github', 'https://github.com/it-spirit'),
    ('Bitbucket', 'https://bitbucket.org/it-spirit'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/LICENSE',
    'extra/README',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/LICENSE': {
        'path': 'LICENSE',
    },
    'extra/README': {
        'path': 'README.rst',
    },
    'extra/favicon.ico': {
        'path': 'favicon.ico',
    }
}

ARTICLE_URL = u'blog/{slug}/'
ARTICLE_SAVE_AS = u'blog/{slug}/index.html'
