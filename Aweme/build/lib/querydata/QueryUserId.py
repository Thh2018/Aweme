# coding=utf-8
from tools import DBHelper


class QueryUserId(object):
    def __init__(self):
        self.db_helper = DBHelper.DBHelper()

    def get_user_id(self):
        # 查询目标ID
        self.db_helper.connect_database()
        #query_sql = "SELECT UserId FROM user_id ORDER BY Id;"
        #query_sql = "SELECT user_uid FROM works_comment ORDER BY aweme_id"
        #query_sql = "SELECT uid FROM userinfo ORDER BY uid"

        # query_sql = "SELECT user_id FROM select_id ORDER BY id"
        # return self.db_helper.query_task(query_sql)
        # query_sql = "SELECT %s FROM select_id ORDER BY id"
        # params ="user_id"
        # return self.db_helper.query_task(query_sql,params)

        query_sql = "SELECT select_id FROM select_id ORDER BY id"
        return self.db_helper.query_task(query_sql)

if __name__ == '__main__':
    query = QueryUserId()
    print(query.get_user_id())
