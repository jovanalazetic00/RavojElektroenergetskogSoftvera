from Projekat.DatabaseAnalitics.Classes.PotrosnjaBrojila import PotrosnjaBrojila


class PotrosnjaGrad(PotrosnjaBrojila):  #nasljedjuje potrosnju brojila, jer je prosiruje

    def __init__(self, id_parameter, mesec_parameter, potrosnja_parameter):  #uzima id mjesec i potrosnju
        self.id = id_parameter
        super().__init__(mesec_parameter, potrosnja_parameter)  #iskoristi konstruktor od nadklase

    def get_id(self):
        return self.id
