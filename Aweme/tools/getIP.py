from Aweme.proxypool.db import RedisClient


def get_peoxy():
    # 连接redis数据库
    db = RedisClient()
    # 随机获取一个代理IP
    proxy = db.random()
    return proxy


if __name__ == '__main__':
    a = get_peoxy()
    print(a)
