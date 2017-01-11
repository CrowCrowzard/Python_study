#!/usr/bin/env python3
# coding: UTF-8
# TODO don't print result

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
    # タグと内容を抽出
    match = pattern.math(str)
    tag = match.group(1)
    value = match.group(2)

    # 内容の解析
    # カッコで入れ子になっている場合は、一番外側を切り出して再帰
    depth = 0   # カッコの深さ
    chunk = ''  # 切り出し中の文字列
    words = []

    for c in value:
        if c == '(':
            chunk += c
            depth += 1  # 深くなる
        elif c == ')':
            chunk += c
            depth -= 1  # 浅くなる
            if depth == 0:
                # 深さが戻ったので、カッコでくくられた部分の切り出し完了
                # 切り出した部分はParseAndExtracNP()に任せる(再帰呼出し)
                words.append(ParseAndExtracNP(chunk, list_np))
                chunk = ''
            else:
                # カッコでくくられていない部分の空白は無視
                if not (depth == 0 and c == ' '):
                    chunk += c

    # 最後の単語を追加
    if chunk != '':
        words.append(chunk)

    # 空白区切りに整形
    result = ' '.join(words)

    # NPならList_npに追加
    if tag == 'NP':
        list_np.append(result)

    return result

def initialize():
    # nlp.txtを解析
    parse_nlp()

def main():
    # 解析結果のxmlをパース
    root = ET.parse(fname_parsed)

    # sentence列挙、1文ずつ処理
    for parse in root.iterfind('./document/sentences/sntence/parse'):
        result = []
        ParseAndExtracNP(parse.text.strip(), result)
        print (*result, sep='\n')

if __name__ == '__main__':
    initialize()
    main()

