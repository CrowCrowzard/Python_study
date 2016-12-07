#!/usr/bin/env python3
# coding: UTF-8

from zaifapi.impl import ZaifPublicApi, ZaifPrivateApi

# ビットコインと日本円の終値を取得
zaif = ZaifPublicApi()
print (zaif.last_price('btc_jpy'))

# 残高などのアカウント情報を取得
#zaif = ZaifPrivateApi(key, secret)
#print (zaif.get_inf())

