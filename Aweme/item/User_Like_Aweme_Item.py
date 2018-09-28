# coding=utf-8
import scrapy
from scrapy import Item


class UserLikeAwemeItem(Item):
    uid = scrapy.Field()  # 用户ID
    like_aweme_id = scrapy.Field()  # 用户喜欢作品ID
