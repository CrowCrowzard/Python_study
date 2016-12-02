# TODO 7時間以上かかるので時間短縮を考える
# TODO .envを使う
# Refere: http://qiita.com/lovemuffim114/items/a4760cfa9fc0fff15863
#!/usr/bin/env python3
# coding: UTF-8

from bs4 import BeautifulSoup
import requests

from time import sleep
import json
from progressbar import ProgressBar

# QiitaにLogin
payload = {
    'utf8' : '✓',
    'identity': '', # ユーザー名
    'password': '', # パスワード
}

# authenticity_tokenの取得
s = requests.Session()
r = s.get('https://qiita.com')
soup = BeautifulSoup(r.text, 'html.parser')
auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
payload['authenticity_token'] = auth_token

# ログイン
s.post('https://qiita.com/login', data=payload)

# 結果を保存するための辞書
results = dict()

searchId = 1000000
param = {'before': searchId, 'type': 'id'}

# 記事数を取得
maxId = s.get('http://qiita.com/api/public', params=param).json()[0]['id']
bar = ProgressBar(min_value=0, max_value=maxId) # 最大値をセット

# 読み込む記事がなくなるとエラー
try:
    while True:
        param = {'before': searchId, 'type': 'id'}
        # 記事リスト取得
        j = s.get('http://qiita.com/api/public', params=param).json()

        # resultsに「いいね」かつストックしていない記事を追加
        # 'url'以外に、'uuid'も指定可能
        results.update({p['title']: p['url'] for p in j if p['liked'] and not p['stocked']})

        searchId = j[-1]['id']
        bar.update(maxId - searchId) # プログレスバー更新
        sleep(1)
finally:
    print (results)

    # results.jsonに保存
    with open('results.json', 'a') as f:
        json.dump(results, f, ensure_ascii=False, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    main()


