import unittest
from MockDB import MockDB


class MyTestCase(MockDB):

    def test1_potrosnja_po_gradu(self):
        self.assertEqual(self.db3.potrosnja_po_gradu("Beograd"), [(3, 4, 555)])

    def test2_potrosnja_po_gradu(self):
        self.assertEqual(self.db3.potrosnja_po_gradu("Nis"), [])

    def test3_potrosnja_po_gradu(self):
        self.assertEqual(self.db3.potrosnja_po_gradu(3), [])

    def test4_potrosnja_po_gradu(self):
        self.assertEqual(self.db3.potrosnja_po_gradu("'a'='a';--;"), [])

    def test5_potrosnja_po_gradu(self):
        with self.assertRaises(Exception):
            self.db3.potrosnja_po_gradu()

    def test6_potrosnja_po_gradu(self):
        self.assertEqual(self.db3.potrosnja_po_gradu("Nis", 2), -5)

    def test1_potrosnja_po_brojilu(self):
        self.assertEqual(self.db3.potrosnja_po_brojilu(1), [(2, 1000), (3, 999)])

    def test2_potrosnja_po_brojilu(self):
        self.assertEqual(self.db3.potrosnja_po_brojilu(2), [])

    def test3_potrosnja_po_brojilu(self):
        self.assertEqual(self.db3.potrosnja_po_brojilu("BG"), [])

    def test4_potrosnja_po_brojilu(self):
        self.assertEqual(self.db3.potrosnja_po_brojilu("'a'='a';--;"), [])

    def test5_potrosnja_po_brojilu(self):
        with self.assertRaises(Exception):
            self.db3.potrosnja_po_brojilu()

    def test6_potrosnja_po_brojilu(self):
        self.assertEqual(self.db3.potrosnja_po_brojilu(2, 2), -5)

   # if __name__ == '__main__':
        # unittest.main()