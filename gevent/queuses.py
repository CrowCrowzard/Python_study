#!/usr/bin/env python3
# coding: UTF-8

import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=3)

def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1)
            print ('Worker %s got task %s' % (n, task))
            gevent.sleep(0)
    except Empty:
        print('Quitting time!')

def boss():
    for i in range(1, 10):
        tasks.put(i)
    print('Assinged all work in iteration 1')

    for i in range(10, 20):
        tasks.put(i)
    print('Assinged all work in iteration 2')


def main():
    gevent.joinall([
        gevent.spawn(boss),
        gevent.spawn(worker, 'steve'),
        gevent.spawn(worker, 'john'),
        gevent.spawn(worker, 'nancy'),
    ])

if __name__ == '__main__':
    main()


