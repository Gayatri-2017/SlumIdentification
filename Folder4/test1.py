x, y = 8106849,2167219
x0, y0 = 8106849,2167219
xdiff,ydiff = 631.3, -328.5
x1, y1 = x0+xdiff, y0+ydiff

loopingvariable=0

import subprocess
import time

for z1 in range(1,77):
	for z2 in range(1,24):
		cmd = 'qgis --project GoogleSatellite.qgs --snapshot image' + str(loopingvariable) + '.jpg --width 1200 --height 720 --extent ' + str(x) + ',' + str(y) + ',' + str(x1) + ',' + str(y1) 
		process = subprocess.Popen(cmd, shell=True)
		time.sleep(20)
		x = x1
		x1 = x1 + xdiff
		loopingvariable += 1
	y = y1
	y1 = y1 + ydiff
	x = x0
	x1 = x + xdiff


#8121625,2141945

#xrange = 24
#yrange = 77

#total images = 77 * 24 = 1848
#total time = 1848 * 20 = 36960 sec = 616 min = 10.3 hrs
# time for 24 images = 24 * 20 = 480 sec = 8 min
