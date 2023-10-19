from Scripts.Parser import Parser
from Scripts.Report import Report
from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class AnaliticsUI:

    def __init__(self):
        self.db = DatabaseCRUD()

    def Options(self):
        print('1. Mesecna potrosnja brojila po gradovima')  #opcije
        print('2. Mesecna potrosnja po brojilu')
        print('3. Izlaz')

    def Handle(self, option):  #kao kod writera
        _ret_val = True
        if option == '1':
            print("Grad: ")
            _grad = input()  #kad unesemo grad
            _result = self.db.get_potrosnja_po_gradu(_grad)  #dobijemo potrosnju po gradu
            _result = Parser.parsiranje_po_gradovima(_result) #proslijedimo parsiranje po gradovima
            if _result:  #ako vraca rez
                Report.prikazi_potrosnju_po_gradovima(_result)  #pozivamo metodu repost potrosnja po gradovima
            else:
                print("Ne postoji izvestaj za zadati grad!")
        elif option == '2':
            print("ID brojila: ")
            _id = input()
            _result = self.db.get_potrosnja_po_brojilu(_id)
            _result = Parser.parsiranje_po_brojilima(_result)
            if _result:
                Report.prikaz_potrosnje_po_brojilu(_result)
            else:
                print("Ne postoji izvestaj za zadato brojilo!")
        elif option == '3':
            _ret_val = False
        return _ret_val
