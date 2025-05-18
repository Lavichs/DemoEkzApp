import pymysql

from pymysql.constants import CLIENT


class Database:


    database_cred = {

        "host": "localhost",

        "user": "root",

        "password": "root",

        "database": "dem_DB",

        "autocommit": True,  # making sure updated, inserts, deletions are commited for every query

        "cursorclass": pymysql.cursors.DictCursor,

    }


    def __init__(self, database_cred: dict = None):

        if database_cred:

            self.conn = pymysql.connect(**database_cred)

        else:

            self.conn = pymysql.connect(**self.database_cred)

        # end if


    def run_qry(self, sql: str):

        # to check DB Connection pin the instance

        self.conn.ping()

        with self.conn.cursor() as cursor:

            cursor.execute(sql)

            self.conn.commit()

            result = cursor.fetchall()

        # end with

        return result


    def run_multiple_queries(self, sql_statements: list[str]):

        if len(sql_statements) == 1:

            result = self.run_qry(sql_statements[0])

            return result


        new_db_cred = {"client_flag": CLIENT.MULTI_STATEMENTS, **self.database_cred}

        sql_statements = ";".join(sql_statements)


        sql_connetion = pymysql.connect(**new_db_cred)

        # to check DB Connection pin the instance

        sql_connetion.ping()

        with sql_connetion.cursor() as cursor:

            affected_rows = cursor.execute(sql_statements)

            self.conn.commit()

            result = cursor.fetchall()

        return result
# end class

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="dem_DB",
    charset="utf8mb4"
)
# cursor = conn.cursor()
# q = "SELECT * FROM partners"
# cursor.execute(q)
# rows = cursor.fetchall()
# # print(rows)
# for row in rows:
#     print(row)

# dtb = Database()
# print(dtb.run_qry("SELECT * FROM partners"))
