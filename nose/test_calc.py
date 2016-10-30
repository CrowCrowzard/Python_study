# coding: UTF-8

from unittest import TestCase
from nose.tools import ok_, eq_
from calc import sum, is_even

class CalcTestCase(TestCase):
    def setUp(self):
        print ('before test')

    def tearDown(self):
        print ('after test')

    def test_sum(self):
        eq_(sum(1,2), 3)
        eq_(sum(5,11), 16)
        eq_(sum(0,0), 0)

    def test_is_even(self):
        ok_(is_even(2))
        ok_(not is_even(3))

