#coding: utf-8
import mysql.connector
from random import randint

class Programm():
    def __init__(self,connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def main_program(self):
        print("1 - Quel aliment souhaitez-vous remplacer ? ")
        print("2 - Retrouver mes aliments substitués. ")
        choice = input('')
        if choice == '1' :
            self.replace_aliments()
        elif choice == '2' :
            self.disp_sub_aliments()
        else:
            pass

    def replace_aliments(self):
        self.choose_cat()
        if 1 <= self.choice_cat <= 10 :
            self.choice_cat = str(self.choice_cat)
            self.operation = ("SELECT * FROM `product` WHERE `category_id` ="+self.choice_cat +" ")
            self.cursor.execute(self.operation)
            record = self.cursor.fetchall()
            print(record)
            print("le nombre de produits est",self.cursor.rowcount)   
            for row in record:
                print("L'id du produit est : ",row[0])
                print("le nom du produit est :",row[1])
                print("le nutriscore est :",row[2])
                print("l'url est :",row[3])
                print("le magasin est :",row[4])
                print("l'id de la catégorie est :",row[5],'\n')
            self.choice_product = input("Quel produit choisissez vous?,saisir id ")
            self.choice_product = int(self.choice_product)
            if 1 <= self.choice_product <= 20 :
                self.operation = ("SELECT * FROM `product` WHERE `id` ="+ self.choice_product +" ")
                self.cursor.execute(self.operation)
                record = self.cursor.fetchall()
                print(record)
                print("le produit choisi à pour id",row[0])
                print("le nom du produit est :",row[1])
                print("le nutriscore est :",row[2])
                print("l'url est :",row[3])
                print("le magasin est :",row[4])
                print("l'id de la catégorie est :",row[5],'\n')
                random_product= randint(0,20)
                print(random_product)
                # self.operation = ("SELECT * FROM `product` WHERE `category_id` = 1 AND `id` = %s")
                # self.cursor.execute(self.operation,random_product)
                # record = self.cursor.fetchall()
                # print(record)
                    
            else: 
                pass
        else: 
            pass


    def choose_cat(self):
        self.operation = ("SELECT * FROM `category`")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        print(record)
        print("le nombre totale de categories est",self.cursor.rowcount)
        for row in record:
            print("L'id de la catégorie est : ",row[0])
            print("le nom de la catégorie est :",row[1])
        self.choice_cat = input("Quel catégorie voulez vous choisir : ")
        self.choice_cat = int(self.choice_cat)

    def disp_sub_aliments(self):
        self.operation = ("SELECT * FROM `substitut_product`")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        print("le nombre totale de produits substitué est",self.cursor.rowcount)
        for row in record:
            print("L'id du produit est : ",row[0])
            print("il est substitué de :",row[1],)
            print("il est substituant de :",row[2])