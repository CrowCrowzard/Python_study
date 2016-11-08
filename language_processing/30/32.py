#!/usr/bin/env python3
# coding: UTF-8

with open('neko.txt.mecab', 'r') as file:
    morphemes = []
    for line in file:
        cols = line.split('\t')
        if (len(cols) < 2):
            raise StopIteration
        res_cols = cols[1].split(',')

        if res_cols[0] == '動詞':
            print ('{%s:%s}' % (cols[0], res_cols[6]))
            
