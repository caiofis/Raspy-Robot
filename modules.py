import cv2
import numpy as np
import matplotlib.pyplot as plt

def filteredCanny(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray scale
	#Apply a bilateral filter
	#filtered = cv2.bilateralFilter(gray,9,75,75)
	filtered = cv2.GaussianBlur(gray,(5,5),0)
	# create a CLAHE object (Arguments are optional).
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(5,5))
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

def sobel(img, y):
	roi = img[y-(1):y+(1), 0:]		#Cut a ROI of the image around the line
	roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY) #convert to gray scale
	roi = cv2.Sobel(roi,cv2.CV_64F,1,0,ksize = -1)
	line = roi[1]
	maxi = np.argmax(line)
	mini = np.argmin(line)
	center = (maxi+mini)/2
	print center
	#plt.plot(range(len(line)),line)
	#plt.show()
def readLineDebug(img,y,h = 5):
	roi = img[y-(h/2):y+(h/2), 0:]		#Cut a ROI of the image around the line
	roi = filteredCanny(roi)		#Canny edge detector
	line = roi[h/2]				#array of the line
	edges = []				#list of edges
	length = len(line)			#length of the line
	error = 0
	for i in xrange(length):		#find the edges
		if line[i]==255:
			edges.append(i)

	cv2.line(img,(0,y),(640,y),(255,0,0),2) #draw the line
	for i in edges:				#draw the edges founds
		cv2.circle(img,(i,y),3,(0,0,255),-1)
	if len(edges) > 0:
	#if any edge was found draw the centroid of the edges
	#and calc the ortogonal deviation from the center of the image
		cv2.circle(img,(sum(edges)/len(edges),y),3,(0,255,0),-1)
		error = (length/2) - sum(edges)/len(edges)
	return error
