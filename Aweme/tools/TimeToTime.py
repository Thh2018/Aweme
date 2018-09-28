# coding = utf-8

import time


# 将时间戳转换为时间
def timestamp_to_localtime(timestamp):
    # 转换成localtime
    timestamp = int(timestamp)
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt

