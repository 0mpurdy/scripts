PageNumber = 66
OpenPage = {
ClosePage = }
q::
  SendRaw %OpenPage%%PageNumber%%ClosePage%
  PageNumber -= 1
  Send {enter}
Return

Escape::
ExitApp
Return