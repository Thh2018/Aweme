# -*- coding: utf-8 -*-

# Scrapy settings for Aweme project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import os

import sys

BOT_NAME = 'Aweme'

SPIDER_MODULES = ['Aweme.spiders']
NEWSPIDER_MODULE = 'Aweme.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Aweme (+http://www.yourdomain.com)'
USER_AGENT = 'okhttp/3.7.0.6'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8  # 最大并发下载量

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'Aweme.middlewares.AwemeSpiderMiddleware': 543,
# }
# 增量去重
SPIDER_MIDDLEWARES = {
    'scrapy_deltafetch.DeltaFetch': 100,
}
DELTAFETCH_ENABLED = True
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
#     'Aweme.middlewares.AwemeDownloaderMiddleware': 543,
#     'Aweme.middlewares.IPPOOLS': 143,
# }


DOWNLOADER_MIDDLEWARES = {
    # 代理
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
    'Aweme.middlewares.ProxyMiddleware': 300,
    # 随机user-agent
    # 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
    #  'Aweme.middlewares.RandomUserAgentMiddleware':200,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/itemxion -pipeline.html
ITEM_PIPELINES = {
    # 'Aweme.pipelines.DouyinPipeline': 300,
    # 'Aweme.pipelines.UserInfoPipeline': 300,
    'Aweme.pipelines.DouyinMySQLPipline': 300,
    # 'Aweme.pipelines.MySQLTwistedPipeline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# 启用限速设置
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.2  # 初始下载延迟
DOWNLOAD_DELAY = 0.2  # 每次请求间隔时间
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# LOG_LEVEL = "ERROR"

# # MySQL数据库的配置信息
MYSQL_HOST = 'db.test.moheah.com'
MYSQL_DBNAME = 'douyinpython'  # 数据库名字，请修改
MYSQL_USER = 'douyinpython'  # 数据库账号，请修改
MYSQL_PASSWD = 'Douyinpython!!'  # 数据库密码，请修改
MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

# MYSQL_HOST = 'localhost'
# MYSQL_DBNAME = 'douyinpython'  # 数据库名字，请修改
# MYSQL_USER = 'root'  # 数据库账号，请修改
# MYSQL_PASSWD = '123.com'     #密码修改
# MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

# MYSQL_HOST = 'l92.168.1.5'
# MYSQL_DBNAME = 'main'  # 数据库名字，请修改
# MYSQL_USER = 'root'  # 数据库账号，请修改
# MYSQL_PASSWD = '123.com'     #密码修改
# MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'Aweme'))
