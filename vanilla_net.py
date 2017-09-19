import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

data = np.load('compressed_data.npy',encoding='bytes') # Load the data

data = np.random.shuffle(data.flat) # Random Shuffle array

test, training = data[:,:100], data[:,100:]  # Split test and train data
print test.shape
print test[0][0].shape
print test[1][30]
plt.imshow(test[0][30])
plt.show()

