import os
from dotenv import load_dotenv
import mysql.connector

SQL_CREATE_SOLAR_FLARE_PROBABILITY = """
CREATE TABLE solar_flare_probability (
    id INT AUTO_INCREMENT PRIMARY KEY,
    class_c_1_day INT,
    class_c_2_day INT,
    class_c_3_day INT,
    class_m_1_day INT,
    class_m_2_day INT,
    class_m_3_day INT,
    class_x_1_day INT,
    class_x_2_day INT,
    class_x_3_day INT,
    time TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""

SQL_CREATE_PLANETARY_KP_INDICES = """
CREATE TABLE planetary_kp_indices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kp CHAR(2),
    estimated_kp FLOAT,
    time DATETIME NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""

SQL_CREATE_SOLAR_FLARES = """
CREATE TABLE solar_flares (
    id INT AUTO_INCREMENT PRIMARY KEY,
    begin_time TIMESTAMP NULL,
    end_time TIMESTAMP NULL,
    max_class_time TIMESTAMP NULL,
    class VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""


def main():
    load_dotenv()
    db_config_without_db_name = {
        'host': os.getenv("DB_HOST"),
        'port': os.getenv("DB_PORT"),
        'user': os.getenv("DB_USER"),
        'password': os.getenv("DB_PASSWORD")
    }

    try:
        db = mysql.connector.connect(**db_config_without_db_name)
        cur = db.cursor()
        cur.execute("DROP DATABASE IF EXISTS space_weather;")
        cur.execute(f"CREATE DATABASE {os.getenv("DB_NAME")};")
        db.database = os.getenv("DB_NAME")
        cur.execute(SQL_CREATE_SOLAR_FLARE_PROBABILITY)
        cur.execute(SQL_CREATE_PLANETARY_KP_INDICES)
        cur.execute(SQL_CREATE_SOLAR_FLARES)

    except Exception as e:
        print(f'DB connection error: {e}')
    finally:
        db.close()


main()
