import cv2
import numpy as np
import modules
import comm
import time

#cam = cv2.VideoCapture(0)

while(True):
	#_,frame = cam.read()		#read the image
	e1 = cv2.getTickCount()
	frdm = comm.FRDM('/dev/ttyACM0')
	for i in xrange(-10,10,1):
		frdm.write(M1=0,M2=0,steer=i,leds=4)
		time.sleep(0.02)
	for i in xrange(10,-10,-1):
		frdm.write(M1=0,M2=0,steer=i,leds=4)
		time.sleep(0.02)
	e2 = cv2.getTickCount()
	#print (e2-e1)/cv2.getTickFrequency()
	#cv2.imshow("frame",frame)
	# k = cv2.waitKey(1) & 0xFF
	# if k == 27:	#Tecla esc
	# 	break
# cam.release()
# cv2.destroyAllWindows()
