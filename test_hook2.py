#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import win32con
import win32gui
import ctypes
from ctypes import wintypes

# container class for global hook
# this will store the HHOOK id and mouse information


class Hook:
    def __init__(self):
        self.hook = 0
        self.m_struct = None


class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [("pt", wintypes.POINT),
                ("mouseData", ctypes.c_long),
                ("flags", ctypes.c_long),
                ("time", ctypes.c_long),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]


def CopyMemory(Destination, Source):
    Source = ctypes.c_void_p(Source)
    ctypes.windll.kernel32.RtlMoveMemory(ctypes.addressof(Destination), Source, ctypes.sizeof(Destination))


def PostQuitMessage(nMsg):
    return ctypes.windll.user32.PostQuitMessage(nMsg)


def GetModuleHandle(lpModuleName):
    return ctypes.windll.kernel32.GetModuleHandleA(lpModuleName)


def CallNextHookEx(hhk, nCode, wParam, lParam):
    return ctypes.windll.user32.CallNextHookEx(hhk, nCode, wParam, lParam)


def SetWindowsHookEx(idHook, lpFunc, hMod, dwThreadId):
    WINFUNC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long)
    return ctypes.windll.user32.SetWindowsHookExA(idHook, WINFUNC(lpFunc), hMod, dwThreadId)


def UnhookWindowsHookEx(hhk):
    return ctypes.windll.user32.UnhookWindowsHookEx(hhk)


# create instance of global mouse hook class
mll_hook = Hook()
mll_hook.m_struct = MSLLHOOKSTRUCT()

# mouse hook callback. intercept mouse events


def LowLevelMouseProc(nCode, wParam, lParam):
    print nCode, wParam, lParam

    if nCode == win32con.HC_ACTION:
        # lparam holds the starting address of the mouse hook structure
        # call copymemory so that m_struct class points to the mouse structure pool
        CopyMemory(mll_hook.m_struct, lParam)
        # print out the cursors x and y screen position
        if wParam == win32con.WM_MBUTTONUP:
            PostQuitMessage(0)

        if wParam == win32con.WM_LBUTTONUP:    # WM_RBUTTONUP
            print "x = [%d]/ty = [%d]" % (mll_hook.m_struct.pt.x, mll_hook.m_struct.pt.y)

    return CallNextHookEx(mll_hook.hook, nCode, wParam, lParam)


if __name__ == '__main__':
    print "Press the middle mouse button to exit "
    try:
        mll_hook.hook = SetWindowsHookEx(win32con.WH_MOUSE_LL,
                                         LowLevelMouseProc,
                                         GetModuleHandle(0),
                                         0)
    except Exception, err:
        print err
    # set up a message queue, you can use any valid message loop tkinter, pygtk and wxpythons message loops all work
    win32gui.PumpMessages()
    # unhook the mouse hook
    UnhookWindowsHookEx(mll_hook.hook)
