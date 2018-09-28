import pymysql
from scrapy.utils.project import get_project_settings


class DBHelper(object):
    def __init__(self):
        self.settings = get_project_settings()

        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.password = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    def connect_database(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db,
                               charset='utf8')
        return conn

    def insert_task(self, sql, params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def query_task(self, sql, *params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results

    def query_fetchone_task(self, sql, params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        results = cur.fetchone()
        cur.close()
        conn.close()
        return results

    def update_task(self, sql, params):
        conn = self.connect_database()

        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()

    def delete_task(self, sql, params):
        conn = self.connect_database()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()


if __name__ == "__main__":
    db = DBHelper()
    sql = """SELECT * FROM rent_review  WHERE house_code = %s AND time = %s """  # AND `time` = %s
    params = ('107001292240', '2018-07-05')
    print(db.query_task(sql, params))
