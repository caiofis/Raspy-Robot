import cv2
import numpy as np
import matplotlib.pyplot as plt

def filteredCanny(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray scale
	#Apply a bilateral filter
	filtered = cv2.bilateralFilter(gray,9,75,75)
	# create a CLAHE object (Arguments are optional).
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	filtered = clahe.apply(filtered)
	#find the thresh to the Canny and apply it
	thresh_max = filtered.mean()
	thresh_min = thresh_max/2
	canny = cv2.Canny(filtered,thresh_min,thresh_max)
	return canny

def ROIfilteredCanny(img,x,y,w,h):
	roi = img[y:h, x:w]
	roi = filteredCanny(roi)
	return roi

def findLine(img,y,h):
	roi = img[y-(h/2):y+(h/2), 0:]
	line = roi[h/2]
	cv2.line(img,(0,y),(640,y),(255,0,0),2)
	
	return roi
