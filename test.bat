set /A x = 8109284.3
set /A y = 2164982.0

set /A x1=%x+86.64
set /A y1=%y-50.16

set /A loopingvariable=0

:L1
echo. %x
echo. %x1
echo. %y
echo. %y1
echo NewLine

set x=%x1
set x1=%x1+86.64
set y=%y1
set y1=%y1-50.16
set loopingvariable=%loopingvariable+1
if %loopingvariable leq 10 goto L1