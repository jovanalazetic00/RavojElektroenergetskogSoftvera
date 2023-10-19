from AnaliticsUI import AnaliticsUI


class DatabaseAnalitics:  #klijent koji komunicira sa bazom

    def __init__(self):
        self.menu = AnaliticsUI() #konstruktor
        self.do = True

    def Analitics_UI(self):
        while self.do:
            self.menu.Options() #opcije menija
            _input = input()  #ceka korisnikov unos
            self.do = self.menu.Handle(_input)  #proslijedi sta je korisnik unio


def main():
    databaseAnalitics = DatabaseAnalitics()   #instanciranje pozivanje
    databaseAnalitics.Analitics_UI()


if __name__ == "__main__":
    main()
