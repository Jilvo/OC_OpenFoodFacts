import requests 
import json
import mysql.connector

class Get_data():

    def __init__(self,file,connection):
        self.file = file
        self.connection = connection
        self.cursor = connection.cursor()
        self.increm_cat = 1
        self.increm_product = 1
        self.category_id = 0
        self.nutrition_product = 0
        self.category_id = self.increm_cat
        self.number_of_product = 0
    def access_to_api(self):
        with open('list_category.txt') as file:
            for line in file.readlines():
                r = requests.get('https://fr.openfoodfacts.org/categorie/'+line+'/1.json')
                test = json.loads(r.text)
                self.cat = (self.increm_cat,line)
                self.operation = ("INSERT INTO `category`(`id`, `name`) VALUES (%s,%s)")
                self.cursor.execute(self.operation,self.cat)
                self.increm_cat= self.increm_cat +1
                self.connection.commit()
                for product in test["products"]:
                    # print(product["url"])
                    if product.get("nutrition_grades",False):
                        if product.get("stores",False):
                            self.product = (self.increm_product,product["product_name"],product["nutrition_grades"],product["url"],product["stores"],self.category_id)
                            self.operation = ("INSERT INTO `product`(`id`, `name`, `nutriscore`, `url`, `store`, `category_id`) VALUES (%s,%s,%s,%s,%s,%s)")
                            self.cursor.execute(self.operation,self.product)
                            self.increm_product= self.increm_product +1
                            self.connection.commit()
                            print(product["nutrition_grades"])
                            # if product.get("stores",False):
                            #     print(product["stores"])
