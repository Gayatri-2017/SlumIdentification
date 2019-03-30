'''
x = 8109284.3
y = 2164982.0

xdiff = 86.64
ydiff = -50.16

x1 = x + xdiff
y1 = y + ydiff

loopingvariable=0

import subprocess
#process = subprocess.Popen('ping -c 3 192.168.0.100', shell=True)
#i = 0
#cmd = 'qgis --project GoogleSatellite.qgs --snapshot image' + str(i) + '.png --width 1500 --height 1000 --extent ' + str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1) 

for z in xrange(1,11):
	print x, y, x1, y1
	x = x1
	x1 = x1 + xdiff
	y = y1
	y1 = y1 - ydiff
	cmd = 'qgis --project GoogleSatellite.qgs --snapshot image' + str(i) + '.png --width 1500 --height 1000 --extent ' + str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1) 
	process = subprocess.Popen(cmd, shell=True)
	
'''

#x = 8109284.3
#y = 2164982.0
#xdiff = 86.64
#ydiff = -50.16


#x,y = 8109710.7,2185828.3
#x1,y1 = 8110342.0,2185499.8

x, y = 8107572,2177331
x1, y1 = 8108203.3, 2177002.5
xdiff,ydiff = 631.3, -328.5


x1 = x + xdiff
y1 = y + ydiff

loopingvariable=0

import subprocess
import time
#process = subprocess.Popen('ping -c 3 192.168.0.100', shell=True)
#cmd = 'qgis --project GoogleSatellite.qgs --snapshot image.png --width 1500 --height 1000 --extent ' + str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1) 
#process = subprocess.Popen(cmd, shell=True)
#process.terminate()

for z1 in range(1,5):
	#print x, y, x1, y1
	for z2 in range(1,2):
		cmd = 'qgis --project GoogleSatellite.qgs --snapshot image' + str(loopingvariable) + '.png --width 1200 --height 720 --extent ' + str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1) 
		process = subprocess.Popen(cmd, shell=True)
		time.sleep(10)
		x = x1
		x1 = x1 + xdiff
		loopingvariable += 1
	y = y1
	y1 = y1 + ydiff