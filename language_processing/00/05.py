#!/usr/bin/env python3
# coding: UTF-8

def get_n_gram(target, n):
    n_gram = []
    for i in range(len(target)-n+1):
        n_gram.append(target[i:i+n])
    return n_gram

def main():
    target = 'I am an NLPer'
    words_target = target.split(' ')

    # 単語bi-gram
    n_gram = get_n_gram(words_target, 2)
    print (n_gram)

    # 文字bi-gram
    n_gram = get_n_gram(target, 2)
    print (n_gram)

if __name__ == '__main__':
    main()

