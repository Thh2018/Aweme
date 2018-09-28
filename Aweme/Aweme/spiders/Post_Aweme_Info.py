# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Environment: Python3.6.1
import json
import re
import time

import scrapy

from item.Aweme_Info_Item import AwemeInfoItem
from item.User_Post_Aweme_Item import UserPostAwemeItem
from querydata import QueryUserId
from tools import Encrypt
from tools.TimeToTime import timestamp_to_localtime


class AwemeInfoSpider(scrapy.Spider):
    name = 'Post_Aweme_Info'

    def __init__(self):
        """变化参数：max_cursor  user_id mas as ts"""
        self.User_ID_List = QueryUserId.QueryUserId().get_user_id()
        self.base_url = 'https://aweme.snssdk.com'
        self.api = '/aweme/v1/aweme/post/'
        self.params = 'user_id={}&max_cursor=0&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=MuMu&device_brand=Android&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=576*1024&dpi=192&update_version_code=1832&_rticket=1536220140745&ts=1536220143&as=a1e56d39cf5e9b0be04355&cp=d9eeb852f3059ebbe1[cIg&mas=00313caf6d9f1b3dcccf4f876f8de34838acaccc2c0ca6460c469c'
        self.url = self.base_url + self.api + "?" + self.params

    def start_requests(self):
        for user_id in self.User_ID_List:
            start_url1 = self.url.format(user_id[0])
            start_url = Encrypt.get_aweme_token(start_url1)
            yield scrapy.Request(url=start_url, callback=self.parse,
                                 meta={'url': start_url})

    def parse(self, response):
        item = AwemeInfoItem()
        item1 = UserPostAwemeItem()
        data = json.loads(response.body.decode())
        aweme_lists = data["aweme_list"]
        has_more = data['has_more']
        for aweme_list in aweme_lists:
            item['author_user_id'] = aweme_list['author_user_id']  # 作者id
            item1['uid'] = aweme_list['author_user_id']  # 关系表中用户id
            item['aweme_id'] = aweme_list['aweme_id']  # 作品ID
            item1['post_aweme_id'] = aweme_list['aweme_id']  # 关系表中用户发表作品ID
            item['aweme_type'] = aweme_list['aweme_type']  # 作品类型
            create_time = timestamp_to_localtime(int(aweme_list['create_time']))
            item['create_time'] = create_time  # 创建时间
            try:
                item['des'] = re.findall('\w+', aweme_list['desc'])
                item['des'] = ''.join(item['des'])
            except:
                item['des'] = None
            statistics = aweme_list['statistics']
            item['digg_count'] = statistics['digg_count']  # 点赞数
            item['comment_count'] = statistics['comment_count']  # 评论数
            item['share_count'] = statistics['share_count']  # 转发数

            item['is_ads'] = aweme_list['is_ads']  # 是否是广告
            item['is_hash_tag'] = aweme_list['is_hash_tag']  #
            item['is_pgcshow'] = aweme_list['is_pgcshow']  # 是否为pgc显示
            item['is_relieve'] = aweme_list['is_relieve']
            item['is_top'] = aweme_list['is_top']  # 是否置顶
            item['is_vr'] = aweme_list['is_vr']  # 是否是VR视频
            item['item_comment_settings'] = aweme_list[
                'item_comment_settings']  # 评论设置
            item['prevent_download'] = aweme_list['prevent_download']  # 是否禁止下载
            item['rate'] = aweme_list['rate']  # 比率
            item['region'] = aweme_list['region']  # 区域
            share_info = aweme_list['share_info']
            item['share_url'] = share_info['share_url']  # 分享链接
            item['sort_label'] = aweme_list['sort_label']  # 分类标签

            # 音乐
            music = aweme_list['music']
            try:
                item['owner_nickname'] = re.findall('\w+', aweme_list[
                    'owner_nickname'])
                item['owner_nickname'] = ''.join(item['owner_nickname'])
            except:
                item['owner_nickname'] = None
            # item['author'] = music['author']  # 背景音乐作者
            try:
                item['author'] = re.findall('\w+', aweme_list['author'])
                item['author'] = ''.join(item['author'])
            except:
                item['author'] = None
            item['is_del_video'] = music['is_del_video']  # 作者是否删除
            item['cover_hd'] = music['cover_hd']['url_list'][0]  # 封面高清图片地址
            item['cover_large'] = music['cover_large']['url_list'][0]  # 封面大图地址
            item['cover_medium'] = music['cover_medium']['url_list'][
                0]  # 封面中图地址
            item['cover_thumb'] = music['cover_thumb']['url_list'][0]  # 封面小图地址
            item['is_original'] = music['is_original']  # 是否为原创
            item['music_id'] = music['id']  # 音乐ID
            item['is_restricted'] = music['is_restricted']  # 是否保密
            item['is_video_self_see'] = music['is_video_self_see']  # 是否只有自己可看
            item['mid'] = music['mid']  # mid
            if 'owner_handle' in music:
                item['owner_handle'] = music['owner_handle']  # 作者自定义ID
            else:
                item['owner_handle'] = ''
            if 'owner_id' in music:
                item['owner_id'] = music['owner_id']  # 作者ID
            else:
                item['owner_id'] = ''
            item['offline_desc'] = music['offline_desc']  # 线下描述
            play_url = music['play_url']['url_list']  # 播放地址列表
            if len(play_url):  # 播放列表可能为空 添加判断
                item['play_url'] = music['play_url']['url_list'][0]  # 音乐播放地址
            else:
                item['play_url'] = ''
            item['source_platform'] = music['source_platform']  # 来源平台？
            try:
                item['title'] = re.findall('\w+', aweme_list['title'])  # 北京音乐名称
                item['title'] = ''.join(item['title'])
            except:
                item['title'] = None
            item['user_count'] = music['user_count']  # 使用数量
            item['redirect'] = music['redirect']  # 是否重定向
            item['audio_track'] = music['cover_hd']['url_list'][0]  # 音轨地址

            # 视频信息
            video = aweme_list['video']
            item['origin_cover'] = video['origin_cover']['url_list'][0]
            item['height'] = video['height']  # 视频高度
            item['width'] = video['width']  # 视频宽度
            item['has_watermark'] = video['has_watermark']  # 是否有水印
            item['ratio'] = video['ratio']  # 清晰度
            item['duration'] = video['duration']
            item['play_addr_url'] = video['play_addr']['url_list'][0]  # 视频播放url
            item['play_addr_uri'] = video['play_addr']['uri']  # 视频播放uri
            item['url_key'] = video['play_addr']['url_key']  # 视频key
            item['download_addr'] = video['download_addr']['url_list'][
                0]  # 视频下载地址
            item['dynamic_cover'] = video['dynamic_cover']['url_list'][
                0]  # 动态封面地址

            # 风险信息
            risk_infos = aweme_list['risk_infos']
            item['content'] = risk_infos['content']
            item['risk_sink'] = risk_infos['risk_sink']
            item['type'] = risk_infos['type']
            item['warn'] = risk_infos['warn']

            item['pytime'] = time.time()

            yield item
            yield item1

        if has_more == 1:
            max_cursor = data['max_cursor']
            url = re.sub("max_cursor=(\d+)", "max_cursor=" + str(max_cursor),
                         response.meta['url'])
            # 重新获取mas和as加密参数，返回下一页url
            next_start_url = Encrypt.get_aweme_token(url)

            yield scrapy.Request(url=next_start_url, callback=self.parse,
                                 meta={'url': next_start_url})
