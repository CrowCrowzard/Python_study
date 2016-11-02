#!/usr/bin/env python3
# coding: UTF-8

sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

result = {}
word = sentence.split(' ')
for i,w in enumerate(word):
    if (i == 0 or i == 4 or i == 5 or i == 6 or i== 7 or i == 8 or i == 14 or i == 15 or i == 18):
        result[w[0]] = i+1
    else:
        result[w[0:2]] = i+1

print (result)
    
