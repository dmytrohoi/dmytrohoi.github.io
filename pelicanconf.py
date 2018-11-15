#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Dmytro Hoi'
SITENAME = 'Dmytro Hoi'
SITEURL = ''
SITETITLE = 'Dmytro Hoi'
SITESUBTITLE = 'Python Developer and Blogger'
SITEDESCRIPTION = 'On this site you find my articles, links to social networks and CV. \nNice to meet you here!'
SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

PATH = 'content'
STATIC_PATHS = ['images', 'pages', 'pdfs', 'extra']
PAGE_PATHS = ['pages']
PLUGIN_PATHS = ['plugins']

ARTICLE_PATHS = ['blog', 'projects', 'books', 'podcasts']

THEME = '/mnt/Files/CODE/PROJECT/dmytrohoi.github.io/main/dmytrohoi.github.io'
PLUGINS = ['representative_image', 'post_stats', 'pelican_alias']

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                        'extra/LICENSE.md': {'path': 'LICENSE.md'},
                        'extra/README.md': {'path': 'README.md'},
                        'extra/robots.txt': {'path': 'robots.txt'},
                        }


TIMEZONE = 'Europe/Vilnius'

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = True

# Blogroll
MAIN_MENU = True

LINKS = ( ('Blog', '/category/blog.html'),
        ('Books', '/category/books.html'),
         ('Projects', '/category/projects.html'),
         ('About', '/about.html'),
         ('Podcasts', '/category/podcasts.html'),
         )

# Social widget
SOCIAL = (('fab fa-facebook', 'http://fb.com/dmytro.hoi'),
          ('fab fa-telegram', 'http://t.me/progsrc'),
          ('fab fa-github-square', 'http://github.com/dmytrohoi'),
          ('fab fa-linkedin', 'http://linkedin.com/in/dmytrohoi'),
          ('fab fa-twitter-square', 'http://twitter.com/criticoffer'),
        #   ('', ''),
          ('fab fa-dev', 'http://dev.to/dmytrohoi'),
          ('fas fa-broadcast-tower', '/category/podcasts'),
          ('fas fa-rss-square', '/feeds/all.atom.xml'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CATEGORY_IMAGES = ['projects', 'blog']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = False


PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
CATEGORY_URL = 'category/{slug}/'

DEFAULT_DATE = 'fs'

ROBOTS = 'index, follow'

COPYRIGHT_YEAR = str(datetime.now().year)

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

DATE_FORMATS = {
    'en': r'%B %d, %Y',
}

# MARKDOWN = {
#         'extension' : ['markdown.extensions.codehilite', 'markdown.extensions.extra', 'markdown.extensions.meta', 'markdown.extensions.toc'],
#         # 'extension_configs': {
#         #     'markdown.extensions.codehilite': {
#         #         'css_class': 'highlight',
#         #     },
#         #     'markdown.extensions.extra': {},
#         #     'markdown.extensions.meta': {},
#         #     'markdown.extensions.toc': {},
#         # },
#         # 'output_format': 'html5',
    # }

DISQUS_SITENAME = 'hoi-pp'
ADD_THIS_ID = 'ra-5be372bf4e2a102c'

GOOGLE_TAG_MANAGER = "GTM-TSH38JV"
GOOGLE_ANALYTICS = "UA-129013894-1"
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-3596869803955189',
    'page_level_ads': True,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '',
        'article_top': '',
        'article_bottom': '',
    }
}