# coding=utf-8
import scrapy
from scrapy import Item


class UserLikeAwemeItem(Item):
    uid = scrapy.Field()
    like_aweme_id = scrapy.Field()
