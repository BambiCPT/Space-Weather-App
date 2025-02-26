import os 
from dotenv import load_dotenv



def main():
    # to access the env varibles for the database
    load_dotenv()
    MY_DB_VAL = os.getenv('DB_PORT')
    print(MY_DB_VAL)


main()