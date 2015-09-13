#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'it-spir.it'
SITENAME = u'it-spir.it'
SITEURL = u''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'
DATE_FORMATS = {
    'en': ('en_US', '%b %d, %Y'),
}

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Plone.org', 'http://plone.org/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/it_spirit'),
    ('Github', 'https://github.com/it-spirit'),
    ('Bitbucket', 'https://bitbucket.org/it-spirit'),
)

MENUITEMS = (
    # ('Home', u'{0}/'.format(SITEURL)),
    # ('Services', u'{0}/services.html'.format(SITEURL)),
    # ('References', u'{0}/references.html'.format(SITEURL)),
    # # ('About Us', '/pages/about.html'),
    # # ('Contact Us', '/pages/contact.html'),
    # ('Blog', u'{0}/blog'.format(SITEURL)),
    # # ('Co-Working', '/pages/coworking.html'),
    # # ('Impressum', '/impressum.html'),
    # # ('Archives', '/archives.html'),
)

DEFAULT_PAGINATION = 5

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

ARTICLE_URL = u'blog/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
ARTICLE_SAVE_AS = u'blog/{date:%Y}-{date:%m}-{date:%d}-{slug}.html'
INDEX_SAVE_AS = u'blog/index.html'
PAGE_ORDER_BY = 'sort_order'
PAGE_SAVE_AS = u'{slug}.html'
PAGE_URL = u'{slug}.html'
TAGS_SAVE_AS = u'tags/index.html'
TAG_SAVE_AS = u'tags/{slug}.html'
TAG_URL = u'tags/{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False

JINJA_EXTENSIONS = [
    u'jinja2.ext.with_',
]
THEME = u'pelican_unify'

# Theme options
UNIFY_BREADCRUMBS_INDEX = u'Blog'
UNIFY_BREADCRUMBS_INDEX_VISIBLE = True
UNIFY_BREADCRUMBS_TAG = u'Tags'
UNIFY_BREADCRUMBS_TAG_VISIBLE = True
UNIFY_SHOW_ARTICLE_BREADCRUMBS = True
UNIFY_SHOW_ARTICLE_BREADCRUMBS_CATEGORY = True
UNIFY_SHOW_PAGE_BREADCRUMBS = True
UNIFY_FAVICON = u'favicon.ico'
UNIFY_FOOTER = u'footer-v1'
UNIFY_FOOTER_ABOUT = """
<p>We love to <a href="{site_url}/services.html">turn ideas into
beautiful things</a>.<br>We love to
<a href="{site_url}/references.html">build great software</a>.<br>We love
<a href="http://python.org" target="_blank">Python</a>.</p>
""".format(site_url=SITEURL)

UNIFY_FOOTER_CONTACT = """
<p>it-spirit<br>
Regenleitenstr. 13<br>
87600 Kaufbeuren, Germany<br>
Phone: +49-(0)8341-9966186-0<br>
Fax: +49-(0)8341-9966186-9<br>
Email: <a href="mailto:info@it-spir.it" class="">info@it-spir.it</a></p>
"""
UNIFY_FOOTER_COPYRIGHT = """
<p>Copyright &copy; 2015 <a href="http://it-spir.it"
title="IT-Consulting &amp; Software Development">it-spirit</a>.
All rights reserved.
</p>
"""
UNIFY_FOOTER_RECENT_ARTICLES_COUNT = 3
UNIFY_FOOTER_RECENT_ARTICLES_HEADLINE = u'Recent Blog Items'
UNIFY_HEADER = u'header-v3'
UNIFY_HEADER_FIXED = False
UNIFY_HEADING_BLOG = u'Articles about Technology'
UNIFY_HEADING_INDEX = u'Articles about Technology'
UNIFY_LAYOUT_BOXED = True
