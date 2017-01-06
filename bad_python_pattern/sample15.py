#!/usr/bin/env python3
# coding: UTF-8

from collections import *

names = ['s', 'p', 'l', 'g']
o = OrderedDict()
for name in names:
    o[name] = 1
#>>> sample15.o
#OrderedDict([('s', 1), ('p', 1), ('l', 1), ('g', 1)])

oo = dict()
for name in names:
    oo[name] = 1
#>>> sample15.oo
#{'s': 1, 'l': 1, 'p': 1, 'g': 1}
