#!/usr/bin/env python3
# coding: UTF-8

from urllib.request import urlopen

#f = urlopen('http://qiita.com/advent-calendar/2014')
#print (f.code)
#print (f.getheader('content-type'))
#print (f.info().get_content_charset())
##print (f.read())

def downloadImageFromInternet(source, filename):
    # 画像ソースを開く
    response = urlopen(source)

    # HTTPステータスコードが200でないなら-1を返す
    if response.code != 200:
        return -1

    # 保存先をバイナリ形式で開く
    with open(filename, 'wb') as file:
        file.write(response.read())

    # 0を返す
    return 0

