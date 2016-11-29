#!/usr/bin/env python3
# coding: UTF-8

ENGLISH_TXT = 'nlp.txt'

with open(ENGLISH_TXT, 'r') as file:
    cnt = 0
    for line in file.readlines():
        if line == "\n":
            continue
        for word in line.strip().split(' '):
            if cnt >= 50:
                break
            else:
                print (word)
            cnt +=1
        if cnt >= 50:
            break
        else:
            print ()
            cnt += 1

