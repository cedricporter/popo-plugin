#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Hua Liang[Stupid ET] <et@everet.org>
#


import ctypes
from ctypes import *
import win32con
import time


user32 = windll.user32

hwnd = 590214

HSHELL_REDRAW = 6
WM_SHELL = 10


def SetWindowsHookEx(idHook, lpFunc, hMod, dwThreadId):
    WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long)
    return ctypes.windll.user32.SetWindowsHookExA(idHook, WINFUNC(lpFunc), hMod, dwThreadId)


def UnhookWindowsHookEx(hhk):
    return ctypes.windll.user32.UnhookWindowsHookEx(hhk)


def my_callback(nCode, wParam, lParam):
    print 'nCode', nCode, wParam, lParam
    if nCode == HSHELL_REDRAW and lParam:
        got_flashing_window_with_hwnd(wParam)

hook = SetWindowsHookEx(WM_SHELL, my_callback, None, 0)

time.sleep(5)

UnhookWindowsHookEx(hook)
