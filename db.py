import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class MySQLDatabase:
    def __init__(self):
        self.config = {
            "host": os.getenv("HOST"),
            "user": os.getenv("USER"),
            "password": os.getenv("PASSWORD"),
            "database": os.getenv("DB")
        }

    def return_connection(self):
        return mysql.connector.connect(**self.config)
