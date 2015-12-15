__author__ = 'aberes'

import proboscis
import unittest
from proboscis.asserts import assert_equal
from proboscis.decorators import test

from proboscis.decorators import after_class
from proboscis.decorators import before_class


#this class will be run be noze
@test
class RunByNose (unittest.TestCase):

    """ this does not work anymore
    def setUpClass(self):
        print("RunByNose.setUpClass")
    """

    @before_class
    def beforemethod():
        print("RunByNose.beforeclass")

    def setUp(self):
        print ("RunByNose.setUp")
    def tearDown(self):
        print ("RunByNose.tearDown")

    def test_somemet(self):
        print ("RunByNose.test_somemet")

    def test(self):
        print("RunByNose.test")

#this class will be run by proboscis and show dependencies for us
@test
class Dependencies():
    @test(groups=["first_group"])
    def test_A(self):
        print ("Dependencies.test_A")
        assert_equal("1", "2")
    @test(depends_on = [test_A])
    def test_B(self):
        print ("Dependencies.test_B")

#this class will show us fixtures in proboscis
@test
class Fixture(object):
    @test
    def method(self):
        print("Fixture.method")

    @before_class
    def beforemethod(self):
        print("Fixture.before")

    @after_class(always_run=True)
    def aftermethod(self):
        print("Fixture.after")

#this is runner
def run_tests():
    from proboscis import TestProgram
    #from tests import unit

    # Run Proboscis and exit.
    TestProgram().run_and_exit()

if __name__ == '__main__':

    run_tests()
