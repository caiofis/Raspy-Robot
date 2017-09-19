import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

data = np.load('compressed_data.npy',encoding='bytes') # Load the data

p = np.random.permutation(len(data[0])) # Create a list of random permutations
data[0] = data[0][p] # Random Shuffle array
data[1] = data[1][p]

test, training = data[:,:100], data[:,100:]  # Split test and train data

print test[0][0].flatten().shape

plt.imshow(test[0][30])
plt.show()

x# = tf.placeholder(tf.float32, [None, 784])
#W = tf.Variable(tf.zeros([784, 10]))
#b = tf.Variable(tf.zeros([10]))
#y = tf.nn.softmax(tf.matmul(x, W) + b)

