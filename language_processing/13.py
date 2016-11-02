#!/usr/bin/env python3
# coding: UTF-8

col1 = open('col1.txt', 'r')
col2 = open('col2.txt', 'r')
col12 = open('col12.txt', 'w')

with col1, col2, col12:
    for a,b in zip(col1, col2):
        col12.write(a.rstrip('\n') + '\t' + b)

