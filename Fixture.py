__author__ = 'aberes'


# This module is cteted to show differance between fixtures in Unittest and Nose
# You must run it with both nose and unittest:
# Do not forget to use param --nocapture for nose:
import unittest

def setUpModule():
    print("In Setup Module")


def tearDownModule():
    print("In tear down Module")


# @unittest.skip("weve")
class TestOfFixture_Unit_Test(unittest.TestCase):
    def setUp(self):
        print("TestOfFixture_Unit_Test.in Setup test")

    def tearDown(self):
        print("TestOfFixture_Unit_Test.In Tear Down")

    @classmethod
    def setUpClass(cls):
        print("TestOfFixture_Unit_Test.in Setup Class")

    @classmethod
    def tearDownClass(cls):
        print("TestOfFixture_Unit_Test.In Tear Down Class")

    def testmethod(self):
        print("TestOfFixture_Unit_Test.test")
        self.assertTrue(1 == 1)


def setup_func():
    print("setup_func.in setup test")


def teardown_func():
    print("teardown_func.in tear down")


class TestOfFixture_Nose():
    @classmethod
    def setUpClass(self):
        print("TestOfFixture_Nose.in Setup Class")

    def setUp(self):
        print("TestOfFixture_Nose.in Setup test")

    def test(self):
        print("TestOfFixture_Nose.some test code")
