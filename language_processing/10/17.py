#!/usr/bin/env python3
# coding: UTF-8

with open('txt_data/hightemp.txt', 'r') as file:
    result = set(line.split('\t')[0] for line in file)

for x in result:
    print (x)

