class Report:

    @staticmethod
    def prikazi_potrosnju_po_gradovima(input_parameter):
        print("ID BROJILA".ljust(15), "MESEC ".ljust(20), "POTROSNJA")
        print("-" * 46)
        for _item in input_parameter:  #ispis onoga sto je korisnik isparsirao
            print(f"  {_item.get_id()}".ljust(15), f"{Report.get_mesec(_item.get_mesec())}".ljust(20), f"{_item.get_potrosnja()}")
        print("-" * 46)

    @staticmethod
    def prikaz_potrosnje_po_brojilu(input_parameter):
        print("MESEC ".ljust(20), "POTROSNJA")
        print("-" * 30)
        for _item in input_parameter:
            print(f"{Report.get_mesec(_item.get_mesec())}".ljust(20), f"{_item.get_potrosnja()}")
        print("-" * 30)

    @staticmethod
    def get_mesec(mesec):
        if mesec == 1:
            return "JANUAR"
        elif mesec == 2:
            return "FEBRUAR"
        elif mesec == 3:
            return "MART"
        elif mesec == 4:
            return "APRIL"
        elif mesec == 5:
            return "MAJ"
        elif mesec == 6:
            return "JUN"
        elif mesec == 7:
            return "JUL"
        elif mesec == 8:
            return "AVGUST"
        elif mesec == 9:
            return "SEPTEMBAR"
        elif mesec == 10:
            return "OKTOBAR"
        elif mesec == 11:
            return "NOVEMBAR"
        else:
            return "DECEMBAR"