import mysql.connector
import pandas as pd
from mysql.connector import Error
import time


class Sql_connector:

    def __init__(self, cls):
        self.query = "SELECT * FROM axies_db.sales"
        self.makeQuery(cls)
        self.connection = None
        self.createConnection(
            "eu-cdbr-west-02.cleardb.net",
            "b18f253a60769a",
            "315c526d",
            "heroku_8ba8b98744212ea"
        )
        self.axies_from_sql = None
        self.getAxiesFromDatabase()

    def createConnection(self, host_name, user_name, user_password, db_name):
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

    def makeQuery(self, cls):
        if cls == '':
            self.query = f"SELECT * FROM axies_db.sales"
        else:
            self.query = f"SELECT * FROM axies_db.sales " \
                         f"AND class = '{cls}'"

    def getAxiesFromDatabase(self):
        try:
            print('Downloading axies from Database...')
            self.axies_from_sql = pd.read_sql(self.query, con=self.connection)
            print('Download completed!')
        except Error as e:
            print(f"The error '{e}' occurred")
            return None
