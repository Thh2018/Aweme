# coding = utf-8
import scrapy


# 评论信息
class CommentInfoItem(scrapy.Item):
    aweme_id = scrapy.Field()  # 作品ID
    create_time = scrapy.Field()  # 评论时间
    text = scrapy.Field()  # 评论内容
    user_id = scrapy.Field()  # 用户ID
    total = scrapy.Field()  # 评论总数
    digg_count = scrapy.Field()  # 评论点赞数
    cid = scrapy.Field()  # 评论ID
    status = scrapy.Field()  # 状态
    reply_id = scrapy.Field()  # 回复ID
    pytime = scrapy.Field()  # 爬取时间
