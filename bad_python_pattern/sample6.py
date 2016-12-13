#!/usr/bin/env python3
# coding: UTF-8

import datetime

def log_out(msg, when=datetime.datetime.now()):
    print('%s %s ' % (when, msg))

# >>> log_out('Good bye!!')
# 2016-12-13 23:21:12.960946 Good bye!!
# >>> log_out('Good bye!!')
# 2016-12-13 23:21:12.960946 Good bye!!
