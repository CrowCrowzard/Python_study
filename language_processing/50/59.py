#!/usr/bin/env python3
# coding: UTF-8

import os
import subprocess
import xml.etree.ElementTree as ET
import re

fname = 'nlp.txt'
fname_parsed= 'nlp.txt.xml'

# タグと内容を抽出するための正規表現
pattern = re.compile(r'''
    ^
    \(          # S式の開始カッコ
        (.*?)   # = タグ
        \s      # 空白
        (.*)    # = 内容
    \)          # S式の終わりのカッコ
    $
    ''', re.VERBOSE + re.DOTALL)

def parse_nlp():
    '''
    nlp.txtをStanford Core NLPで解析しxmlファイルへ出力
    すでに結果ファイルが存在する場合は実行しない
    '''
    if not os.path.exists(fname_parsed):
        # StanfordCoreNLP実行、標準エラーはparse.outへ出力
        subprocess.run(
            'java -cp "/usr/local/lib/stanford-corenlp-full-2016-103-31/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,limma,ner,parse,dcoref'
            ' -file ' + fname + ' 2>parse.out',
            shell=True,     # shellで実行
            check=True      # エラーチェックあり
        )

def ParseAndExtractNP(str, list_up):
    '''
    S式をタグと内容に分解し内容のみを返す
    またタグがNPの場合は、内容をlist_npにも追加する
    内容が入れ子になっている場合は、
    その中身も解析して、内容を空白区切りで返す

    戻り値：
    タグを除いた内容
    '''
    # TODO プログラム記載



if __name__ == '__main__':
    main()


