#!/usr/bin/env python3
# coding: UTF-8

in_file  = open('hightemp.txt', 'r')
out_file = open('head_n.txt', 'w')

n = int(input('input number : '))

with in_file, out_file:
    for i,line in enumerate(in_file):
        if i == n:
            break
        out_file.write(line)



