#!/usr/bin/env python3
# coding: UTF-8

delimiter = ".;:?!"

with open('nlp.txt', 'r') as file:
    sentence = ""
    for line in file:
        for c in line:
            if c.isupper():
                if (len(sentence) > 2 and sentence[-1] == ' ' and (sentence[-2] in delimiter)):
                    print (sentence)
                    sentence = ""
            else:
                sentence += c
    print (sentence)

