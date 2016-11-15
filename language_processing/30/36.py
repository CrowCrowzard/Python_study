#!/usr/bin/env python3
# coding: UTF-8

import MeCab
from collections import Counter

input_file  = 'neko.txt'
output_file = 'neko.txt.mecab'

def parse_neko():
    with open(input_file, 'r') as in_f, open(output_file, 'w') as out_f:
        mecab = MeCab.Tagger()
        out_f.write(mecab.parse(in_f.read()))

def neko_lines():
    with open(output_file, 'r') as out_f:
        morphemes = []
        for line in out_f:
            cols = line.split('\t')
            if (len(cols) < 2):
                raise StopIteration
            res_cols = cols[1].split(',')

            morpheme = {
                'surface': cols[0],
                'base': res_cols[6],
                'pos': res_cols[0],
                'pos1': res_cols[1]
            }
            morphemes.append(morpheme)

            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []

def main():
    word_counter = Counter()
    for line in neko_lines():
        word_counter.update([morpheme['surface'] for morpheme in line])

    list_word = word_counter.most_common()
    print (list_word)

if __name__ == '__main__':
    parse_neko()
    main()

