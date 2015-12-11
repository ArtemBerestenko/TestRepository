__author__ = 'aberes'

# Section with features may be created in .ini file
import unittest

featureA = False


class A(unittest.TestCase):
    @unittest.skipIf(not featureA, "skiped")
    def test(self):
        print("In test")
