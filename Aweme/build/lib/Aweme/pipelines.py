# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings
from twisted.enterprise import adbapi


# # 异步存储到MySQL数据库中
from item.Aweme_Info_Item import AwemeInfoItem
from item.Comment_Info_Item import CommentInfoItem
from item.Fans_Concern_Total import FansConcernItem
from item.Fans_Info_Item import FansInfoItem
from item.Likes_info_Item import ConcernInfoItem
from item.User_Info_Item import UserInfoItem
from item.User_Like_Aweme_Item import UserLikeAwemeItem


class DouyinMySQLPipline(object):
    def __init__(self, ):
        self.settings = get_project_settings()
        dbparms = dict(
            host=self.settings['MYSQL_HOST'],
            db=self.settings['MYSQL_DBNAME'],
            user=self.settings['MYSQL_USER'],
            passwd=self.settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,  # 指定 cursor 类型
            use_unicode=True,
        )

        # 指定擦做数据库的模块名和数据库参数参数
        # 初始化数据库连接池(线程池)
        # 参数一：mysql的驱动
        # 参数二：连接mysql的配置信息
        self.dbpool = adbapi.ConnectionPool("pymysql", **dbparms)

    # 使用twisted将mysql插入变成异步执行
    def process_item(self, item, spider):
        # 指定操作方法和操作的数据
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 指定异常处理方法
        # 如果异步任务执行失败的话，可以通过ErrBack()进行监听, 给insert_db添加一个执行失败的回调事件
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        # insert_sql, params = item.get_insert_sql()

        # 这是UserInfo 表，44个字段 ,对应的是User_Info_Item.py
        if isinstance(item, UserInfoItem):
            try:
                params = (item['nickname'], item['uid'], item['short_id'],
                          item['unique_id'], item['unique_id_modify_time'],
                          item['total_favorited'], item['aweme_fans_count'],
                          item['aweme_apple_id'], item['toutiao_fans_count'],
                          item['toutiao_apple_id'],
                          item['live_stream_aweme_fans_count'],
                          item['live_stream_apple_id'], item['aweme_count'],
                          item['favoriting_count'], item['gender'],
                          item['avatar_larger_uri'], item['avatar_larger_url'],
                          item['weibo_name'], item['school_name'],
                          item['school_poi_id'],
                          item['school_type'], item['location'],
                          item['birthday'], item['constellation'], item['city'],
                          item['signature'], item['login_platform'],
                          item['realname_verify_status'], item['is_block'],
                          item['custom_verify'],
                          item['is_ad_fake'], item['is_gov_media_vip'],
                          item['live_agreement'], item['live_verify'],
                          item['enterprise_verify_reason'],
                          item['commerce_user_level'], item['user_canceled'],
                          item['with_commerce_entry'], item['with_dou_entry'],
                          item['with_douplus_entry'],
                          item['with_shop_entry'], item['with_new_goods'],
                          item['with_fusion_shop_entry'],
                          item['need_recommend'],
                          item['room_id'], item['special_lock'],
                          item['pytime'])

                sql = (
                    "INSERT INTO userinfo(nickname ,uid , short_id , unique_id , unique_id_modify_time ,total_favorited , aweme_fans_count , aweme_apple_id , toutiao_fans_count , toutiao_apple_id , live_stream_aweme_fans_count , live_stream_apple_id , aweme_count , favoriting_count ,gender , avatar_larger_uri , avatar_larger_url , weibo_name , school_name , school_poi_id , school_type , location , birthday ,constellation , city , signature , login_platform ,realname_verify_status , is_block , custom_verify , is_ad_fake , is_gov_media_vip , live_agreement,live_verify,enterprise_verify_reason,commerce_user_level,user_canceled,with_commerce_entry,with_dou_entry,with_douplus_entry,with_shop_entry,with_new_goods,with_fusion_shop_entry,need_recommend,room_id,special_lock,pytime) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                cursor.execute(sql, params)
            except Exception as error:
                print(error)

        # 这是UserInfo_concern 表， 4个字段, 对应的是Aweme_Info_Item.py
        elif isinstance(item, FansConcernItem):
            try:
                params = (
                    item['uid'], item['aweme_fans_count'],
                    item['following_count'],
                    item['pytime'])
                sql = "INSERT INTO userinfo_concern(uid ,aweme_fans_count , following_count , pytime) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, params)
            except Exception as error:
                print(error)

        # 这是 UserInfo_concern_ID 表， 5个字段 , 对应的是 Likes_info_Item.py
        elif isinstance(item, ConcernInfoItem):
            try:
                params = (item['uid'], item['concern_id'], item['max_time'],
                          item['effective'], item['pytime'])
                sql = "INSERT INTO userinfo_concern_id(uid , concern_id , max_time , effective , pytime) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, params)
            except Exception as error:
                print(error)

        # 这是UserInfo_fans_ID 表，5个字段 , 对应的是 Fans_Info_Item.py
        elif isinstance(item, FansInfoItem):
            try:
                params = (item['uid'], item['fans_id'], item['max_time'],
                          item['effective'], item['pytime'])
                sql = "INSERT INTO userinfo_fans_id(uid , fans_id , max_time , effective , pytime) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, params)
            except Exception as error:
                print(error)


        # 这是Works 表，54个字段 , 对应的是 Aweme_Info_Item.py
        elif isinstance(item, AwemeInfoItem):
            try:
                params = (
                    item['aweme_id'], item['author_user_id'],
                    item['aweme_type'],
                    item['create_time'], item['duration'], item['des'],
                    item['digg_count'], item['comment_count'],
                    item['share_count'],
                    item['is_ads'],
                    item['is_hash_tag'], item['is_pgcshow'], item['is_relieve'],
                    item['is_top'], item['is_vr'],
                    item['item_comment_settings'],
                    item['prevent_download'], item['rate'], item['region'],
                    item['share_url'],
                    item['sort_label'], item['owner_nickname'],
                    item['author'], item['is_del_video'],
                    item['cover_thumb'], item['is_original'],
                    item['music_id'], item['is_restricted'],
                    item['is_video_self_see'], item['mid'],
                    item['owner_handle'], item['owner_id'],
                    item['offline_desc'], item['play_url'],
                    item['source_platform'], item['title'],
                    item['user_count'], item['redirect'],
                    item['audio_track'], item['origin_cover'],
                    item['height'], item['width'],
                    item['has_watermark'], item['ratio'],
                    item['play_addr_uri'], item['play_addr_url'],
                    item['url_key'], item['download_addr'],
                    item['dynamic_cover'], item['content'],
                    item['risk_sink'], item['type'], item['warn'],
                    item['pytime'])
                sql = "INSERT INTO works(aweme_id , author_user_id , aweme_type , create_time , duration , des , digg_count , comment_count , share_count , is_ads , " \
                      "is_hash_tag , is_pgcshow ,is_relieve ,is_top ,is_vr , item_comment_settings , prevent_download ,rate , region , share_url ," \
                      "sort_label , music_owner_nickname , music_author , music_is_del_video ,music_cover_thumb ,music_is_original ,music_id, music_is_restricted ,music_is_video_self_see, music_mid ," \
                      "music_owner_handle , music_owner_id , music_offline_desc , music_play_url , music_source_platform , music_title , music_user_count , music_redirect , music_audio_track ,video_origin_cover ," \
                      "video_height ,video_width ,video_has_watermark ,video_ratio ,video_play_addr_uri ,video_play_addr_url ,video_url_key ,video_download_addr ,video_dynamic_cover ,risk_content ," \
                      "risk_sink ,risk_type ,risk_warn , pytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, params)
            except Exception as error:
                print(error)

        # 这是Works_comment 表，10个字段 , 对应的是 Comment_Info_Item.py
        elif isinstance(item, CommentInfoItem):
            try:
                params = (
                    item['aweme_id'], item['create_time'], item['digg_count'],
                    item['user_id'], item['cid'], item['text'], item['status'],
                    item['reply_id'], item['total'], item['pytime'])
                sql = "INSERT INTO works_comment(aweme_id ,create_time ,digg_count ,user_id ,cid ,text ,status ,reply_id ,total ,pytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, params)
            except Exception as error:
                print(error)
        elif isinstance(item, UserLikeAwemeItem):
            try:
                params = (
                    item['uid'], item['like_aweme_id']
                )
                sql = "INSERT INTO user_like_aweme(uid,like_aweme_id) VALUES (%s, %s)"
                cursor.execute(sql, params)
            except Exception as error:
                print(error)

    def close_spider(self):
        pass

#########
########
########


# class MySQLTwistedPipeline(object):
#     def __init__(self, pool):
#         self.dbpool = pool
#
#     @classmethod
#     def from_settings(cls, settings):
#         """
#         这个函数名称是固定的，当爬虫启动的时候，scrapy会自动调用这些函数，加载配置数据。
#         :param settings:
#         :return:
#         """
#         params = dict(
#             host=settings['MYSQL_HOST'],
#             port=settings['MYSQL_PORT'],
#             db=settings['MYSQL_DB'],
#             user=settings['MYSQL_USER'],
#             passwd=settings['MYSQL_PASSWD'],
#             charset=settings['MYSQL_CHARSET'],
#             cursorclass=pymysql.cursors.DictCursor
#         )
#
#         # 创建一个数据库连接池对象，这个连接池中可以包含多个connect连接对象。
#         # 参数1：操作数据库的包名
#         # 参数2：链接数据库的参数
#         db_connect_pool = adbapi.ConnectionPool('pymysql', **params)
#
#         # 初始化这个类的对象
#         obj = cls(db_connect_pool)
#         return obj
#
#     def process_item(self, item, spider):
#         """
#         在连接池中，开始执行数据的多线程写入操作。
#         :param item:
#         :param spider:
#         :return:
#         """
#         # 参数1：在线程中被执行的sql语句
#         # 参数2：要保存的数据
#         result = self.dbpool.runInteraction(self.insert, item)
#         # 给result绑定一个回调函数，用于监听错误信息
#         result.addErrback(self.error)
#
#     def error(self, reason):
#         print('--------', reason)
#     # 线面这两步分别是数据库的插入语句，以及执行插入语句。这里把插入的数据和sql语句分开写了，跟何在一起写效果是一样的
#     def insert(self, cursor, item):
#
#         # 这是UserInfo 表，44个字段 ,对应的是User_Info_Item.py
#         if isinstance(item.UserInfoItem):
#             try:
#                 insert_sql = "INSERT INTO bole(nickname , uid , short_id , unique_id , unique_id_modify_time , total_favorited , aweme_fans_count , aweme_apple_id , toutiao_fans_count , toutiao_apple_id , live_stream_aweme_fans_count , live_stream_apple_id , aweme_count , favoriting_count , gender , avatar_larger_uri , avatar_larger_url , weibo_name , school_name , school_poi_id , school_type , location , birthday ,constellation , city , signature , login_platform , realname_verify_status , is_block , custom_verify , is_ad_fake , is_gov_media_vip , live_agreement , pytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#                 cursor.execute(insert_sql, (item['nickname'], item['uid'], item['short_id'], item['unique_id'], item['unique_id_modify_time'], item['total_favorited'], item['aweme_fans_count'], item['aweme_apple_id'], item['toutiao_fans_count'], item['toutiao_apple_id'],
#                                             item['live_stream_aweme_fans_count'], item['live_stream_apple_id'], item['aweme_count'], item['favoriting_count'], item['gender'], item['avatar_larger_uri'], item['avatar_larger_url'], item['weibo_name'], item['school_name'], item['school_poi_id'],
#                                             item['school_type'], item['location'], item['birthday'], item['constellation'], item['city'], item['signature'], item['login_platform'], item['realname_verify_status'], item['is_block'], item['custom_verify'],
#                                             item['is_ad_fake'], item['is_gov_media_vip'], item['live_agreement'] , item['pytime']))
#             except Exception as error:
#                 print(error)
#
#
#         # 这是UserInfo_concern 表， 4个字段, 对应的是Aweme_Info_Item.py
#         elif isinstance(item, AwemeInfoItem):
#             try:
#                 insert_sql = "INSERT INTO bole(uid ,aweme_fans_count , following_count , pytime) VALUES (%s, %s, %s, %s)"
#                 cursor.execute(insert_sql, (item['uid'], item['aweme_fans_count'], item['following_count'], item['pytime']))
#
#             except Exception as error:
#                 print(error)
#
#
#         # 这是 UserInfo_concern_ID 表， 5个字段 , 对应的是 Likes_info_Item.py
#         elif isinstance(item, ConcernInfoItem):
#             try:
#                 insert_sql = "INSERT INTO bole(uid , concern_id , max_time , effective , pytime) VALUES (%s, %s, %s, %s, %s)"
#                 cursor.execute(insert_sql, (item['uid'], item['concern_id'], item['max_time'], item['effective'], item['pytime']
#             ))
#             except Exception as error:
#                 print(error)
#
#
#         # 这是UserInfo_fans_ID 表，5个字段 , 对应的是 Fans_Info_Item.py
#         elif isinstance(item, FansInfoItem):
#             try:
#                 insert_sql = "INSERT INTO bole(uid , fans_id , max_time , effective , pytime) VALUES (%s, %s, %s, %s, %s)"
#                 cursor.execute(insert_sql, (item['uid'], item['fans_id'], item['max_time'],item['effective'], item['pytime']
#             ))
#             except Exception as error:
#                 print(error)
#
#         # 这是Works 表，54个字段 , 对应的是 Aweme_Info_Item.py
#         elif isinstance(item, AwemeInfoItem):
#             try:
#                 insert_sql = "INSERT INTO bole(aweme_id , author_user_id , aweme_type , create_time , duration , desc , digg_count , comment_count , share_count , is_ads , is_ads , " \
#                       "is_hash_tag , is_pgcshow ,is_relieve ,is_top ,is_vr , item_comment_settings , prevent_download ,rate , region , share_url ," \
#                       "sort_label , music_owner_nickname , music_author , music_is_del_video ,music_cover_thumb ,music_is_original ,music_music_id, music_is_restricted ,music_is_video_self_see, music_mid ," \
#                       "music_owner_handle , music_owner_id , music_offline_desc , music_play_url , music_source_platform , music_title , music_user_count , music_redirect , music_audio_track ,video_origin_cover ," \
#                       "video_height ,video_width ,video_has_watermark ,video_ratio ,video_play_addr_uri ,video_play_addr_url ,video_url_key ,video_download_addr ,video_dynamic_cover ,risk_content ," \
#                       "risk_sink ,risk_type ,risk_warn , pytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#                 cursor.execute(insert_sql, (item['aweme_id'], item['author_user_id'], item['aweme_type'], item['create_time'], item['duration'], item['desc'], item['digg_count'], item['comment_count'], item['share_count'], item['is_ads'],
#                                             item['is_hash_tag'], item['is_pgcshow'], item['is_relieve'], item['is_top'], item['is_vr'], item['item_comment_settings'], item['prevent_download'], item['rate'], item['region'], item['share_url'],
#                                             item['sort_label'], item['music_owner_nickname'], item['music_author'], item['music_is_del_video'], item['music_cover_thumb'], item['music_is_original'], item['music_music_id'], item['music_is_restricted'], item['music_is_video_self_see'], item['music_mid'],
#                                             item['music_owner_handle'], item['music_owner_id'], item['music_offline_desc'], item['music_play_url'], item['music_source_platform'], item['music_title'], item['music_user_count'], item['music_redirect'], item['music_audio_track'], item['video_origin_cover'],
#                                             item['video_height'], item['video_width'], item['video_has_watermark'], item['video_ratio'], item['video_play_addr_uri'], item['video_play_addr_url'], item['video_url_key'], item['video_download_addr'], item['video_dynamic_cover'], item['risk_content'],
#                                             item['risk_sink'], item['risk_type'], item['risk_warn'], item['pytime']))
#             except Exception as error:
#                 print(error)
#
#
#
#         # 这是Works_comment 表，10个字段 , 对应的是 Comment_Info_Item.py
#         elif isinstance(item, CommentInfoItem):
#             try:
#                 insert_sql = "INSERT INTO bole(aweme_id ,create_time ,digg_count ,user_uid ,cid ,text ,status ,reply_id ,total ,pytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#                 cursor.execute(insert_sql, (item['aweme_id'], item['create_time'], item['digg_count'], item['user_uid'], item['cid'], item['text'], item['status'], item['reply_id'], item['total'], item['pytime']
#             ))
#
#             except Exception as error:
#                 print(error)
#
#
#     def close_spider(self):
#         pass
