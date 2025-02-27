import os 
import mysql.connector
from dotenv import load_dotenv
from config import db_config


def main():
    load_dotenv()

    try:
        db = mysql.connector.connect(**db_config) #creates connection
        if db.is_connected():
            print("Database connection successful!")
    
        cursor = db.cursor()
        cursor.execute("SHOW TABLES") #decide on what cursor to do

        for table in cursor:
            print(table)

    except Exception as e:
        print(f'Something went wrong: {e}')
    finally: 
        if cursor != None:
            cursor.close() #closes cursor
        if db.is_connected():
            db.close() #closes connection
            print("Database connection closed.")
    
if __name__ == "__main__":
    main()