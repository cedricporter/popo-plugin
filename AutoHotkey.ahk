; borrow from http://www.autohotkey.com/board/topic/36510-detect-flashingblinking-window-on-taskbar/?p=229583

DetectHiddenWindows, On
Script_Hwnd := WinExist("ahk_class AutoHotkey ahk_pid " DllCall("GetCurrentProcessId"))
DetectHiddenWindows, Off

; Register shell hook to detect flashing windows.
DllCall("RegisterShellHookWindow", "uint", Script_Hwnd)
OnMessage(DllCall("RegisterWindowMessage", "str", "SHELLHOOK"), "ShellEvent")
;...

ShellEvent(wParam, lParam) {
    if (wParam = 0x8006) ; HSHELL_FLASH
    {   ; lParam contains the ID of the window which flashed:

	WinGetTitle, win_title, ahk_id %lParam%
	WinGetClass, win_class, ahk_id %lParam%
	if (win_class = "SessionForm" or win_class = "TeamForm")
	{
		; MsgBox, %win_title%, %win_class%
		run pythonw "Z:/popo-plugin/win-notify.py" "%win_title%"
	}

    }
}
