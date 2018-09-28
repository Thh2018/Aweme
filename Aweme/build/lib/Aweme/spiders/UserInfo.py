# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Environment: Python3.6.1

import json
import re
import time

import scrapy

from item.Fans_Concern_Total import FansConcernItem
from item.User_Info_Item import UserInfoItem
from querydata import QueryUserId
from tools import Encrypt


class FansSpider(scrapy.Spider):
    name = 'UserInfo'

    def __init__(self, *args, **kwargs):
        """变化参数：max_time  user_id mas as ts"""

        super(FansSpider, self).__init__(*args, **kwargs)
        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'https://aweme.snssdk.com'
        self.api = '/aweme/v1/user/'
        self.params = "user_id={}&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=ALP-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024%2A576&dpi=192&update_version_code=1832&_rticket=1536810055399&ts=1536810055&as=a125cd7967d42bbcc94355&mas=002c520bf899c55a590a96590bfac2ce3aacaccc2c9cc6c646464c&cp=d744b05c7b9298c6e1OsKa"
        self.url = self.base_url + self.api + "?" + self.params

    def start_requests(self):
        for user_id in self.User_ID_List:
            start_url1 = self.url.format(user_id[0])
            start_url = Encrypt.get_aweme_token(start_url1)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    def parse(self, response):
        item = UserInfoItem()
        data = json.loads(response.body.decode('utf-8'))
        user_info = data["user"]
        item["uid"] = user_info['uid']  # 用户id
        item["nickname"] = re.findall(r'\w+', user_info['nickname'])  # 用户名
        item["nickname"] = ' '.join(item["nickname"])

        item["short_id"] = user_info['short_id']  # 用户短id
        item["unique_id"] = user_info['unique_id']  # 自定义id
        item["unique_id_modify_time"] = user_info[
            'unique_id_modify_time']  # 自定义id修改时间
        item["total_favorited"] = user_info['total_favorited']  # 抖音总获赞数
        followers_detail = user_info["followers_detail"]
        item["aweme_fans_count"] = followers_detail[0]['fans_count']  # 抖音粉丝数
        item["aweme_apple_id"] = followers_detail[0]['apple_id']  # 抖音apple_id
        item["toutiao_fans_count"] = followers_detail[1]['fans_count']  # 头条粉丝数
        item["toutiao_apple_id"] = followers_detail[1]['apple_id']  # 头条apple_id
        item["live_stream_aweme_fans_count"] = followers_detail[2][
            'fans_count']  # 火山粉丝数
        item["live_stream_apple_id"] = followers_detail[2][
            'apple_id']  # 火山apple_id
        item["aweme_count"] = user_info['aweme_count']  # 抖音作品数
        item["favoriting_count"] = user_info['favoriting_count']  # 抖音喜欢作品数
        item['following_count'] = user_info['following_count']  # 关注总人数

        item["gender"] = user_info['gender']  # 性别
        avatar_larger = user_info["avatar_larger"]
        item['avatar_larger_uri'] = avatar_larger['uri']
        item['avatar_larger_url'] = avatar_larger['url_list'][0]

        # item["weibo_name"] = user_info["weibo_name"]  # 绑定微博
        item['weibo_name'] = re.findall(r'\w', user_info['weibo_name'])  # 绑定微博
        item['weibo_name'] = ''.join(item['weibo_name'])
        item["school_name"] = user_info['school_name']  # 学校名称
        item["school_poi_id"] = user_info['school_poi_id']  # 学校POI ID
        item["school_type"] = user_info['school_type']  # 学校类型
        item["birthday"] = user_info['birthday']  # 出生日期
        item["location"] = user_info['location']  # 位置
        item["constellation"] = user_info['constellation']  # 星座
        item["city"] = user_info['city']
        item["signature"] = re.findall(r'\w+', user_info['signature'])  # 个性签名
        item["signature"] = ' '.join(item["signature"])

        item["login_platform"] = user_info['login_platform']  # 登录方式
        item["is_block"] = user_info['is_block']  # 是否被锁
        # item["custom_verify"] = user_info['custom_verify']
        item["custom_verify"] = re.findall(r'\w+',
                                           user_info['custom_verify'])  #
        item["custom_verify"] = ' '.join(item["custom_verify"])

        # verify_info = user_info['verify_info']
        # item["verify_info"] = is_NULL.is_null(verify_info)  # 认证信息
        item["realname_verify_status"] = user_info[
            'realname_verify_status']  # 是否是实名认证
        item["is_ad_fake"] = user_info['is_ad_fake']  # 是否是假广告？
        item["is_gov_media_vip"] = user_info['is_gov_media_vip']  # 是否是政府单位媒体
        item["is_verified"] = user_info['is_verified']  # 是否验证过
        item["live_agreement"] = user_info['live_agreement']  # 直播资格？
        item["live_verify"] = user_info['live_verify']  # 直播资格认证？
        # 企业认证原因
        item["enterprise_verify_reason"] = user_info['enterprise_verify_reason']
        item["commerce_user_level"] = user_info['commerce_user_level']  # 商务等级
        item["user_canceled"] = user_info['user_canceled']
        item["with_commerce_entry"] = user_info['with_commerce_entry']
        item["with_dou_entry"] = user_info['with_dou_entry']
        item["with_douplus_entry"] = user_info['with_douplus_entry']
        item["with_fusion_shop_entry"] = user_info['with_fusion_shop_entry']
        item["with_new_goods"] = user_info['with_new_goods']
        item["with_shop_entry"] = user_info['with_shop_entry']
        item["need_recommend"] = user_info['need_recommend']
        item["room_id"] = user_info['room_id']
        item["special_lock"] = user_info['special_lock']
        item["pytime"] = time.time()  # 爬虫开始时间

        item1 = FansConcernItem()  # 用户关注人数和粉丝人数
        item1["aweme_fans_count"] = followers_detail[0]['fans_count']  # 抖音粉丝数
        item1['following_count'] = user_info['following_count']  # 关注总人数
        item1["uid"] = user_info['uid']
        item1["pytime"] = time.time()  # 爬虫开始时间

        yield item
        yield item1
