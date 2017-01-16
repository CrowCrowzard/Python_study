#!/usr/bin/env python3
# coding: UTF-8

import leveldb

fname_db = 'test_db'

def main():
    # LevelDBオープン
    db = leveldb.LevelDB(fname_db)

    # valueが'Japan'のものを列挙
    clue = 'Japan'.encode()
    result = [value[0].decode() for value in db.RangeIter() if value[1] == clue]

    # 件数表示
    print ('{}件'.format(len(result)))

if __name__ == '__main__':
    main()


