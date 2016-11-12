#!/usr/bin/env python3
# coding: UTF-8

import MeCab

in_file  = 'neko.txt'
out_file = 'neko.txt.mecab'

def parse_neko():
    with open(in_file, 'r') as in_f, open(out_file, 'w') as out_f:
        mecab = MeCab.Tagger()
        out_f.write(mecab.parse(in_f.read()))

def neko_lines():
    with open(out_file, 'r') as out_f:
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
    list_a_no_b = []
    lines = neko_lines()
    for line in lines:
       if len(line) > 2:
           for i in range(1, len(line)-1):
               if line[1]['surface'] == 'の' \
                       and line[i-1]['pos'] == '名詞' \
                       and line[i+1]['pos'] == '名詞':
                    list_a_no_b.append(line[i-1]['surface'] + 'の' + line[i+1]['surface'])

    a_no_b = set(list_a_no_b)
    print(sorted(a_no_b, key=list_a_no_b.index))

if __name__ == '__main__':
    parse_neko()
    main()
