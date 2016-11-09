#!/usr/bin/env python3
# coding: UTF-8

with open('neko.txt.mecab', 'r') as file:
    words = set()
    for line in file:
        cols = line.split('\t')
        if (len(cols) < 2):
            for word in words:
                print (word)
            raise StopIteration
        res_cols = cols[1].split(',')

        if res_cols[0] == '名詞' and res_cols[1] == 'サ変接続':
            words.add(cols[0])
            
