import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization
from tflearn.optimizers import Momentum

def simpleConv(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, 20, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 10, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = fully_connected(network, 100, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 10, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_simpleConv',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def vanilla(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    #network = local_response_normalization(network)
    network = fully_connected(network, 600, activation='relu')
    network = dropout(network, 0.5)
    network = fully_connected(network, 100, activation='relu')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_vanilla',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def smallVanilla(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    #network = local_response_normalization(network)
    network = fully_connected(network, 100, activation='relu')
    network = dropout(network, 0.5)
    network = fully_connected(network, 10, activation='relu')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_small_vanilla',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model

# Setup the model
WIDTH = 50
HEIGHT = 50
LR = 1e-2
EPOCHS = 200
#MODEL_NAME = 'raspy-car-{}-{}-{}-epochs.model'.format(LR, 'heuristic',EPOCHS)
#model = simpleConv(WIDTH, HEIGHT, LR)

LR = 1e-3
EPOCHS = 200
#MODEL_NAME = 'raspy-car-{}-{}-{}-epochs.model'.format(LR, 'vanilla',EPOCHS)
#model = vanilla(WIDTH, HEIGHT, LR)

MODEL_NAME = 'raspy-car-{}-{}-{}-epochs.model'.format(LR, 'smallVanilla',EPOCHS)
model = smallVanilla(WIDTH, HEIGHT, LR)


#Setup training data
train_data = np.load('training_data.npy')

train = train_data[:-100]
test = train_data[-100:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=log

model.save(MODEL_NAME)

