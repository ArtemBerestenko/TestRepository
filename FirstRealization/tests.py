# -*- coding: cp1251 -*-
import time

from nose import with_setup

from functions_for_test import plus, minus


def setup_module():
    f = open("txt.txt", "w")
    f.write("This is written at start of the module run: %s" % str(time.time()))
    f.close()


def my_setup_function():
    f = open("text.txt", "w")
    f.write("some line")
    f.close()


def my_teardown_function():
    pass


def test_plus():
    assert plus(3, 2) == 5
    print "In method test_plus"


def test_minus():
    print "test numbers"
    assert minus(3, 1) == 2


@with_setup(my_setup_function, my_teardown_function)
def test_initials():
    assert 5 == 5


def test_some_not_correct():
    assert 1 == 2


print plus(1, 2)
print minus(4, 2)
