#!/usr/bin/env python3
# coding: UTF-8

import time

def echo(i):
    time.sleep(0.001)
    return i

from multiprocessing.pool import Pool

with Pool(10) as p:
    run1 = [a for a in p.imap_unordered(echo, range(10))]
    run2 = [a for a in p.imap_unordered(echo, range(10))]
    run3 = [a for a in p.imap_unordered(echo, range(10))]
    run4 = [a for a in p.imap_unordered(echo, range(10))]
    
    print (run1 == run2 == run3 == run4)

from gevent.pool import Pool

p = Pool(10)
run1 = [a for a in p.imap_unordered(echo, range(10))]
run2 = [a for a in p.imap_unordered(echo, range(10))]
run3 = [a for a in p.imap_unordered(echo, range(10))]
run4 = [a for a in p.imap_unordered(echo, range(10))]

print (run1 == run2 == run3 == run4)

