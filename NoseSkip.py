__author__ = 'aberes'

import unittest

from configobj import ConfigObj
# file = open("failure.ini", "w+")
# file.close()
config = None


# This decorator can write to file failured tests
#
def decorator(function_to_decorate):
    def wrapper(self):
        try:
            function_to_decorate(self)
        except AssertionError as exc:
            print "*********In decorator"
            file = open("failure.ini", "w+")
            file.write(function_to_decorate.__name__ + " = " + "Failure" + '\n')
            # file.write("dsgbndgfmjg")
            file.close()
            config = ConfigObj('failure.ini')

            raise exc

    return wrapper


class A(unittest.TestCase):
    # @nose.tools.make_decorator(decorator)
    @decorator
    def testA(self):
        self.assertTrue(1 == 2)

    @unittest.skipIf(config['testA'] == "Failure", "Must be skiped")
    def testB(self):
        print "In test B"
