import mysql.connector
from helpers.mappers import PlanetaryKIndex, SolarProbability, XRayFlare
from config.db_config import db_config


class MySqlConnector:
    def _connector(self):
        try:
            return mysql.connector.connect(**db_config)
        except Exception as e:
            print(f'DB connection error: {e}')
            return None

    def insert_data(self, table_name: str, data: dict):
        if isinstance(data, dict):
            data = [data]

        try:
            connection = self._connector()
            if not connection:
                return ("Failed to connect to database")

            cursor = connection.cursor()
            count = 0

            for item in data:
                if isinstance(item, PlanetaryKIndex):
                    sql = f"INSERT INTO {table_name} (kp, estimated_kp, time) VALUES (%s, %s, %s)"
                    values = (item.kp, item.estimated_kp, item.time)
                elif isinstance(item, SolarProbability):
                    sql = f"INSERT INTO {table_name} (class_c_1_day, class_c_2_day, class_c_3_day, class_m_1_day, class_m_2_day, class_m_3_day, class_x_1_day, class_x_2_day, class_x_3_day, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (item.class_c_1_day, item.class_c_2_day, item.class_c_3_day, item.class_m_1_day, item.class_m_2_day,
                              item.class_m_3_day, item.class_x_1_day, item.class_x_2_day, item.class_x_3_day, item.time)
                elif isinstance(item, XRayFlare):
                    sql = f"INSERT INTO {table_name} (begin_time, end_time, max_class_time, class) VALUES (%s, %s, %s, %s)"
                    values = (item.begin_time, item.end_time,
                              item.max_class_time, item.max_class)
                else:
                    continue

                cursor.execute(sql, values)
                count += cursor.rowcount

            connection.commit()

            num_items = "item" if count == 1 else "items"
            return f"Successfully inserted {count} {num_items} into {table_name}"

        except mysql.connector.Error as e:
            if connection:
                connection.rollback()
            return (f"Error inserting data: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_by_id(self, table_name: str, id_num: int):
        try:
            connection = self._connector()
            if not connection:
                return ("Failed to connect to database")

            cursor = connection.cursor()

            if not table_name.isidentifier():
                return f"Invalid table name: {table_name}"

            sql = (f"SELECT * from {table_name} where id = %s")

            cursor.execute(sql, (id_num,))
            result = cursor.fetchone()

            if result:
                columns = [desc[0] for desc in cursor.description]
                formatted_result = "\n".join(f"{col}: {val}" for col, val in zip(
                    columns, result))  # yes i used AI for this

                return f"Successfully selected id: {id_num} from the {table_name}:\n{formatted_result}"
            return f"No record found with id: {id_num} from the table {table_name}"

        except mysql.connector.Error as e:
            if connection:
                connection.rollback()
            return f"Error selecting id: {id_num}: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
