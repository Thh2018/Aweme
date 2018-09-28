# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Environment: Python3.6.1
import json
import re
import time

import scrapy

from item.Likes_info_Item import ConcernInfoItem
from querydata import QueryUserId
from tools import Encrypt


class AwemeInfoSpider(scrapy.Spider):
    name = 'LikeList'

    def __init__(self, *args, **kwargs):
        super(AwemeInfoSpider, self).__init__(*args, **kwargs)
        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'https://aweme.snssdk.com'
        self.api = '/aweme/v1/user/following/list/'
        self.params = "user_id={}&max_time=1537436091&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=MuMu&device_brand=Android&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024%2A576&dpi=192&update_version_code=1832&_rticket=1536544908721&ts=1536544908&as=a1d50d99fc687bd0f54355&mas=00af178a284dd5a08a570443e924fbdda6acaccc2cac660c2646ec&cp=d683b959c1559b08e1WsKa"
        self.url = self.base_url + self.api + "?" + self.params

    # 遍历url并请求访问
    def start_requests(self):
        for user_id in self.User_ID_List:
            url = self.url.format(user_id[0])
            start_url = Encrypt.get_aweme_token(url)  # 获取加密参数cp as mas
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    # 解析响应json数据
    def parse(self, response):
        item = ConcernInfoItem()
        data = json.loads(response.body.decode())
        concern_lists = data["followings"]
        # 判断是否有下一页的参数
        has_more = data["has_more"]

        for concern_list in concern_lists:
            item["concern_id"] = concern_list["uid"]
            item['uid'] = re.search('user_id=(\d+)',
                                    response.meta['url']).group(1)
            item['max_time'] = re.search("max_time=(\d+)",
                                         response.meta['url']).group(1)
            item['effective'] = 1
            item["pytime"] = time.time()
            print(item)
            yield item

        while has_more:
            # 下一页url中的"max_time"为上一次json数据中的"min_time"
            max_time = str(data["min_time"])
            url = re.sub("max_time=(\d+)", "max_time=" + max_time,
                         response.meta['url'])
            # 重新获取mas和as加密参数，返回下一页url
            next_start_url = Encrypt.get_aweme_token(url)

            yield scrapy.Request(url=next_start_url, callback=self.parse,
                                 meta={'url': next_start_url})
