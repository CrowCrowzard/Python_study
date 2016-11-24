#!/usr/bin/env python3
# coding: UTF-8

import random

def typoglycmia(target):
    result = []
    shuffle_list = target[1:-1]
    random.shuffle(shuffle_list)
    
    result.append(target[0])
    result.extend(shuffle_list)
    result.append(target[-1])
    return result

def main():
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    split_sentence = sentence.split(' ')
    if len(split_sentence) > 4:
        split_sentence = typoglycmia(split_sentence)
        print (split_sentence)
        #print (' '.join(split_sentence))
    else:
        print (sentence)

if __name__ == '__main__':
    main()


