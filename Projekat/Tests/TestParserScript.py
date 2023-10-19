import unittest
from Projekat.DatabaseAnalitics.Scripts.Parser import Parser
from ParserDummy import ParserDummy


class MyTestCase(ParserDummy):
    def test1_gradovi(self):
        _ret = Parser.parsiranje_po_gradovima(self.dummy1)

        i = 0
        for item in _ret:
            self.assertEqual(item.id, self.report1[i].id)
            self.assertEqual(item.mesec, self.report1[i].mesec)
            self.assertEqual(item.potrosnja, self.report1[i].potrosnja)
            i = i + 1

    def test2_gradovi(self):
        self.assertEqual(Parser.parsiranje_po_gradovima([]), [])

    def test1_brojila(self):
        _ret = Parser.parsiranje_po_brojilima(self.dummy2)

        i = 0
        for item in _ret:
            self.assertEqual(item.potrosnja, self.report2[i].potrosnja)
            self.assertEqual(item.mesec, self.report2[i].mesec)
            i = i + 1

    def test2_brojila(self):
        self.assertEqual(Parser.parsiranje_po_brojilima([]), [])

