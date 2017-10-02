import numpy as np
import cv2
from random import shuffle

"""This code reduct the bias in the data set"""

data = np.load('compressed_data.npy',encoding='bytes') # Load the data

p = np.random.permutation(len(data[0])) # Create a list of random permutations
data[0] = data[0][p] # Random Shuffle array
data[1] = data[1][p]

print data.shape

lefts = []
rights = []
forwards = []

# Flattering the data
for i in xrange(len(data[0])):		
	if data[1][i] > 2:
		rights.append([data[0][i],[1,0,0]])
	elif data[1][i] < -2:
		lefts.append([data[0][i],[0,0,1]])
	else:
		forwards.append([data[0][i],[0,1,0]])



print len(lefts) , len(rights), len(forwards)
forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]
final_data = forwards + lefts + rights
print len(final_data)

shuffle(final_data)

np.save('training_data.npy', final_data)
