import unittest
from Projekat.LoadBalancer.Scripts.add_script import Add_script
from MockDB import MockDB


class MyTestCase(MockDB):

    def test1_manual_adding(self):
        self.assertEqual(Add_script.manual_adding("Manual:1:2:100", 'test'), -2)  #ako postoji

    def test2_manual_adding(self):
        self.assertEqual(Add_script.manual_adding("Manual:1:11:100", 'test'), 0)  #ako je dodao

    def test3_manual_adding(self):
        self.assertEqual(Add_script.manual_adding("Manual:16:10:100", 'test'), -1)  #ako ne postoji

    def test1_automatic_adding(self):
        buffer = list()

        self.assertEqual(Add_script.automatic_adding("1:1:1", buffer), 1)

