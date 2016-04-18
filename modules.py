import cv2
import numpy as np
import matplotlib.pyplot as plt


def sobel(img, y):
	roi = img[y-(1):y+(1), 0:]		#Cut a ROI of the image around the line
	roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY) #convert to gray scale
	roi = cv2.Sobel(roi,cv2.CV_64F,1,0,ksize = -1)
	line = roi[1]
	return line

def readLine(img,y):
	line = sobel(img,y)
	maxi = np.argmax(line)		#Find a edge of the line
	mini = np.argmin(line)		#Find the second edge of the line
	center = (maxi+mini)/2		#Calculate the centroid of the edges
	#draw a circle in the edges for debuging
	cv2.circle(img,(maxi,y),3,(0,0,255),-1)
	cv2.circle(img,(mini,y),3,(0,0,255),-1)
	# error = diference from the center of the line and the center of the image
	error = ((len(line)/2) - center)
	return error
	#plt.plot(range(len(line)),line)
	#plt.show()

def Pcontrol(error,Kp,error_max = 220):
		if error > error_max:
			error = error_max
		if error < -error_max:
			error = -error_max
		return Kp*error
