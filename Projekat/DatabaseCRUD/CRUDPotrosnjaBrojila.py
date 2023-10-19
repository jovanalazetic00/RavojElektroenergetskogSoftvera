from Projekat.DatabaseCRUD.CRUDAbstract import CRUD
from mysql.connector import connect, Error


class CrudPotrosnjaBrojila(CRUD):

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def read(self, *args):
        if len(args) > 2:
            return -5
        _id = args[0]
        _mesec = args[1]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = f"SELECT * FROM potrosnjaBrojila pb where pb.IdBrojila = %s and pb.Mesec = %s;"
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id, _mesec)
                    cursor.execute(query, parameter)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            return e.errno

    def insert(self, *args):
        if len(args) > 3:
            return -5
        _id = args[0]
        _mesec = args[1]
        _potrosnja = args[2]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = f"INSERT INTO potrosnjaBrojila (IdBrojila, Potrosnja, Mesec) VALUES (?, ?, ?);"
                with connecting.cursor(prepared=True) as cursor:  #prepared=true zastita od napada
                    parameter = (_id, _potrosnja, _mesec)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return cursor.rowcount
        except Error as e:
            return e.errno

    def delete(self, *args):
        if len(args) > 2:
            return -5
        _id = args[0]
        _mesec = args[1]

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """DELETE FROM potrosnjaBrojila WHERE IdBrojila=(?) and Mesec=(?)"""
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id, _mesec)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return cursor.rowcount
        except Error as e:
            print(e)

    def update(self, *args):
        if len(args) > 3:
            return -5
        _id = args[0]
        _potrosnja = args[1]
        _mesec = args[2]

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """UPDATE potrosnjaBrojila SET Potrosnja=(?)
                                           WHERE IdBrojila=(?) and Mesec=(?);"""
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_potrosnja, _id, _mesec)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return cursor.rowcount
        except Error as e:
            print(e)
