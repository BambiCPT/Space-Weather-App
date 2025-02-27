from helpers.db_connector import DataBaseConnector


def main():
    db = DataBaseConnector()._mysql_connector()
    cur = db.cursor()
    cur.execute("SELECT * from test;")
    print(cur.fetchall())


main()
