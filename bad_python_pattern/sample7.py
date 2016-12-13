#!/usr/bin/env python3
# coding: UTF-8

import datetime

def log_out(msg, when=None):
    """ タイムスタンプを含めたログを出力する

    Args:
        msg: ログメッセージ
        when: ログ出力の日時。なければ現在時刻を設定する
    """
    when = datetime.datetime.now() if when is None else when
    print ('%s %s ' % (when, msg))

# >>> log_out('Good bye!!')
# 2016-12-13 23:24:32.778606 Good bye!!
# >>> log_out('Good bye!!')
# 2016-12-13 23:24:41.363866 Good bye!!
# >>> log_out('Good bye!!', datetime.datetime(2016,11,1))
# 2016-11-01 00:00:00 Good bye!!
