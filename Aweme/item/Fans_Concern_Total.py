# coding=utf-8
import scrapy


# 用户粉丝总数与关注总数
class FansConcernItem(scrapy.Item):
    uid = scrapy.Field()
    aweme_fans_count = scrapy.Field()
    following_count = scrapy.Field()
    pytime = scrapy.Field()
