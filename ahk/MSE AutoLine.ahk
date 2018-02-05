InputBox, a, Question 1, What page to start at?

x := a

F7::x--

F8:: 
SendInput, {Delete}{Enter}+[%x%+]{Enter}{PgDn}
x++
return

F10::SendInput {Delete}

^!\::SendInput {PgDn}

Esc:: ExitApp

