# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Environment: Python3.6.1
import json
import re
import time

import scrapy

from item.Comment_Info_Item import CommentInfoItem
from querydata import QueryAwemeId
from tools.Encrypt import get_aweme_token


class CommentInfoSpider(scrapy.Spider):
    name = 'CommentInfo'

    def __init__(self, *args, **kwargs):
        """变化参数：max_time  user_id mas as ts"""

        super(CommentInfoSpider, self).__init__(*args, **kwargs)
        # # 从数据库中获取作品ID
        self.Aweme_ID_List = QueryAwemeId.QueryAwemeId().get_aweme_id()
        self.base_url = 'https://aweme.snssdk.com'
        self.api = '/aweme/v1/comment/list/'
        self.params = (
            "aweme_id={}&cursor=0&count=20&comment_style=2&digged_cid=&insert_cids=&ts=1537852756&app_type=normal&os_api=23&device_type=MuMu&device_platform=android&ssmix=a&iid=43398130756&manifest_version_code=183&dpi=192&uuid=008796758836908&version_code=183&app_name=aweme&version_name=1.8.3&openudid=14c5f0e306271ae&device_id=57259297041&resolution=576*1024&os_version=6.0.1&language=zh&device_brand=Android&ac=wifi&update_version_code=1832&aid=1128&channel=aweGW&_rticket=1536558941166&as=a1b510c93e555b07764355&cp=015fbf54e06c9a75e1Ycag&mas=007fd54dfdbfb7b48bcb4841250d989668acaccc2c6cecec0c46ac")
        self.url = self.base_url + self.api + "?" + self.params

    def start_requests(self):
        for aweme_id in self.Aweme_ID_List:
            start_url1 = self.url.format(aweme_id[0])
            start_url = get_aweme_token(start_url1)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    def parse(self, response):
        item = CommentInfoItem()
        data = json.loads(response.body.decode())
        has_more = data["has_more"]
        comment_lists = data["comments"]

        for comment_list in comment_lists:
            item["aweme_id"] = comment_list["aweme_id"]  # 作品ID
            item["create_time"] = comment_list["create_time"]  # 评论时间
            item["cid"] = comment_list['cid']  # 评论ID
            # item["text"] = comment_list["text"]  # 评论内容
            item["text"] = re.findall(r'\w+', comment_list['text'])  # 评论内容
            item["text"] = ' '.join(item["text"])

            item["digg_count"] = comment_list["digg_count"]  # 该评论点赞数
            item["user_id"] = comment_list["user"]["uid"]  # 评论者ID
            item["total"] = data["total"]  # 评论总数
            item["status"] = comment_list["status"]  # 状态
            item["pytime"] = time.time()  # 爬取时间
            item["reply_id"] = comment_list["reply_id"]  # 回复ID
            yield item
        while has_more:
            cursor = str(data["cursor"])
            next_url = re.sub("cursor=(\d+)", "cursor=" + cursor,
                              response.meta['url'])  # 得到下一页评论信息
            start_url = get_aweme_token(next_url)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})
