# coding=utf-8
from tools import DBHelper


class QueryAwemeId(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_aweme_id(self):
        # 查询目标ID
        self.db_helper.connect_database()
        # query_sql = "SELECT aweme_id FROM works ORDER BY aweme_id"
        # return self.db_helper.query_task(query_sql)

        # query_sql = "SELECT %s FROM works ORDER BY aweme_id"
        # params = "aweme_id"
        # return self.db_helper.query_task(query_sql,params)
        query_sql = "SELECT aweme_id FROM works ORDER BY aweme_id"
        return self.db_helper.query_task(query_sql)





if __name__ == '__main__':
    query = QueryAwemeId()
    print(query.get_aweme_id())
