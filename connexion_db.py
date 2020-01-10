import mysql.connector
from mysql.connector import Error

class Access_to_data_base():
    def __init__(self):
        self.connection = None
        
    def open_data_base(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                database='a',
                                                user='Julien',
                                                password='')
            if self.connection.is_connected():
                self.db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", self.db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                self.record = self.cursor.fetchone()
                print("You're connected to database: ", self.record)

        except Error as e:
            print("Error while connecting to MySQL", e)
    def close_data_base(self):
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
                print("MySQL connection is closed")


            
