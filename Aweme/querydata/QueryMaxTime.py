# coding = utf-8

# coding=utf-8
from tools import DBHelper


class QueryMaxTime(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_max_time(self):
        # 查询max_time最大值
        self.db_helper.connect_database()
        query_sql = "SELECT MAX(max_time) FROM userinfo_fans_id"
        return self.db_helper.query_task(query_sql)


if __name__ == '__main__':
    query = QueryMaxTime()
    a = query.get_max_time()
    print(a[0][0])
