# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 17:13
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : SpiderMapping.py
# @Software: PyCharm
import importlib


class SpiderMapping(object):
    def __init__(self, name):
        self.name = name

    def mapping(self, item):
        try:
            house_details_lib = importlib.import_module('models.dynamicdata.' + self.name)
            house_details = house_details_lib.HouseDetails(item)
            return house_details
        except Exception as e:
            print(e)


if "__main__" == __name__:
    Spider = SpiderMapping()
    print(Spider.mapping())
