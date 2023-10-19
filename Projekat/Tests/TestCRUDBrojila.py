import unittest
from MockDB import MockDB


class MyTestCase(MockDB):

    def test1_read(self):
        # Pokusaj citanja brojila koje postoji u MockDB
        self.assertEqual(self.db1.read(1), [self.test_tuple])  #da li se vratilo ono sto ja ocekujem

    def test2_read(self):
        # Pokusaj citanja brojila koje ne postoji u MockDB
        self.assertEqual(self.db1.read(2), [])

    def test3_read(self):
        # Pokusaj citanja brojila koje ne postoji u MockDB
        self.assertEqual(self.db1.read("SD"), [])

    def test4_read(self):
        # Pokusaj citanja svih brojila SQL Injection napadom
        self.assertEqual(self.db1.read("'a'='a';--;"), [])

    def test5_read(self):
        # Pokusaj citanja bez da se prosledi parametar
        with self.assertRaises(Exception):
            self.db1.read()

    def test6_read(self):
        # Pokusaj citanja sa osam parametara
        self.assertEqual(self.db1.read(1, 2, 1, 1, 2, 6, 1, 1), -5)

    def test1_insert(self):
        # Pokusaj unosa novog brojila ciji IdBrojila ne postoji u MockDB
        self.assertEqual(self.db1.insert(10, "Marko", "Markovic", "Zmaj Jovina", 100, '21480', "Srbobran"), 1)

    def test2_insert(self):
        # Pokusaj unosa novog brojila ciji IdBrojila vec postoji u MockDB
        self.assertEqual(self.db1.insert(1, "Janko", "Jankovic", "Neretljanska", 50, '21101', "Novi Sad"), -1)

    def test3_insert(self):
        # Pokusaj unosa novog brojila bez parametra
        with self.assertRaises(Exception):
            self.db1.insert()

    def test4_insert(self):
        with self.assertRaises(Exception):
            self.db1.insert(1)

    def test5_insert(self):
        with self.assertRaises(Exception):
            self.db1.insert(1, 2)

    def test6_insert(self):
        with self.assertRaises(Exception):
            self.db1.insert(1, 2, 3)

    def test7_insert(self):
        with self.assertRaises(Exception):
            self.db1.insert(1, 2, 3, 2)

    def test8_insert(self):
        with self.assertRaises(Exception):
            self.db1.insert(1, 2, 3, 2, 5)

    def test9_insert(self):
        with self.assertRaises(Exception):
            self.db1.insert(1, 2, 3, 2, 5, 9)

    def test10_insert(self):
        self.assertEqual(self.db1.insert(1, 2, 3, 2, 5, 9, 9, 8), -5)

    def test1_update(self):
        #  Pokusaj izmene postojeceg brojila u MockDB
        self.assertEqual(self.db1.update(1, "Janko", "Jankovic", "Vuka Karadzica", 50, '11000', "Beograd"), 1)

    def test2_update(self):
        #  Pokusaj izmene brojila koje ne postoji u MockDB
        self.assertEqual(self.db1.update(11, "Janko", "Jankovic", "Vuka Karadzica", 50, '11000', "Beograd"), 0)

    def test3_update(self):
        # Pokusaj izmene brojila bez parametra
        with self.assertRaises(IndexError):
            self.db1.update()

    def test4_update(self):
        with self.assertRaises(IndexError):
            self.db1.update(1)

    def test5_update(self):
        with self.assertRaises(IndexError):
            self.db1.update(2, 1)

    def test6_update(self):
        with self.assertRaises(IndexError):
            self.db1.update(2, 1, 1)

    def test7_update(self):
        with self.assertRaises(IndexError):
            self.db1.update(2, 1, 1, 2)

    def test8_update(self):
        with self.assertRaises(IndexError):
            self.db1.update(2, 1, 1, 2, 10)

    def test9_update(self):
        with self.assertRaises(IndexError):
            self.db1.update(2, 1, 1, 2, 10, 2)

    def test10_update(self):
        self.assertEqual(self.db1.update(2, 1, 1, 2, 10, 2, 1, 1), -5)

    def test1_delete(self):
        # Pokusaj brisanja postojeceg u MockDB unutar tabele Brojlo
        self.assertEqual(self.db1.delete(7), 1)

    def test2_delete(self):
        # Pokusaj brisanja postojeceg u MockDB unutar tabele Brojlo (naruseno ogranicenje stranog kljuca)
        self.assertEqual(self.db1.delete(1), -1)

    def test3_delete(self):
        # Pokusaj brisanja brojila koje ne postoji u MockDB
        self.assertEqual(self.db1.delete(5), 0)

    def test4_delete(self):
        # Pokusaj brisanja bez parametara
        with self.assertRaises(IndexError):
            self.db1.delete()

    def test5_delete(self):
        self.assertEqual(self.db1.delete(1, 2), -5)


    #if __name__ == '__main__':
         #unittest.main()
