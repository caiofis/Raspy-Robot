from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
rawCapture = PiRGBArray(camera,size=(640,480))

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	img = frame.array
	#take the image to the gray scale
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	filtered = cv2.bilateralFilter(gray,9,75,75)
	thresh_max = filtered.mean()
	thresh_min = thresh_max/2
	canny = cv2.Canny(filtered,thresh_min,thresh_max)
	
	# clear the stream in preparation for the next frame
        rawCapture.truncate(0)

	cv2.imshow("frame",canny)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:	#Tecla esc
		break

cv2.destroyAllWindows()
