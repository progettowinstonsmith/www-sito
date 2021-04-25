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
SITEURL = u'https://pws.winstonsmith.org'


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
SOCIAL = (('Facebook', 'https://www.facebook.com/progetto.winston.smith'),
          ('Twitter', 'https://twitter.com/projectwinnie'),)

DEFAULT_PAGINATION = 10

YEAR = 2018

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SIDEBAR = ()

THEME = "themes/twenty"

STATIC_PATHS = ['css', 'js', 'images']

MENUITEMS = (
    ('E-Privacy', 'https://e-privacy.winstonsmith.org/'),
    ('Sostieni!', "http://paypal.me/eprivacy"),
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
        ('Il Manifesto', '/pages/manifesto-pws.html'),
        ('collabora', '/pages/collabora.html'),
        ('supporta', "/pages/dona.html"),
        # ('sala stampa', '/pages/stampa.html'),
    )),
)


BANNERFIRST = u"""<p>Progetto<p/>
 <p/><strong>Winston Smith</strong><br /></p>
"""
