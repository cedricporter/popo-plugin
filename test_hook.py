#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Hua Liang[Stupid ET] <et@everet.org>
#

import win32api

import win32con

from ctypes import windll

import time

x, y = 10, 10


#鼠标左键

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)

time.sleep(0.05)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)


#鼠标右键

win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y)

time.sleep(0.05)

win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y)
