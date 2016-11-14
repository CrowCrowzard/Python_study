#!/usr/bin/env python3
# coding: UTF-8

import MeCab
import time
input_file  = 'neko.txt'
output_file = 'neko.txt.mecab'

def parse_neko():
    with open('neko.txt', 'r') as in_f, open('neko.txt.mecab', 'w') as out_f:
        mecab = MeCab.Tagger()
        out_f.write(mecab.parse(in_f.read()))

def neko_lines():
    with open('neko.txt.mecab', 'r') as out_f:

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
    noun_list = []
    lines = neko_lines()
    for line in lines:
        for i in range(len(line)):
            noun_sentence = []
            for j in range(i, len(line)):
                if line[j]['pos'] == '名詞':
                    noun_sentence.append(line[j]['surface'])
                else:
                    i += j-i
            if (len(noun_sentence) > 1):
                sentence = ''.join(noun_sentence)
                if sentence not in noun_list:
                    noun_list.append(sentence)
    noun_set = set(noun_list)
    print (sorted(noun_set, key=noun_list.index))
                    
if __name__ == '__main__':
    parse_neko()
    main()

