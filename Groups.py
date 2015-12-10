__author__ = 'aberes'

import unittest


class TestGroupA(unittest.TestCase):
    def test_a(self):
        self.assertTrue(1 == 2)
        print "a"

    def test_c(self):
        print "c"


class TestGroupB(unittest.TestCase):
    def test_b(self):
        print "b"
