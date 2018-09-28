# coding=utf-8

"""
    1.导入Flask扩展
    2.创建Flask应用程序实例
    3.定义路由及视图函数
    4.启动程序
"""
from flask import Flask

from Aweme import run

app = Flask(__name__)


@app.route('/')
def start():
    run.run()


if __name__ == '__main__':
    app.run()
