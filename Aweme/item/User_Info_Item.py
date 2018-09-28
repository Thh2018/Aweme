# coding = utf-8

# 用户个人信息
import scrapy


class UserInfoItem(scrapy.Item):
    nickname = scrapy.Field()  # 用户名
    uid = scrapy.Field()  # 用户ID
    short_id = scrapy.Field()  # 用户短ID
    unique_id = scrapy.Field()  # 自定义ID
    unique_id_modify_time = scrapy.Field()  # 自定义ID修改时间
    total_favorited = scrapy.Field()  # 抖音总获赞数
    aweme_fans_count = scrapy.Field()  # 抖音粉丝数
    aweme_apple_id = scrapy.Field()  # 抖音apple_id
    toutiao_fans_count = scrapy.Field()  # 头条粉丝数
    toutiao_apple_id = scrapy.Field()  # 头条apple_id
    live_stream_aweme_fans_count = scrapy.Field()  # 火山小视频粉丝数
    live_stream_apple_id = scrapy.Field()  # 火山apple_id
    aweme_count = scrapy.Field()  # 抖音作品数量
    favoriting_count = scrapy.Field()  # 抖音喜欢作品数
    following_count = scrapy.Field()  # 抖音关注总数

    gender = scrapy.Field()  # 性别
    avatar_larger_url = scrapy.Field()  # 头像url
    avatar_larger_uri = scrapy.Field()  # 头像uri
    weibo_name = scrapy.Field()  # 绑定微博
    school_name = scrapy.Field()  # 学校名称
    school_poi_id = scrapy.Field()  # 学校POI ID
    school_type = scrapy.Field()  # 学校类型
    location = scrapy.Field()  # 位置
    birthday = scrapy.Field()  # 出生日期
    constellation = scrapy.Field()  # 星座
    city = scrapy.Field()  # 城市
    signature = scrapy.Field()  # 个性签名
    login_platform = scrapy.Field()  # 登录方式

    realname_verify_status = scrapy.Field()  # 实名验证状态
    is_block = scrapy.Field()  # 是否被锁
    custom_verify = scrapy.Field()  # 个人认证
    verify_info = scrapy.Field()  # 认证信息
    is_ad_fake = scrapy.Field()  # 是否是假广告？
    is_gov_media_vip = scrapy.Field()  # 是否是政府单位媒体
    is_verified = scrapy.Field()  # 是否验证过
    live_agreement = scrapy.Field()  # 合同？
    live_verify = scrapy.Field()  # 线下认证？
    enterprise_verify_reason = scrapy.Field()  # 企业认证原因
    commerce_user_level = scrapy.Field()  # 商务等级

    user_canceled = scrapy.Field()  #
    with_commerce_entry = scrapy.Field()  #
    with_dou_entry = scrapy.Field()  #
    with_douplus_entry = scrapy.Field()  #
    with_fusion_shop_entry = scrapy.Field()  #
    with_new_goods = scrapy.Field()  #
    with_shop_entry = scrapy.Field()  #
    need_recommend = scrapy.Field()  #
    room_id = scrapy.Field()  #
    special_lock = scrapy.Field()  #
    pytime = scrapy.Field()
