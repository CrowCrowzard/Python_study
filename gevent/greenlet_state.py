#!/usr/bin/env python3
# coding: UTF-8

import gevent

def win():
    return 'You win!'

def fail():
    raise Exception('You fail failing.')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print (winner.started) # True
print (loser.started) # True

# Exceptions raised in the Greenlet, stay inside the Greelet.
try:
    gevent.joinall([winner, loser])
except Exception as e:
    print ('This will never be reached')

print (winner.value) # 'You win!'
print (loser.value)  # None

print (winner.ready()) # True
print (loser.ready())  # True

print (winner.successful()) # True
print (loser.successful())  # False

print (loser.exception)

