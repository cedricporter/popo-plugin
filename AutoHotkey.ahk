; borrow from http://www.autohotkey.com/board/topic/36510-detect-flashingblinking-window-on-taskbar/?p=229583

DetectHiddenWindows, On
Script_Hwnd := WinExist("ahk_class AutoHotkey ahk_pid " DllCall("GetCurrentProcessId"))
DetectHiddenWindows, Off

; Register shell hook to detect flashing windows.
DllCall("RegisterShellHookWindow", "uint", Script_Hwnd)
OnMessage(DllCall("RegisterWindowMessage", "str", "SHELLHOOK"), "ShellEvent")
;...



ShellEvent(wParam, lParam) {
    team_white_list := ["A平台服务部 - 兴趣组", "2013年7月web新人 - 兴趣组"]

    if (wParam = 0x8006) ; HSHELL_FLASH
    {   ; lParam contains the ID of the window which flashed:

	WinGetTitle, win_title, ahk_id %lParam%
	WinGetClass, win_class, ahk_id %lParam%
	if (win_class = "SessionForm")
	{
		; MsgBox, %win_title%, %win_class%
		run pythonw "Z:/popo-plugin/win-notify.py" "%win_title%"
	}

	if (win_class = "TeamForm")
	{
		
		for i, element in team_white_list 
                {
		    ; MsgBox, %win_title%, %win_class%, %element%
		    if (element = win_title) {
			    run pythonw "Z:/popo-plugin/win-notify.py" "%win_title%"
		    }
		}
	}
 
    }
}




