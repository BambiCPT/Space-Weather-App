from enum import Enum
import mysql.connector
from config.db_config import db_config


class TableEnum(Enum):
    PLANETARY_KP: str = "planetary_kp_indices"
    SOLAR_FLARE: str = "solar_flares"
    SOLAR_FLARE_PROBABILITY: str = "solar_flare_probability"


QUERY_STRINGS = {
    "planetary_kp_indices": "(kp, estimated_kp, time) VALUES (%s, %s, %s)",
    "solar_flare_probability": "(class_c_1_day, class_c_2_day, class_c_3_day, class_m_1_day, class_m_2_day, class_m_3_day, class_x_1_day, class_x_2_day, class_x_3_day, time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    "solar_flares": "(begin_time, end_time, max_class_time, class) VALUES (%s, %s, %s, %s)"
}


class MySqlConnector:
    def _connector(self):
        try:
            return mysql.connector.connect(**db_config)
        except Exception as e:
            print(f'DB connection error: {e}')
            return None

    def insert_data(self, table_name: TableEnum, data: dict) -> str:
        if isinstance(data, dict):
            data = [data]

        try:
            connection = self._connector()
            cursor = connection.cursor()
            count = 0

            for item in data:
                values = []
                for val in item.__dict__.values():
                    values.append(val)

                sql = f"INSERT INTO {table_name.value} {QUERY_STRINGS[table_name.value]}"
                cursor.execute(sql, values)
                count += cursor.rowcount

            connection.commit()
            num_items = "item" if count == 1 else "items"
            return f"Successfully inserted {count} {num_items} into {table_name}"

        except mysql.connector.Error as e:
            if connection:
                connection.rollback()
            return print(f"Error inserting data: {str(e)}")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_by_id(self, table_name: TableEnum, id_num: int) -> str:
        try:
            connection = self._connector()

            cursor = connection.cursor(dictionary=True)

            sql = (f"SELECT * FROM {table_name} WHERE id = %s")

            cursor.execute(sql, (id_num,))
            result = cursor.fetchone()

            if result:
                return f"Successfully selected id: {id_num} from the {table_name}:\n{result}"
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

    def get_all(self, table_name: TableEnum) -> str:
        try:
            connection = self._connector()

            cursor = connection.cursor(dictionary=True)

            sql = (f"SELECT * FROM {table_name} ORDER BY id")
            cursor.execute(sql)

            results = cursor.fetchall()

            if results:
                return results

        except mysql.connector.Error as e:
            if connection:
                connection.rollback()
            return f"Error selecting records from {table_name}: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def update_by_id(self, table_name: TableEnum, id_num: int, new_data: object) -> str:
        try:
            connection = self._connector()

            cursor = connection.cursor()

            data_dict = vars(new_data)
            if "created_at" in data_dict:
                data_dict.pop("created_at")

            if not data_dict:
                return "No valid fields to update"

            columns = [f"{key} = %s" for key in data_dict.keys()]
            sql = (
                f"UPDATE {table_name} SET {', '.join(columns)} WHERE id = %s")
            values = tuple(data_dict.values()) + (id_num,)

            cursor.execute(sql, values)
            affected_rows = cursor.rowcount

            connection.commit()

            num_items = "record" if affected_rows == 1 else "records"
            return f"Successfully updated {affected_rows} {num_items} in {table_name}"

        except mysql.connector.Error as e:
            if connection:
                connection.rollback()
            return f"Error updating id: {id_num}: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def delete_by_id(self, table_name: TableEnum, id_num: int) -> str:
        try:
            connection = self._connector()

            cursor = connection.cursor()
            count = 0

            sql = (f"DELETE FROM {table_name} WHERE id = %s")

            cursor.execute(sql, (id_num,))
            count += cursor.rowcount

            connection.commit()

            num_items = "item" if count == 1 else "items"
            return f"Successfully deleted {count} {num_items} from {table_name}"

        except mysql.connector.Error as e:
            if connection:
                connection.rollback()
            return f"Error deleting id: {id_num}: {str(e)}"
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
