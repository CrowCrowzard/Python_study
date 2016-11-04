#!/usr/bin/env python3
# coding: UTF-8

in_file  = open('txt_data/hightemp.txt', 'r')
out_file = open('txt_data/tail_n.txt', 'w')

n = int(input("input number : "))
with in_file, out_file:
    lines = [line for line in in_file]
    for line in lines[-n:]:
        out_file.write(line)

