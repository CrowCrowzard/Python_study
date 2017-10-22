#!/usr/bin/env python3
# coding: UTF-8

def get_info(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

def main():
    x = 12
    y = '気温'
    z = 22.4
    print (get_info(x, y, z))

if __name__ == '__main__':
    main()

