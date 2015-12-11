# -*- coding: cp1251 -*-

from nose import with_setup


def setup_module():
    print("setup_module")

def my_setup_function():
    print("my_setup_function")


def my_teardown_function():
    print("my_teardown_function")


def test_plus():
    print("test_plus")


def test_minus():
    print("test_minus")


@with_setup(my_setup_function, my_teardown_function)
def test_initials():
    print("test_initials")


def test_some_not_correct():
    print("test_some_not_correct")
    assert 1 == 2
