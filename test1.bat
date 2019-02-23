set /A x = 8109284
set /A y = 2164982

set /A xdiff = 87
set /A ydiff = -50

set /A x1 = %x% + %xdiff%
set /A y1=%y-%ydiff


set /A loopingvariable=0

:L1
echo. %x%
echo. %x1%
echo. %y%
echo. %y1%
echo NewLine

set x=%x1%
set x1=%x1%+87
set y=%y1%
set y1=%y1%-50

echo. %x%
echo. %x1%
echo. %y%
echo. %y1%
echo NewLine

set loopingvariable=%loopingvariable%+1
rem if %loopingvariable% leq 10 goto L1