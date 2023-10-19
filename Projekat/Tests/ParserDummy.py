from unittest import TestCase

import sys

sys.path.append("../../")

from Projekat.DatabaseAnalitics.Classes.PotrosnjaGrad import PotrosnjaGrad
from Projekat.DatabaseAnalitics.Classes.PotrosnjaBrojila import PotrosnjaBrojila


class ParserDummy(TestCase):

    @classmethod
    def setUp(cls):
        _ret = list()

        _ret.append([1, 1, 1000])
        _ret.append([1, 2, 600])
        _ret.append([9, 12, 333])
        _ret.append([4, 7, 333])

        temp = list()
        temp.append(PotrosnjaGrad(1, 1, 1000))
        temp.append(PotrosnjaGrad(1, 2, 600))
        temp.append(PotrosnjaGrad(9, 12, 333))
        temp.append(PotrosnjaGrad(4, 7, 333))

        cls.report1 = temp
        cls.dummy1 = _ret

        _ret = list()

        _ret.append([1, 1])
        _ret.append([1, 2])
        _ret.append([9, 12])
        _ret.append([4, 7])

        temp = list()
        temp.append(PotrosnjaBrojila(1, 1))
        temp.append(PotrosnjaBrojila(1, 2))
        temp.append(PotrosnjaBrojila(9, 12))
        temp.append(PotrosnjaBrojila(4, 7))

        cls.report2 = temp
        cls.dummy2 = _ret


    def tearDown(self):
        self.dummy1.clear()
        self.dummy2.clear()
