""" V1.0--request_data imported OFF's API data to database"""
import mysql.connector
from mysql.connector import Error

class Fill():
    """ This class is created for connect the programm to db """
    def __init__(self):
        """ init variables """
        self.connection = None
        self.cursor = None
        self.record = None
        self.db_info = None
        self.database_info = None

    def open_data_base(self):
        "fonction for open the connexion"
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      database='oc_projet_5_off',
                                                      user='root',
                                                      password='')
            if self.connection.is_connected():
                self.database_info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", self.database_info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                self.record = self.cursor.fetchone()
                print("You're connected to database: ", self.record)

        except Error as error_db:
            print("Error while connecting to MySQL", error_db)
    def close_data_base(self):
        "fonction for close the connexion"
        if self.connection.is_connected:
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
