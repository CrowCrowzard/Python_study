#!/usr/bin/env python3
# coding: UTF-8

import gevent
from gevent.pool import Pool

pool = Pool(2)

def hello_from(n):
    print ('Size of pool', len(pool))

pool.map(hello_from, range(3))
