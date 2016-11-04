#!/usr/bin/env python3
# coding: UTF-8

from collections import Counter

with open('txt_data/hightemp.txt', 'r') as file:
    lines = file.readlines()
    counter = Counter(line.split('\t')[0] for line in lines)

    keys = [(c,counter[c]) for c in counter]
    keys.sort(key=lambda k: k[1], reverse=True)

    for key in keys:
        for line in lines:
            if key[0] in line:
                print (line, end='')
