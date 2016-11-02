#!/usr/bin/env python3
# coding: UTF-8

with open('hightemp.txt', 'r') as file:
    for line in file:
        print (line.replace("\t", " "), end='')
