from Projekat.DatabaseAnalitics.Classes.PotrosnjaGrad import PotrosnjaGrad
from Projekat.DatabaseAnalitics.Classes.PotrosnjaBrojila import PotrosnjaBrojila


class Parser:

    @staticmethod
    def parsiranje_po_gradovima(input_parameter):  #uzme torke koje su stigle
        _ret_val = list()  #kreira pomocnu listu
        for _item in input_parameter:  #prolazi kroz njih
            _report = PotrosnjaGrad(_item[0], _item[1], _item[2])  #kreira riport
            _ret_val.append(_report)  #dodam ga u pomocnu klasu i dodajemo isparsirano u analitics ui
        return _ret_val

    @staticmethod
    def parsiranje_po_brojilima(input_parameter):
        _ret_val = list()
        for _item in input_parameter:
            _report = PotrosnjaBrojila(_item[0], _item[1])
            _ret_val.append(_report)
        return _ret_val
