#!/usr/bin/env python3
# coding: UTF-8

import os
import subprocess
import xml.etree.ElementTree as ET
import pydot_ng as pydot

fname = 'nlp.txt'
fname_parsed = 'nlp.txt.xml'

def parse_nlp():
    '''
    nlp.txtをStanford Core NLPで解析しxmlファイルへ出力
    すでに結果ファイルが存在する場合は実行しない
    '''
    if not os.path.exists(fname_parsed):
        # Stanford Core NLP実行、標準エラーはparse.outへ出力
        subprocess.run(
            'java cp "/usr/local/lib/stanford-corenlp-full-2016-10-31/*"'
            ' -Xmx2g'
            ' edu.stanford.nlp.pipeline.StanfordCoreNLP'
            ' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
            ' -file ' +fname + ' 2>parse.out',
            shell=True,     # shellで実行
            check=True      # エラーチェックあり
        )


def graph_from_edges_ex(edge_list, directed=False):
    if directed:
        graph = pydot.Dot(graph_type='digraph')
    else:
        graph = pydot.Dot(graph_type='graph')

    for edge in edge_list:
        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[0][1])

        # ノード追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # エッジ追加
        graph.add_edge(pydot.Edge(id1, id2))

    return graph

def main():
    # nlp.txtを解析
    parse_nlp()

    # 解析結果のxmlをパース
    root = ET.parse(fname_parsed)

    # sentence列挙、1文ずつ処理
    for sentence in root.iterfind('./document/sentences/sentence'):
        sent_id = int(sentence.get('id'))   # sentenceのid

        edges = []
        
        # dependencies列挙
        for dep in sentence.iterfind(
            './dependencies[@type="collapsed-dependencies"]/dep'
        ):
            # 句読点はスキップ
            if dep.get('type') != 'punct':
                # govenor、dependent取得、edgesに追加
                govr = dep.find('./governor')
                dept = dep.find('./dependent')
                edges.append(
                    ((govr.get('idx'), govr.text), (dept.get('idx'), dept.text))
                )

        # 描画
        if len(edges) > 0:
            graph = graph_from_edges_ex(edges, directed=True)
            graph.write_png('{}.png'.format(sent_id))

if __name__ == '__main__':
    main()


