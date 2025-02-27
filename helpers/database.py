import mysql.connector
from config.db_config import db_config


class MysqlConnector:
    def _connector(self):
        try:
            return mysql.connector.connect(**db_config)
        except Exception as e:
            print(f'DB connection error: {e}')
            return None
