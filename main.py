from helpers.database import MysqlConnector


def main():
    db = MysqlConnector()._connector()
    cur = db.cursor()
    cur.execute("SELECT * from test;")
    print(cur.fetchall())
    db.close()


main()
