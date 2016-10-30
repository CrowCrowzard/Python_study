# coding: UTF-8

from unittest import TestCase
from nose.tools import eq_, raises
from div import div

class DivTestCase(TestCase):
    def test_div(self):
        eq_(div(10, 5), 2)
        eq_(div(10, 10), 1)
        eq_(div(9, 3), 3)

    @raises(ZeroDivisionError)
    def test_div_zerodiv(self):
        div(10, 0)

