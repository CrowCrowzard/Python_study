#!/usr/bin/env python3
# coding: UTF-8

from urllib.request import urlopen

f = urlopen('http://qiita.com/advent-calendar/2014')
print (f.code)
print (f.getheader('content-type'))
print (f.info().get_content_charset())
#print (f.read())

