#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.16.1
 Author:         Isamaza

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here
Func OpenChromeTab()
	ConsoleWrite("Opening chrome");
EndFunc
Func CloseTab()
	Send("^w")
EndFunc
Func Search($SearchQuery)
	Send("^l)
	ControlSend($SearchQuery)
EndFunc
Func GetOpenWindowUrl()
	$pageTitle = WinGetTitle("[ACTIVE]")
	$url = StringRegExp($pageTitle, "https?://[^\s]*", 3)
	ConsoleWrite("URL: " & $url[0] & @CRLF)

EndFunc
Func sendKeyboardInput($keyboardInput)
	Send($keyboardInput)

EndFunc



