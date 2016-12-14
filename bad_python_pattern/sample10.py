#!/usr/bin/env python3
# coding: UTF-8

class OtherLangStyle(object):
    def __init__(self, val):
        self._val = val

    def get_val(self):
        return self._val

    def set_val(self, new_val):
        self._val = new_val

# >>> import sample10
# >>> ols = sample10.OtherLangStyle(1)
# >>> ols.get_val()
# 1
# >>> ols.set_val(2)
# >>> ols.get_val()
# 2
# >>> ols.set_val(ols.get_val() + 2)
# >>> ols.get_val()
# 4
