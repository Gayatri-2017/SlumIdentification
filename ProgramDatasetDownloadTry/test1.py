x = 8109284.3
y = 2164982.0

xdiff = 86.64
ydiff = -50.16

x1 = x + xdiff
y1 = y + ydiff

loopingvariable=0

import subprocess
process = subprocess.Popen('ping -c 3 192.168.0.100', shell=True)
cmd = 'qgis --project GoogleSatellite.qgs --snapshot image.png --width 1500 --height 1000 --extent ' + str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1) 
process = subprocess.Popen(cmd, shell=True)

for z in xrange(1,11):
	print x, y, x1, y1
	x = x1
	x1 = x1 + xdiff
	y = y1
	y1 = y1 - ydiff
	