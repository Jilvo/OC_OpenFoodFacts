#coding: utf-8
import mysql.connector
from random import randint

class Programm():
    def __init__(self,connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.drap = 0

    def main_program(self):
        while self.drap == 0:
            print("1 - Quel aliment souhaitez-vous remplacer ? ")
            print("2 - Retrouver mes aliments substitués. ")
            choice = input('')
            if choice == '1' :
                self.replace_aliments()
                self.drap +=1
            elif choice == '2' :
                self.disp_sub_aliments()
                self.drap +=1
            else:
                pass

    def replace_aliments(self):
        self.choose_cat()
        self.drap = 0
        while self.drap == 0:
            self.choice_cat = input("Quel catégorie voulez vous choisir : ")
            if 1 <= int(self.choice_cat) <= 10 :
                self.choose_product()
                self.drap +=1
            else:
                pass
        self.drap = 0
        while self.drap == 0:
            self.choice_product = input("Quel produit choisissez vous?,saisir id ")
            if 1+(20*(int(self.choice_cat)-1)) <= int(self.choice_product) <= 20+(20*(int(self.choice_cat)-1)) :
                self.choose_random()
                self.drap +=1
            else: 
                pass
        self.drap = 0
        while self.drap == 0:
            self.choice_random = input("Voulez-vous enregister le produit dans la base de données ? Y/N ")
            # self.drap +=1
            if self.choice_random == "Y":
                self.choice_random_yes()
                self.drap +=1
            elif self.choice_random == "N" :
                print("Le produit n'est pas enregistré, nous allons vous montrer la liste des produits substitué")
                self.disp_sub_aliments()
                self.drap +=1


    def choose_cat(self):
        self.operation = ("SELECT * FROM `category`")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        print(record)
        print("le nombre totale de categories est",self.cursor.rowcount)
        for row in record:
            print("L'id de la catégorie est : ",row[0])
            print("le nom de la catégorie est :",row[1])

    def choose_product(self):
        self.choice_cat = str(self.choice_cat)
        self.operation = ("SELECT * FROM `product` WHERE `category_id` ="+self.choice_cat +" ")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        # print(record)
        print("le nombre de produits est",self.cursor.rowcount)   
        for row in record:
            print("L'id du produit est : ",row[0])
            print("le nom du produit est :",row[1])
            print("le nutriscore est :",row[2])
            print("l'url est :",row[3])
            print("le magasin est :",row[4])
            print("l'id de la catégorie est :",row[5],'\n')

    def choose_random(self):
        self.operation = ("SELECT * FROM `product` WHERE `id` ="+ str(self.choice_product) +" ")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        print(record)
        for row in record:
            print("le produit choisi à pour id",row[0])
            print("le nom du produit est :",row[1])
            print("le nutriscore est :",row[2])
            print("l'url est :",row[3])
            print("le magasin est :",row[4])
            print("l'id de la catégorie est :",row[5],'\n')
        self.random_product= randint(1+(20*(int(self.choice_cat)-1)),20+(20*(int(self.choice_cat)-1)))
        print(self.random_product)
        self.operation = ("SELECT * FROM `product` WHERE `category_id` = " +str(self.choice_cat) +" AND `id` = "+ str(self.random_product) +" ")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        print(record)
        for row in record:
            print("le substituant choisi à pour id",row[0])
            print("le nom du substituant est :",row[1])
            print("le nutriscore est :",row[2])
            print("l'url est :",row[3])
            print("le magasin est :",row[4])
            print("l'id de la catégorie est :",row[5],'\n')
        

    def choice_random_yes(self):
        self.operation = ("INSERT INTO `substitut_product`(`sub_from`, `sub_to`) VALUES (%s,%s)")
        self.cat = (self.choice_product,self.random_product)
        self.cursor.execute(self.operation,self.cat)
        self.connection.commit()
        # record = self.cursor.fetchall()
        # print(record)
        # print("le nombre total de produit substitué est",self.cursor.rowcount)
        # for row in record:
        #     print("L'id est : ",row[0])
        #     print("Il est substitué du :",row[1])
        #     print("Il est substituant du :",row[1])

    def disp_sub_aliments(self):
        self.operation = ("SELECT * FROM `substitut_product`")
        self.cursor.execute(self.operation)
        record = self.cursor.fetchall()
        print("le nombre totale de produits substitué est",self.cursor.rowcount)
        for row in record:
            print("L'id du produit est : ",row[0])
            a = row[1]
            b = row[2]
            # print("il est substitué de :",row[1],)
            self.operation = ("SELECT * FROM `product` WHERE `id` = " + str(a) + " ")
            self.cursor.execute(self.operation)
            record = self.cursor.fetchall()
            for row in record:
                print("le substituant choisi à pour id",row[0])
                print("le nom du substituant est :",row[1])
                print("le nutriscore est :",row[2])
                print("l'url est :",row[3])
                print("le magasin est :",row[4])
                print("l'id de la catégorie est :",row[5],'\n')
            # print("il est substituant de :",row[2])
            self.operation = ("SELECT * FROM `product` WHERE `id` = " + str(b) + " ")
            self.cursor.execute(self.operation)
            record = self.cursor.fetchall()
            for row in record:
                print("le substitué choisi à pour id",row[0])
                print("le nom du substitué est :",row[1])
                print("le nutriscore est :",row[2])
                print("l'url est :",row[3])
                print("le magasin est :",row[4])
                print("l'id de la catégorie est :",row[5],'\n')