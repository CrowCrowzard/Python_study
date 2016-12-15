#!/usr/bin/env python3
# coding: UTF-8

from bottle import get, run, template

@get("/")
def hello():
    return template("index") # view/index.htmlを返す

run(host="localhost", port=8080) # ポート8080番でwebサーバを立てる
