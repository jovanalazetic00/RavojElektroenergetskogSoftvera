from unittest import TestCase
import mysql.connector
from mysql.connector import errorcode

import sys
sys.path.append("../../")

from Projekat.DatabaseCRUD.CRUDBrojila import CRUDBrojila
from Projekat.DatabaseCRUD.CRUDPotrosnjaBrojila import CrudPotrosnjaBrojila
from Projekat.DatabaseCRUD.AnaliticsReport import AnaliticsReport


MYSQL_USER = "admin"
MYSQL_LOGIN = "admin"
MYSQL_DB = "test"   #RADIMO SA ISTOM konekcijom ali sa drugom bazom test, mok baza, koj apostoji za vrijeme testiranja nakon cega ce se izbrisati
MYSQL_HOST = "127.0.0.1"


class MockDB(TestCase):  #nasljedjuje klasu test case za testiranje

    @classmethod
    def setUpClass(cls):  #override metodaq iz test case klase
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_LOGIN,
        )
        cursor = cnx.cursor(dictionary=True)

        # drop database if it already exists
        try:
            cursor.execute("DROP DATABASE {}".format(MYSQL_DB))  #kreiramo bazu za testiranje
            cursor.close()
            print("DB dropped")
        except mysql.connector.Error as err:
            print("{}{}".format(MYSQL_DB, err))

        cursor = cnx.cursor(dictionary=True)
        try:
            cursor.execute(
                "CREATE DATABASE {}".format(MYSQL_DB))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)
        cnx.database = MYSQL_DB

        query = """                              #skripta za testiranje
                  CREATE TABLE `brojilo` (
                  `IdBrojila` INTEGER NOT NULL,
                  `Ime` VARCHAR(35) NOT NULL,
                  `Prezime` VARCHAR(35) NOT NULL,
                  `Ulica` VARCHAR(35) NOT NULL,
                  `Broj` INTEGER NOT NULL,
                  `PostanskiBroj` CHAR(5) NOT NULL,
                  `Grad` VARCHAR(30) NOT NULL,
                   CONSTRAINT `brojilo_PK` PRIMARY KEY (`IdBrojila`),
                   CONSTRAINT `brojilo_CK` CHECK (REGEXP_LIKE(`PostanskiBroj`, '[0-9]{5}')))
                """
        try:
            cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("'Brojilo' already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        insert_data_query = """       #crud brojilo za testiranje
                               INSERT INTO `brojilo` (`IdBrojila`,`Ime`,`Prezime`,`Ulica`,`Broj`, `PostanskiBroj`, `Grad`)
                               VALUES (1,"Janko","Jankovic","Vuka Karadzica",50,"21101", "Novi Sad"),
                                      (3,"Marko","Markovic","Karadjordjeva",11,"11000", "Beograd"),
                                      (7,"Zoran","Zoranovic","Politova",13,"21480", "Srbobran")
                            """
        cls.db1 = CRUDBrojila("127.0.0.1", "admin", "admin", "test")

        try:
            cursor.execute(insert_data_query)
            cnx.commit()
        except mysql.connector.Error as err:
            print("Data insertion to 'Brojilo' failed \n" + err.msg)

        query = """
                        CREATE TABLE `potrosnjaBrojila`(
                        `IdBrojila` INTEGER NOT NULL,
                        `Potrosnja` DOUBLE NOT NULL,
                        `Mesec` INTEGER NOT NULL,
                         CONSTRAINT `potrosnjaBrojila_PK` PRIMARY KEY (`IdBrojila`, `Mesec`),
                         CONSTRAINT `potrosnjaBrojila_FK` FOREIGN KEY (`IdBrojila`) REFERENCES brojilo(`IdBrojila`),
                         CONSTRAINT `potrosnjaBrojila_CK1` CHECK (`Mesec` > 0 and `Mesec` <= 12),
                         CONSTRAINT `potrosnjaBrojila_CK2` CHECK (`Potrosnja` >= 0)) 
                       """

        try:
            cursor.execute(query)
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("'potrosnjaBrojila' already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        insert_data_query = """       #u tabeli potrosnja brojila, za testiranje
                                INSERT INTO `potrosnjaBrojila` (`IdBrojila`,`Mesec`,`Potrosnja`)
                                VALUES (1, 2, 1000),
                                       (1, 3, 999),
                                       (3, 4, 555)
                                    """
        cls.db2 = CrudPotrosnjaBrojila("127.0.0.1", "admin", "admin", "test")
        cls.db3 = AnaliticsReport("127.0.0.1", "admin", "admin", "test")
        try:
            cursor.execute(insert_data_query)
            cnx.commit()
        except mysql.connector.Error as err:
            print("Data insertion to 'potrosnjaBrojila' failed \n" + err.msg)

        cls.test_tuple = (1, "Janko", "Jankovic", "Vuka Karadzica", 50, '21101', "Novi Sad")

        cursor.close()
        cnx.close()

    @classmethod
    def tearDownClass(cls):
        cnx = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_LOGIN
        )
        cursor = cnx.cursor(dictionary=True)

        # drop test database
        try:
            cursor.execute("DROP DATABASE {}".format(MYSQL_DB))
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Database {} does not exists. Dropping db failed".format(MYSQL_DB))
        cnx.close()
