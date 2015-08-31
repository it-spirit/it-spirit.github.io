#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'it-spir.it'
SITENAME = u'it-spir.it'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

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
    'extra/README',
    'extra/LICENSE',
]
EXTRA_PATH_METADATA = {
    'extra/README': {
        'path': 'README.rst',
    },
    'extra/LICENSE': {
        'path': 'LICENSE',
    },
}
