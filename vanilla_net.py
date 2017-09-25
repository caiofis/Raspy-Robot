import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

data = np.load('compressed_data.npy',encoding='bytes') # Load the data

p = np.random.permutation(len(data[0])) # Create a list of random permutations
data[0] = data[0][p] # Random Shuffle array
data[1] = data[1][p]
print data[0][0].shape
test_image = data[0][0]
# Flattering the data
for i in xrange(len(data[0])):
	data[0][i] = data[0][i].flatten()
	if data[1][i] > 0.1:
		data[1][i] = [1]
	else: 
		data[1][i] = [0]
print data[1]
test, training = data[:,:100], data[:,100:]  # Split test and train data

n_samples = len(training[0]) 

x = tf.placeholder(tf.float32, [None, 36864])
W1 = tf.Variable(tf.zeros([36864, 1]))
b1 = tf.Variable(tf.zeros([1]))
#h1 = tf.nn.relu(tf.matmul(X, W1) + b1)
#W2 = tf.Variable(tf.zeros([10,3]))
#b2 = tf.Variable(tf.zeros([1]))
y = tf.nn.softmax(tf.matmul(x, W1) + b1)

y_ = tf.placeholder(tf.float32, [None, 1]) # Correct values
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(200):
  batch_xs, batch_ys = training[0],training[1]
  batch_xs = np.vstack([np.expand_dims(x, 0) for x in batch_xs])
  batch_ys = np.vstack([np.expand_dims(x, 0) for x in batch_ys])
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
  if _==0:
	print(sess.run(accuracy,feed_dict={x: batch_xs, y_: batch_ys}))
  if _==1:#_%100==0:
	print(sess.run(accuracy,feed_dict={x: batch_xs, y_: batch_ys}))

batch_xs, batch_ys = test[0],test[1]
batch_xs = np.vstack([np.expand_dims(x, 0) for x in batch_xs])
batch_ys = np.vstack([np.expand_dims(x, 0) for x in batch_ys])
print(sess.run(accuracy,feed_dict={x: batch_xs, y_: batch_ys}))

print(sess.run(y,feed_dict={x: batch_xs[:5], y_: batch_ys[:5]}))
plt.imshow(test_image)
plt.show()

