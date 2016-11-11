#!/usr/bin/env python3
# coding: UTF-8

def cipher(message):
    chp = ""
    for c in message:
        if c.islower():
            chp += chr(219-ord(c))
        else:
            chp += c
    return chp

def main():
    message = raw_input('input sentence : ')
    print (cipher(message))

if __name__ == '__main__':
    main()

