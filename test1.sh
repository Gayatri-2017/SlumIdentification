x=8109284.3
y=2164982

xdiff=87
ydiff=-50

x1=`expr x + xdiff`
x1=$(awk 'BEGIN{print x + xdiff}')

x1=`scale=4;$x+$xdiff`|
echo try
x1=$(echo x1 + xdiff | bc -l)
echo trydone
echo x1\=
echo $x1
echo xdone
y1='expr $y + $ydiff'

loopingvariable=0

:L1
echo %x
echo %x1
echo %y
echo %y1
echo NewLine

x=%x1
x1=%x1+87
y=%y1
y1=%y1-50

echo %x
echo %x1
echo %y
echo %y1
echo NewLine

loopingvariable=%loopingvariable%+1