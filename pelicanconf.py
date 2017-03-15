#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# Site settings
AUTHOR = u'Kevin'
SITENAME = u"Kevin's Blog"
SITEURL = 'http://www.feisblog.com'

SITESUBTITLE = '专注自动化运维、大数据、云计算'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
#添加订阅等功能
SOCIAL = (
		   ('RSS','http://feisblog.com/feeds/all.atom.xml'),
          )

DEFAULT_PAGINATION = 10
#模板配置

THEME = 'pelican-themes/bootstrap2'
DISQUS_SITENAME = u'feisblog'
#URL配置
ARTICLE_URL = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

##设置菜单项
MENUITEMS = (
            
            )
###添加静态文件			
STATIC_PATHS = ['img']


#Pelican 插件
PLUGIN_PATH = 'pelican-plugins'     #设置路径
PLUGINS = ['summary','sitemap','neighbors'] #选用插件

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.7,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}



#这个是farseerfc同学自己加的, 可以显示他的新浪微博内容, 有微博的话可以把这些加上~
#~ TWITTER_USERNAME = 'farseerfc'
#~ SIDEBAR_CUSTOM = r"""
#~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
#~ src="<http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1>">
#~ </iframe>
#~ """

#google自定义搜索(大概是站内搜索吧)
#~ GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
#~ GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"