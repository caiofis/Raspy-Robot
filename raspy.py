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
	error = modules.readLine(img,400)/32
	print error

cv2.destroyAllWindows()
