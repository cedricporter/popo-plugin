#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Hua Liang[Stupid ET] <et@everet.org>
#

import httplib
import urllib
import traceback
import sys

LINUX_HOST = "10.0.2.2"
PORT = 34567


def notify_linux(host, title, port=80):
    try:
        title = title.encode('utf8')
        conn = httplib.HTTPConnection(host, port)
        query = {'title': title, }
        url = '/' + "?" + urllib.urlencode(query)
        conn.request('GET', url)
        return conn.getresponse()
    except:
        traceback.print_exc()


def main():
    print sys.argv
    notify_linux(LINUX_HOST, sys.argv[1].decode("gbk"), PORT)


if __name__ == '__main__':
    main()
