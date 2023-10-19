from Projekat.DatabaseCRUD.CRUDAbstract import CRUD
from mysql.connector import connect, Error


class CRUDBrojila(CRUD):  #nasljedjuje klasu CRUD, i vrsi implementaciju metoda za tabelu CRUD BROJILA

    def __init__(self, host, user, password, database):  #konstruktor, prosljedjumeo host-gdje se nalazi baza, korisnik admin, sifra dmin, baza je res tim 21
        self.host = host   #postavljamo atribute
        self.user = user
        self.password = password
        self.database = database

    def insert(self, *args):
        if len(args) > 7:
            return -5

        _id = args[0]  #atributi tabele brojilo
        _ime = args[1]
        _prezime = args[2]
        _ulica = args[3]
        _broj = args[4]
        _postanskiBroj = args[5]
        _grad = args[6]

        try:
            with connect(   #with koristimo kao using, da sam zatvori konekciju kad zavrsi posao
                    host=self.host,  #konektuj me na parametre koje smo dobili pomocu konstruktora
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:  #vrati mi konekciju kao parametar koneksn
                query = """INSERT INTO brojilo (IdBrojila, Ime, Prezime, Ulica, Broj, PostanskiBroj, Grad)   #upit pisem, sta treba da izvrsim
                                   VALUES (?, ?, ?, ?, ?, ?, ?);"""  #zastita od sql napada
                with connecting.cursor(prepared=True) as cursor:  #postavi konekciju, postavi kursor da je pripremljen upit, vrati mi kao kursor
                    parameter = (_id, _ime, _prezime, _ulica, _broj, _postanskiBroj, _grad) #kazemo koji su to parametri, kreiramo ih kao tapl
                    cursor.execute(query, parameter)  #pomocu kursora izvrsi upit sa tim parametrima
                    connecting.commit()  #komituj u bazu
                    return cursor.rowcount  #vracam broj redova, koliko je redova promijenjeno u tabeli
        except Error as e:
            return e.errno  #ako se desio izuzetak, vracam broj errora

    def delete(self, *args):
        if len(args) > 1:
            return -5
        _id = args[0]  #kad brisem bitan id samo

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """DELETE FROM brojilo WHERE IdBrojila=(?)"""
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id,)  #kad imam jedan parametar stavljam ,
                    cursor.execute(query, parameter)  #izvrsava upit sa tim parametrima
                    connecting.commit()  #komitujem izmjenu
                    return cursor.rowcount
        except Error as e:
            return e.errno

    def update(self, *args):
        if len(args) > 7:
            return -5
        _id = args[0]  #dobavljamo sve parametre
        _ime = args[1]
        _prezime = args[2]
        _ulica = args[3]
        _broj = args[4]
        _postanskiBroj = args[5]
        _grad = args[6]

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """UPDATE brojilo SET Ime=(?), Prezime=(?), Ulica=(?), Broj=(?), PostanskiBroj=(?), Grad=(?)
                                   WHERE IdBrojila=(?);"""  #id se ne mijenja
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_ime, _prezime, _ulica, _broj, _postanskiBroj, _grad, _id)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return cursor.rowcount
        except Error as e:
            return e.errno

    def read(self, *args):
        if len(args) > 1:
            return -5
        _id = args[0]  #citam brojilo sa nekim id-em
        try:
            with connect(   #konekcija
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = f"SELECT * FROM brojilo p where p.IdBrojila = %s;"  #kreiram upit
                with connecting.cursor(prepared=True) as cursor:
                    cursor.execute(query, (_id,))
                    result = cursor.fetchall()  #vracam sve dobavljene sa tim id-em
                    return result  #vracam torku iz tabele
        except Error as e:
            return e.errno
