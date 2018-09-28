# coding=utf-8
import scrapy
from scrapy import Item


class UserPostAwemeItem(Item):
    uid = scrapy.Field()  # 用户ID
    post_aweme_id = scrapy.Field()  # 用户发表作品ID
