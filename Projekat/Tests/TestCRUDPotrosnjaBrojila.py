import unittest
from MockDB import MockDB


class MyTestCase(MockDB):
    def test1_read(self):
        # Pokusaj citanja sa jednim parametrom
        with self.assertRaises(IndexError):
            self.db2.read(1)

    def test2_read(self):
        # Pokusaj citanja merenja brojila koje postoji u MockDB
        self.assertEqual(self.db2.read(1, 3), [(1, 999.0, 3)])

    def test3_read(self):
        # Pokusaj citanja brojila koje ne postoji u MockDB
        self.assertEqual(self.db2.read(1, 4), [])

    def test4_read(self):
        # Pokusaj citanja svih brojila SQL Injection napadom
        with self.assertRaises(IndexError):
            self.assertEqual(self.db2.read("'a'='a';--;"), [])

    def test5_read(self):
        # Pokusaj citanja bez da se prosledi parametar
        with self.assertRaises(Exception):
            self.db2.read()

    def test6_read(self):
        with self.assertRaises(Exception):
            self.db2.read(1)

    def test7_read(self):
        self.assertEqual(self.db2.read(1, 1, 2), -5)

    def test1_insert(self):
        # Pokusaj unosa novog merenja brojila ciji IdBrojila i Mesec postoji u MockDB
        self.assertEqual(self.db2.insert(1, 2, 1000), -1)

    def test2_insert(self):
        # Pokusaj unosa novog merenja brojila ciji IdBrojila i Mesec ne postoji u MockDB
        self.assertEqual(self.db2.insert(1, 6, 111), 1)

    def test3_insert(self):
        # Pokusaj unosa novog brojila bez parametra
        with self.assertRaises(Exception):
            self.db2.insert()

    def test4_insert(self):
        # Pokusaj unosa novog merenja brojila sa jednim parametrom
        with self.assertRaises(Exception):
            self.db2.insert(1)

    def test5_insert(self):
        # Pokusaj unosa novog merenja brojila sa dva parametra
        with self.assertRaises(Exception):
            self.db2.insert(1, 2)

    def test6_insert(self):
        # Pokusaj unosa novog merenja brojila sa dva parametra
        self.assertEqual(self.db2.insert(1, 1, 1, 2), -5)

    def test1_update(self):
        #  Pokusaj izmene postojeceg merenja brojila u MockDB
        self.assertEqual(self.db2.update(1, 500, 2), 1)

    def test2_update(self):
        #  Pokusaj izmene ne postojeceg merenja brojila u MockDB
        self.assertEqual(self.db2.update(11, 1, 999), 0)

    def test3_update(self):
        # Pokusaj izmene brojila bez parametra
        with self.assertRaises(IndexError):
            self.db2.update()

    def test4_update(self):
        # Pokusaj izmene merenja brojila sa jednim parametrom
        with self.assertRaises(IndexError):
            self.db2.update(1)

    def test5_update(self):
        # Pokusaj izmene merenja brojila sa dva parametrom
        with self.assertRaises(IndexError):
            self.db2.update(1, 1)

    def test6_update(self):
        # Pokusaj izmene merenja brojila sa cetiri parametrom
        self.assertEqual(self.db2.update(1, 1, 1, 1), -5)

    def test1_delete(self):
        # Pokusaj brisanja sa jednim parametrom
        with self.assertRaises(IndexError):
            self.assertEqual(self.db2.delete(7), 1)

    def test2_delete(self):
        # Pokusaj brisanja merenja koje postoji u MockDB
        self.assertEqual(self.db2.delete(1, 2), 1)

    def test3_delete(self):
        # Pokusaj brisanja brojila koje ne postoji u MockDB
        self.assertEqual(self.db2.delete(5, 1), 0)

    def test4_delete(self):
        # Pokusaj brisanja bez parametara
        with self.assertRaises(IndexError):
            self.db2.delete()

    def test5_delete(self):
        # Pokusaj brisanja sa tri parametra
        self.assertEqual(self.db2.delete(1, 2, 2), -5)


#if __name__ == '__main__':
    #unittest.main()
