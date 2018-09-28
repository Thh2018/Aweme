# coding=utf-8
import scrapy


# 关注ID列表
class ConcernInfoItem(scrapy.Item):
    uid = scrapy.Field()  # 用户ID
    concern_id = scrapy.Field()  # 关注用户ID
    max_time = scrapy.Field()  # 本页项目最大创建时间
    begin_time = scrapy.Field()  # 爬虫开始时间
    effective = scrapy.Field()  # 是否有效，默认为1
    pytime = scrapy.Field()
