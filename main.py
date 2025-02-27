import os 
import mysql.connector
from dotenv import load_dotenv
from config import db_config


def main():
    # to access the env varibles for the database
    load_dotenv()
    MY_DB_VAL = os.getenv('DB_PORT')
    print(MY_DB_VAL)

    try:
        db = mysql.connector.connect(**db_config) #creates connection
    
        cursor = db.cursor()
        cursor.execute("SHOW TABLES") #decide on what cursor to do

        for table in cursor:
            print(table)

        cursor.close()

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')
    finally: #makes sure last thing func does is close connection
        if db.is_connected():
            db.close()
            print("Database connection closed.")
    
if __name__ == "__main__":
    main()