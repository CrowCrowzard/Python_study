#!/usr/bin/env python3
# coding: UTF-8

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

result = []
for word in sentence.split(' '):
    count = 0
    for c in word:
        if c.isalpha():
            count += 1
    result.append(count)
print (result)

