import cv2
import numpy as np
import modules

cam = cv2.VideoCapture(0)

while(True):
	_,frame = cam.read()		#read the image
	e1 = cv2.getTickCount()
	#frame = modules.ROIfilteredCanny(frame,0,400,640,450)
	print modules.readLine(frame,400)
	e2 = cv2.getTickCount()
	#print (e2-e1)/cv2.getTickFrequency()*1000
	cv2.imshow("frame",frame)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:	#Tecla esc
		break
	if k == ord('p'):
		modules.sobel(frame,400)
cam.release()
cv2.destroyAllWindows()
