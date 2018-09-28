# coding=utf-8
import scrapy


# 粉丝ID列表
class FansInfoItem(scrapy.Item):
    uid = scrapy.Field()  # 用户ID
    fans_id = scrapy.Field()  # 粉丝ID
    max_time = scrapy.Field()  # 本页爬虫最大创建时间
    effective = scrapy.Field()  # 粉丝是否有效，默认为1
    pytime = scrapy.Field()  # 爬虫开始时间
