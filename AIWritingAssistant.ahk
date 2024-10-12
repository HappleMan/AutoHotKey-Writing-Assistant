askApi() {
    valid := 0
    Send, ^c
    USERINPUT := Clipboard
    Send {BackSpace}
    endpoint:= "https://127.0.0.1:5000/llama?system=Generate+the+following+request+with+no+additional+explanation&user=" + USERINPUT
    req := ComObjCreate("WinHttp.WinHttpRequest.5.1")
    req.Open("POST", endpoint, False)
    req.Option(4) := 0x0100  + 0x0200 + 0x1000 + 0x2000
    req.Send(data)
    req.WaitForResponse()
    resp := req.responseText
    Return resp
}

^'::
    result := askApi()
    StrReplace(result, "\\n", "\n")
    Clipboard := result
    Send, ^v
    Return

^;::
    ExitApp