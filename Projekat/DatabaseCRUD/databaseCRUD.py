from Projekat.DatabaseCRUD.CRUDBrojila import CRUDBrojila
from Projekat.DatabaseCRUD.CRUDPotrosnjaBrojila import CrudPotrosnjaBrojila
from Projekat.DatabaseCRUD.AnaliticsReport import AnaliticsReport


class DatabaseCRUD:  #objedinjuje klae brojila i potrosnja brojila

    def __init__(self, localhost='127.0.0.1', name='admin', password='admin', db='RES_PROJEKAT'):
        self.crud_brojila = CRUDBrojila(localhost, name, password, db)  #u konstruktoru kreiran objekat klase crud brojila
        self.crud_potrosnja_brojila = CrudPotrosnjaBrojila(localhost, name, password, db) #potrosnja brojila
        self.analitics = AnaliticsReport(localhost, name, password, db)  #instanciramo klasu

    def get_brojilo(self, id_param):  #worker poziva, read
        return self.crud_brojila.read(id_param)  #iz crud brojila iscitaj mi sto je korisnik proslijedio

    def get_potrosnja_brojila(self, id_param, mesec_param):  #worker, read
        return self.crud_potrosnja_brojila.read(id_param, mesec_param)

    def insert(self, id_param, mesec_param, potrosnja_param):  #worker, insert
        return self.crud_potrosnja_brojila.insert(id_param, mesec_param, potrosnja_param)

    def get_potrosnja_po_gradu(self, grad_param):   #databaseAnalitics
        return self.analitics.potrosnja_po_gradu(grad_param)

    def get_potrosnja_po_brojilu(self, id_param):  #databaseAnalitics
        return self.analitics.potrosnja_po_brojilu(id_param)
