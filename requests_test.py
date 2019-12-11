import requests 
import json
import mysql.connector
from mysql.connector import Error
r = requests.get('https://fr.openfoodfacts.org/categorie/popcorn/1.json')


print(r)
# print(r.json)
test = json.loads(r.text)
# print(test)
# class Produits:
bdd={}
for product in test["products"]:
    # print(product["product_name"])
    # print(product["nutrition_grades"])
    # print(product["url"])
    bdd[product["product_name"]] = product["nutrition_grades"],product["url"]
    # bdd[product["product_name"]] = product["url"]
# print (bdd)

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='oc_projet_5_off',
                                         user='Julien',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")