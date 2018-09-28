# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 11:52
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : Encrypt.py
# @Software: PyCharm
import time
import json
import requests
import hashlib
from urllib.parse import urlparse, parse_qs, urlencode


def get_aweme_token(url):
    timestamp = time.time()
    token_url = "http://47.97.186.56:4570/getascpmas41d8224167374f85994185cd7d68be88"
    parse_param = parse_qs(urlparse(url).query, keep_blank_values=True)
    data = {key: value[-1] for key, value in parse_param.items()}
    data.pop("mas")
    data.pop("cp")
    data.pop("as")
    data["_rticket"] = str(round(timestamp * 1000))
    data["ts"] = str(int(timestamp))
    ts_short = (str(int(timestamp)) + "504c53f18b834e8b9b853cc64628cd12").encode()
    param = {"dic": data, "device_id": data["device_id"], "ts_short": int(timestamp),
             "mykey": hashlib.md5(ts_short).hexdigest()}
    token = requests.post(token_url, data=json.dumps(param)).json()
    data["as"] = token["As"]
    data["mas"] = token["Mas"]
    data["cp"] = token["Cp"]
    return url.split("?")[0] + "?" + urlencode(data)


if __name__ in "__main__":
    # url = "https://aweme.snssdk.com/aweme/v1/user/follower/list/?user_id=84064249580&max_time=1537196762&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=ALP-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024*576&dpi=192&update_version_code=1832&_rticket=1536744989405&ts=1536744990&as=a1a5dde97e81fbfea84355&cp=d31aba58ec819ee6e1McUg&mas=00a8422d39d7eb28de04f7adaffd1292f0acaccc2c1c86a6664666"
    url = "https://aweme.snssdk.com/v1/user/follower/list/?user_id=84064249580&max_time=1537196762&count=20&retry_type=no_retry&iid=43398130756&device_id=57259297041&ac=wifi&channel=aweGW&aid=1128&app_name=aweme&version_code=183&version_name=1.8.3&device_platform=android&ssmix=a&device_type=ALP-AL00&device_brand=HUAWEI&language=zh&os_api=23&os_version=6.0.1&uuid=008796758836908&openudid=14c5f0e306271ae&manifest_version_code=183&resolution=1024%2A576&dpi=192&update_version_code=1832&_rticket=1537197039358&ts=1537197039&as=a1c56c697faedbb31f4355&mas=00c24f6eb91ef4b58c459932b5f931ecd8acaccc2c668ccc464626&cp=c7edb95ef8fe943ae1MiKa"
    print(get_aweme_token(url))
