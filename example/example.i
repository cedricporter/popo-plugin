/* File: example.i */
%module example

%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
#include <windows.h>
#include <stdio.h>

%}

%wrapper %{

LRESULT CALLBACK cMyCallback(int code, WPARAM wParam, LPARAM lParam)
{
    printf("%d %d %d", code, wParam, lParam);

    return 0;
}

int start()
{
    HINSTANCE hMod;

    printf("in start()");

    Py_BEGIN_ALLOW_THREADS
    hMod = GetModuleHandle("_etHook.pyd");
    Py_END_ALLOW_THREADS;

    Py_BEGIN_ALLOW_THREADS
    SetWindowsHookEx(WH_SHELL, cMyCallback, (HINSTANCE)hMod, 0);
    Py_END_ALLOW_THREADS;

    return 0;
}

%}

int fact(int n);
int start();
