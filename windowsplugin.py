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

def find_windows(class_name, window_name=None):
    hwnds = []
    try:
        hwnd = win32gui.FindWindow(class_name, window_name) 
    except:
        return hwnds 
    while hwnd:
        hwnds.append(hwnd) 
        hwnd = win32gui.FindWindowEx(None, hwnd, class_name, window_name)
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
    class_names = ["SessionForm",
            "TeamForm", ]
    window_names = [u"提示",
            u"兴趣组提示",]

    print '-' * 40
    hwnds = set()
    for name in class_names:
       hwnds |= set(find_windows(name))
    for name in window_names:
        hwnds |= set(find_windows(None, name.encode('gbk')))


    print_hwnds(hwnds)

    need_notifies = hwnds - last_hwnds

    for hwnd in need_notifies:
        title = win32gui.GetWindowText(hwnd)
        print hwnd, title
        notify_linux(LINUX_HOST, title.decode('gbk'), port=PORT)

    last_hwnds = hwnds

    time.sleep(1)


