from scrapy import cmdline


cmdline.execute("scrapy crawl UserInfo".split())  # 爬取用户个人信息
# cmdline.execute("scrapy crawl FansList".split())  # 爬取粉丝列表
# cmdline.execute("scrapy crawl LikeList".split())  # 爬取关注列表
# cmdline.execute("scrapy crawl Post_Aweme_Info".split())  # 爬取发布抖音作品列表
# cmdline.execute("scrapy crawl Like_Aweme_Info".split())  # 爬取喜欢抖音作品列表
# cmdline.execute("scrapy crawl CommentInfo".split())  # 爬取抖音作品评论信息

