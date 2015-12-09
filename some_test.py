import random
import unittest

from ForTest import TestedClass


def setUpModule():
    print "Before module"


def tearDownModule():
    print "After module"


testinst = TestedClass()


class TestSequenceFunctions(unittest.TestCase):
    def test_ForTest(self):
        self.assertTrue(testinst.plus(1, 2) == 3)

    @classmethod
    def setUpClass(self):
        print "Initials before test class"

    @classmethod
    def tearDownClass(self):
        print "Conditions after test class"

    def setUp(self):
        print "before each unit test"
        self.seq = range(10)

    def tearDown(self):
        print "after each unit test"

    def testmytest(self):
        self.assertTrue(2 == 1)

    def test_shuffle(self):
        # We check that blended sequence is not lost
        # no element
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))
        # throw exceptions for not changable sequenses
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)
