#!/usr/bin/env python3
# coding: UTF-8

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
position = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dict = {}
for index, word in enumerate(sentence.split(' ')):
    pos = index+1
    if pos in position:
        dict[word[0]] = pos
    else:
        dict[word[0:2]] = pos

print (dict)