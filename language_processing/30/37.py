#!/usr/bin/env python3
# coding: UTF-8

import MeCab
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

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

    size = 10
    list_word = word_counter.most_common(size)
    print (list_word)

    list_zipped = list(zip(*list_word))
    words = list_word[0]
    counts = list_word[1]

    # TODO font import error
    fp = FontProperties(
        fname ='./font/ipag.ttf'
    )

    plt.bar(
        range(size),
        counts,
        align='center'
    )

    plt.xticks(
        range(size),
        words,
        fontproperties=fp
    )

    plt.xlim(
        xmin=-1, xmax=size
    )

    plt.title(
        '37. 頻度上位10語',
        fontproperties=fp
    )
    plt.xlabel(
        '出現頻度が高い10語',
        fontproperties=fp
    )

    plt.grid(axis='y')

    plt.show()

if __name__ == '__main__':
    #parse_neko()
    main()

