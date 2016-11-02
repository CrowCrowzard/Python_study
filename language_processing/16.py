#!/usr/bin/env python3
# coding: UTF-8

import os
import shutil
import math

create_dir = 'txt_data/split'
if os.path.exists(create_dir):
    shutil.rmtree(create_dir)
os.mkdir(create_dir)


n = int(input('file split num : '))

with open('txt_data/hightemp.txt', 'r') as file:
    lines = file.readlines()

count = len(lines)
group = math.ceil(count / n)

for i,index in enumerate(range(0, count, group), 1):
    with open('txt_data/split/file%02d.txt' % i, 'w') as file:
        for line in lines[index:index+group]:
            file.write(line)

