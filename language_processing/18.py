#!/usr/bin/env python3
# coding: UTF-8

from operator import itemgetter

with open('txt_data/hightemp.txt', 'r') as file:
    line_tuples = []
    for line in file:
        raws = line.split('\t')
        line_tuples.append((raws[0], raws[1], raws[2], raws[3]))

    for line in sorted(line_tuples, key=itemgetter(2), reverse=True):
        print ('\t'.join((line)), end='')

