import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while(True):
	_,frame = cam.read()		#read the image
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #convert to gray scale
	#Apply a bilateral filter
	filtered = cv2.bilateralFilter(gray,9,75,75)
	# create a CLAHE object (Arguments are optional).
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	filtered = clahe.apply(filtered)
	#find the thresh to the Canny and apply it
	thresh_max = filtered.mean()
	thresh_min = thresh_max/2
	canny = cv2.Canny(filtered,thresh_min,thresh_max)

	cv2.imshow("frame",canny)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:	#Tecla esc
		break
cam.release()
cv2.destroyAllWindows()
