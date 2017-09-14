import numpy as np
import cv2

"""This code reduct the dataset images climbing two levels in the 
   Gaussian Pyramid"""

data = np.load('data.npy',encoding='bytes') # Load the data

images = []
for im in data[0]:
	compressed = cv2.pyrDown(im)
	compressed = cv2.pyrDown(compressed)
	images.append(compressed)
data[0] = images
np.save('compressed_data',data)
