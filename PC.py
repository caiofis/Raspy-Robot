import cv2
import numpy as np
import modules
import comm

cam = cv2.VideoCapture(0)
frdm = comm.FRDM('/dev/ttyACM0')


while(True):
	_,frame = cam.read()		#read the image
	e1 = cv2.getTickCount()
	#frame = modules.ROIfilteredCanny(frame,0,400,640,450)
	error = modules.readLine(frame,400)/32
	print error
	frdm.write(M1=0,M2=0,steer=error,leds=3)
	e2 = cv2.getTickCount()
	#print (e2-e1)/cv2.getTickFrequency()
	cv2.imshow("frame",frame)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:	#Tecla esc
		break
cam.release()
cv2.destroyAllWindows()
