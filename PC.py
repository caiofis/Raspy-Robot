import cv2
import numpy as np
import modules
import comm

cam = cv2.VideoCapture(0)
frdm = comm.FRDM('/dev/ttyACM0')
encoder = []
while(True):
	_,frame = cam.read()		#read the image
	e1 = cv2.getTickCount()
	error = modules.readLine(frame,400)
	servo = modules.Pcontrol(error,(6/200.0))
	print servo
	encoder.append(frdm.write(M1=4,M2=4,steer=int(-servo),leds=4))
	e2 = cv2.getTickCount()
	#print (e2-e1)/cv2.getTickFrequency()*1000
	cv2.imshow("frame",frame)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:	#Tecla esc
		encoder.append(frdm.write(M1=0,M2=0,steer=0,leds=0))
		print encoder
		break
	if k == ord('p'):
		modules.sobel(frame,400)
cam.release()
cv2.destroyAllWindows()
