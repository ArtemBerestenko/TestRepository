__author__ = 'aberes'


# This module is cteted to show differance between fixtures in Unittest and Nose
# You must run it with both nose and unittest:
# Do not forget to use param --nocapture for nose:
import unittest

def setUpModule():
    print "In Setup Module"


def tearDownModule():
    print "In tear down Module"


# @unittest.skip("weve")
class TestOfFixture_Unit_Test(unittest.TestCase):
    def setUp(self):
        print "in Setup test"

    def tearDown(self):
        print "In Tear Down"

    @classmethod
    def setUpClass(cls):
        print "in Setup Class"

    @classmethod
    def tearDownClass(cls):
        print "In Tear Down Class"

    def testmethod(self):
        self.assertTrue(1 == 1)


def setup_func():
    print "in setup test"


def teardown_func():
    print "in tear down"


class TestOfFixture_Nose():
    @classmethod
    def setUpClass(self):
        print "in Setup Class"

    def setUp(self):
        print "in Setup test"

    def test(self):
        print "some test code"
