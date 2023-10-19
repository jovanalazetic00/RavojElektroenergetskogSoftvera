from unittest import TestCase

import sys

sys.path.append("../../")

from Projekat.Worker.worker import Worker


class DummyWorkers(TestCase):

    @classmethod
    def setUp(cls):
        workers = list()

        for i in range(0, 4):
            workers.append(Worker(f"WORKER_{i}"))

        cls.dummy = workers

    def tearDown(self):
        self.dummy.clear()
