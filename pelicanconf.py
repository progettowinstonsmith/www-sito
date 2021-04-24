#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


def sidebar(value):
    if value.startswith('archives') or value.startswith('category'):
        return 'right-sidebar'
    elif value == 'index':
        return 'index'
    else:
        return 'no-sidebar'

JINJA_FILTERS = {'sidebar': sidebar}

AUTHOR = u'Winston Smith'
SITENAME = u'Progetto Winston Smith'
SITESUBTITLE = u''
SITEURL = 'https://pws.winstonsmith.org'


HEADINGS = (
    ('Progetto Winston Smith', '/'),
)

ORGANIZERS = (
     ('Progetto Winston Smith', 'http://pws.winstonsmith.org'),

)

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = u'it'

USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Telegram', '')
    ('Facebook', '#'),
    ('Twitter', '#'),)

DEFAULT_PAGINATION = 10

YEAR = 2018

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SIDEBAR = ()

THEME = "themes/twenty"

STATIC_PATHS = ['css', 'js', 'images']

PAST_EDITIONS = (
    ('BBA 2012', '/big-brother-award-italia-2012.html'),
    ('BBA 2011', '/big-brother-award-italia-2011.html'),
    ('BBA 2010', '/big-brother-award-italia-2010.html'),
    ('BBA 2009', '/big-brother-award-italia-2009.html'),
    ('BBA 2008', '/big-brother-award-italia-2008.html'),
    ('BBA 2007', '/big-brother-award-italia-2007.html'),
    ('BBA 2006', '/big-brother-award-italia-2006.html'),
    ('BBA 2005', '/big-brother-award-italia-2005.html'),
)

MENUITEMS = (
    ('E-Privacy', 'https://e-privacy.winstonsmith.org/'),
    ('Sostienici', "http://paypal.me/eprivacy"),
)

DISPLAY_PAGES_ON_MENU = False

SUBMENUS = (
    ('Cosa facciamo', "/", (
        ('Convegno e-privacy', 'https://e-privacy.winstonsmith.org'),
        ('Big Brother & CoViD-1984 t-shirts', 'https://worthwearing.org/store/progetto-winston-smith'),
        ('La guida al Voto Digitale', 'https://blog.crvd.org/la-guida-hermes-al-voto-digitale/'),
        #('Big brother award', 'https://bba.winstonsmith.org')
    )),
    ('Chi siamo', "/", (
        ('...io sono Winston Smith', '/pages/io-sono-winston-smith.html'),
        # ('Progetto Winston Smith', 'http://pws.winstonsmith.org'),
        ('collabora', '/pages/collabora.html'),
        ('supporta', "/pages/dona.html"),
        # ('sala stampa', '/pages/stampa.html'),
    )),
)


BANNERFIRST = u"""<p>Progetto<p/>
 <p/><strong>Winston Smith</strong><br /></p>
"""
