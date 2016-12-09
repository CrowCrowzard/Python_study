#!/usr/bin/env python3
# coding: UTF-8

from functools import partial

def sayhello(message="hello", to="ryo"):
    print ("{1}さん、{0}".format(message, to))

def main():
    sayhello()

    konnichiwa = partial(sayhello, "こんにちは")

    konnichiwa("nishikawa")
    konnichiwa("takahashi")

if __name__ == "__main__":
    main()
