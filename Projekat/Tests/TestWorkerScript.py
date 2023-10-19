import unittest
from DummyWorkers import DummyWorkers
from Projekat.LoadBalancer.Scripts.worker_script import Worker_script


class MyTestCase(DummyWorkers):

    def test1_new_worker(self):
        _temp_len = len(self.dummy)
        self.assertEqual(Worker_script.new_worker(_temp_len, self.dummy), _temp_len + 1)

    def test1_terminate_worker(self):
        _temp_len = len(self.dummy)
        self.assertEqual(Worker_script.terminate_worker("WORKER_0", self.dummy, _temp_len), _temp_len)

    def test2_terminate_worker(self):
        _temp_len = len(self.dummy)
        self.assertEqual(Worker_script.terminate_worker("WORKER_1", self.dummy, _temp_len), _temp_len - 1)

    def test3_terminate_worker(self):
        _temp_len = len(self.dummy)
        self.assertEqual(Worker_script.terminate_worker("RANDOM NAME", self.dummy, _temp_len), _temp_len)

    def test4_terminate_worker(self):
        _temp_len = len(self.dummy)
        self.dummy[1].is_free = False
        self.assertEqual(Worker_script.terminate_worker("WORKER_1", self.dummy, _temp_len), _temp_len)

