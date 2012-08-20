#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
# 

import time, httplib, urllib
from pprint import pprint
import win32gui

LINUX_HOST = "10.0.2.2"
PORT = 34567

def find_windows(class_name):
    hwnds = []
    print class_name
    try:
        hwnd = win32gui.FindWindow(class_name, None) 
    except:
        return hwnds 
    while hwnd:
        hwnds.append(hwnd) 
        hwnd = win32gui.FindWindowEx(None, hwnd, class_name, None)
    return hwnds

def print_hwnds(hwnds):
    for hwnd in hwnds:
        print 'hwnd:', hwnd, 'title:', win32gui.GetWindowText(hwnd)

def notify_linux(host, title, port=80): 
    title = title.encode('utf8')
    conn = httplib.HTTPConnection(host, port)
    query = {'title':title,} 
    url = '/' + "?" + urllib.urlencode(query)
    conn.request('GET', url)
    return conn.getresponse() 

last_hwnds = set()
while True: 
    names = ["SessionForm",
            "TeamForm", ]

    print '-' * 40
    hwnds = set()
    for name in names:
        hwnds |= set(find_windows(name))

    print_hwnds(hwnds)

    need_notifies = hwnds - last_hwnds

    for hwnd in need_notifies:
        title = win32gui.GetWindowText(hwnd)
        print hwnd, title
        notify_linux(LINUX_HOST, title.decode('gbk'), port=PORT)

    last_hwnds = hwnds

    time.sleep(1)


