import cv2
import numpy as np
import modules
import comm

cam = cv2.VideoCapture(1)
frdm = comm.FRDM('/dev/ttyACM0')
while(True):
	_,frame = cam.read()		#read the image
	e1 = cv2.getTickCount()
	error = modules.readLine(frame,400)
	servo = modules.Pcontrol(error,(6/200.0))
	print servo
	frdm.write(M1=4,M2=4,steer=int(-servo),leds=4)
	frdm.write(M1=4,M2=4,steer=int(-servo),leds=4)
	frdm.write(M1=4,M2=4,steer=int(-servo),leds=4)
	e2 = cv2.getTickCount()
	#print (e2-e1)/cv2.getTickFrequency()*1000
	cv2.imshow("frame",frame)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:	#Tecla esc
		frdm.write(M1=0,M2=0,steer=int(-servo),leds=4)
		frdm.write(M1=0,M2=0,steer=int(-servo),leds=4)
		frdm.write(M1=0,M2=0,steer=int(-servo),leds=4)
		break
	if k == ord('p'):
		modules.sobel(frame,400)
cam.release()
cv2.destroyAllWindows()
