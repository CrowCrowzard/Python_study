#!/usr/bin/env python3
# coding: UTF-8

result = 0
with open('hightemp.txt', 'r') as file:
    for line in file:
        result += 1
print result

