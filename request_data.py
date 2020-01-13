""" V1.0--request_data imported OFF's API data to database"""
import json
import requests

class Getdata():
    """ This class is created for import and push data"""
    def __init__(self, file, connection):
        """ init variables """
        self.file = file
        self.connection = connection
        self.cursor = connection.cursor()
        self.increm_cat = 1
        self.increm_product = 1
        self.category_id = 0
        self.increm_cat = 1
        self.number_of_product = 0
        self.page_product = 1
        self.operation = None
        self.cat = None
        self.product = None

    def find_if_db_is_empty(self):
        """ when we lunch the main file, this fonction check if the database is empty to fill in """
        self.operation = ("SELECT * FROM `product` ")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        # print(record)
        if self.cursor.rowcount <= 10:
            self.fill_in_db()
    def fill_in_db(self):
        """ This fonction fill the db """
        with open('list_category.txt') as file:
            for line in file.readlines():
                self.operation = ("INSERT INTO `category`(`id`, `name`) VALUES (%s,%s)")
                self.cat = (self.increm_cat, line)
                self.cursor.execute(self.operation, self.cat)
                self.connection.commit()
                self.increm_cat += 1
                self.category_id += 1
                self.page_product = 1
                self.number_of_product = 0
                while self.number_of_product < 20:
                    request_to_api = requests.get('https://fr.openfoodfacts.org/categorie/'\
                        + line + \
                        '/' + str(self.page_product) + '.json')
                    test = json.loads(request_to_api.text)
                    for product in test["products"]:
                        if product.get("nutrition_grades", False) and product.get("stores", False):
                            self.product = (self.increm_product, \
                                product["product_name"],\
                                product["nutrition_grades"], product["url"],\
                                product["stores"], self.category_id)
                            self.operation = ("INSERT INTO `product`(`id`, `name`,\
                                `nutriscore`, `url`,`store`, \
                                `category_id`) VALUES (%s,%s,%s,%s,%s,%s)")
                            self.cursor.execute(self.operation, self.product)
                            self.increm_product = self.increm_product + 1
                            self.connection.commit()
                            self.number_of_product += 1
                            # print(self.number_of_product)
                        if self.number_of_product >= 20:
                            break
                    self.page_product += 1
