# coding = utf-8


# 作品列表信息
import scrapy


class AwemeInfoItem(scrapy.Item):
    author_user_id = scrapy.Field()  # 作者ID
    aweme_id = scrapy.Field()  # 作品ID
    aweme_type = scrapy.Field()  # 作品类型
    create_time = scrapy.Field()  # 创建时间
    duration = scrapy.Field()  # 持续时间
    des = scrapy.Field()  # 作品描述
    digg_count = scrapy.Field()  # 点赞数
    comment_count = scrapy.Field()  # 评论数
    share_count = scrapy.Field()  # 转发数

    is_ads = scrapy.Field()  # 是否是广告
    is_fantasy = scrapy.Field()
    is_hash_tag = scrapy.Field()
    is_pgcshow = scrapy.Field()  # 是否为pgc显示
    is_relieve = scrapy.Field()
    is_top = scrapy.Field()  # 是否置顶
    is_vr = scrapy.Field()  # 是否是VR视频
    item_comment_settings = scrapy.Field()  # 评论设置
    prevent_download = scrapy.Field()  # 是否禁止下载
    rate = scrapy.Field()  # 比率
    region = scrapy.Field()  # 区域
    share_url = scrapy.Field()  # 分享链接
    sort_label = scrapy.Field()  # 分类标签

    # 背景音乐信息
    # album = scrapy.Field()  # 音乐专辑
    owner_nickname = scrapy.Field()  # 音乐作者
    title = scrapy.Field()  # 背景音乐名称
    author = scrapy.Field()  # 背景音乐作者
    is_del_video = scrapy.Field()  # 作者是否删除
    collect_stat = scrapy.Field()  # 值为0
    cover_hd = scrapy.Field()  # 封面高清图片地址
    cover_large = scrapy.Field()  # 封面大图地址
    cover_medium = scrapy.Field()  # 封面中图地址
    cover_thumb = scrapy.Field()  # 封面小图地址
    is_original = scrapy.Field()  # 是否为原创
    music_id = scrapy.Field()  # 音乐ID
    is_restricted = scrapy.Field()  # 是否保密
    is_video_self_see = scrapy.Field()  # 是否只有自己可看
    mid = scrapy.Field()  # mid
    owner_handle = scrapy.Field()  # 作者自定义ID
    owner_id = scrapy.Field()  # 作者ID
    offline_desc = scrapy.Field()  # 线下描述
    play_url = scrapy.Field()  # 音乐播放地址
    source_platform = scrapy.Field()  # 来源平台？
    status = scrapy.Field()  # 状态
    user_count = scrapy.Field()  # 使用数量
    redirect = scrapy.Field()  # 是否重定向
    video_labels = scrapy.Field()  # 视频标签
    audio_track = scrapy.Field()  # 音轨地址

    # 视频信息
    bit_rate = scrapy.Field()  # 比特率
    height = scrapy.Field()  # 视频高度
    width = scrapy.Field()  # 视频宽度
    origin_cover = scrapy.Field()  # 原始封面
    has_watermark = scrapy.Field()  # 有无水印
    ratio = scrapy.Field()  # 清晰度
    play_addr_url = scrapy.Field()  # 视频播放url
    play_addr_uri = scrapy.Field()  # 视频播放uri
    url_key = scrapy.Field()  # 视频key
    download_addr = scrapy.Field()  # 视频下载地址
    dynamic_cover = scrapy.Field()  # 动态封面

    # 风险信息
    content = scrapy.Field()
    risk_sink = scrapy.Field()
    type = scrapy.Field()
    warn = scrapy.Field()
    vote = scrapy.Field()

    pytime = scrapy.Field()
