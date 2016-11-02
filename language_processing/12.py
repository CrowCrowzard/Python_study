#!/usr/bin/env python3
# coding: UTF-8

file = open('hightemp.txt', 'r')
out1 = open('col1.txt', 'w')
out2 = open('col2.txt', 'w')

with file, out1, out2:
    for i, line in enumerate(file):
        array = line.split('\t')
        out1.write(array[0] + '\n')
        out2.write(array[1] + '\n')
