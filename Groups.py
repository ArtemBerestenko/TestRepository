__author__ = 'aberes'

import unittest


class TestGroupA(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1 == 2)
        print("In test_a")

    def test_c(self):
        print("In test_c")


class TestGroupB(unittest.TestCase):
    def test_b(self):
        print("In test_b")
