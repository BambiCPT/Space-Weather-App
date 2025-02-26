import os 
from dotenv import load_dotenv



def main():
    load_dotenv()
    MY_DB_VAL = os.getenv('DB_PORT')
    print(MY_DB_VAL)




main()