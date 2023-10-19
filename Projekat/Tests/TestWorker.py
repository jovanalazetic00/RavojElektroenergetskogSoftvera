import unittest

import sys

sys.path.append("../../")

from unittest.mock import MagicMock
from Projekat.Worker.worker import Worker
from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class MyTestCase(unittest.TestCase):

    def test1_do_work(self):
        obj = Worker("WORKER_1")

        db = DatabaseCRUD()
        db.get_brojilo = MagicMock(return_value=[])
        obj.db = db

        self.assertEqual(obj.do_work("1 1 1"), -1)
        db.get_brojilo.assert_called_once()  #da li se get brojilo metoda pozvala jednom

    def test2_do_work(self):
        obj = Worker("WORKER_1")

        db = DatabaseCRUD()
        db.get_potrosnja_brojila = MagicMock(return_value=[1, 1, 1000])
        obj.db = db

        self.assertEqual(obj.do_work("1 1 1"), -2)
        db.get_potrosnja_brojila.assert_called_once()

    def test3_do_work(self):
        obj = Worker("WORKER_1")

        db = DatabaseCRUD()
        db.insert = MagicMock(return_value=1)
        db.get_potrosnja_brojila = MagicMock(return_value=[])
        obj.db = db

        self.assertEqual(obj.do_work("1 1 1"), 0)
        db.insert.assert_called_once()
        db.get_potrosnja_brojila.assert_called_once()

    def test1_queue_put(self):
        obj = Worker("WORKER_1")  #da li je nesto stavljeno u red
        self.assertEqual(obj.q.empty(), True)
        obj.queue_put("SOME ITEM")
        self.assertEqual(obj.q.qsize(), 1)

    def test1_check(self):
        obj = Worker("WORKER_1")
        self.assertEqual(obj.is_free, True)

    def test2_check(self):
        obj = Worker("WORKER_1")
        obj.is_free = False
        self.assertEqual(obj.is_free, False)

    def test1_start_worker(self):
        obj = Worker("WORKER_1")
        obj.queue_put("!TERM")
        self.assertEqual(obj.start_worker(), 0)

