# coding: UTF-8

from unittest import TestCase
from nose.tools import timed
from time_ import do_something

class TimeTestCase(TestCase):
    @timed(0.2)
    def test_do_something(self):
        do_something()

