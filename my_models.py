#import tflearn
#from tflearn.layers.conv import conv_2d, max_pool_2d
#from tflearn.layers.core import input_data, dropout, fully_connected
#from tflearn.layers.estimator import regression
#from tflearn.layers.normalization import local_response_normalization
#from tflearn.optimizers import Momentum, RMSProp
import numpy as np
np.random.seed(20)
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.losses import categorical_crossentropy
from keras.optimizers import SGD



def vanilla(width, lr):
    model = Sequential()
    model.add(Dense(units=15,kernel_initializer='TruncatedNormal', activation='relu', input_dim=width * 1))
    model.add(Dropout(0.85))
    model.add(Dense(units=3,kernel_initializer='TruncatedNormal', activation='softmax'))
    model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr,decay=10e-6, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
    model_name = "vanilla-{}".format(lr)
    return model, model_name

def small_vanilla(width, lr):
    model = Sequential()
    model.add(Dense(units=4,kernel_initializer='TruncatedNormal', activation='relu', input_dim=width * 1))
    model.add(Dropout(0.85))
    model.add(Dense(units=3,kernel_initializer='TruncatedNormal', activation='softmax'))
    model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
    model_name = "small_vanilla-{}".format(lr)
    return model, model_name

def two_layers_vanilla(width, lr):
    model = Sequential()
    model.add(Dense(units=15,kernel_initializer='TruncatedNormal', activation='relu', input_dim=width * 1))
    model.add(Dropout(0.85))
    model.add(Dense(units=7,kernel_initializer='TruncatedNormal', activation='relu'))
    model.add(Dropout(0.85))
    model.add(Dense(units=3, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
    model_name = "two_layers_vanilla-{}".format(lr)
    return model, model_name

def big_vanilla(width,  lr):
    model = Sequential()
    model.add(Dense(units=100,kernel_initializer='TruncatedNormal',
              activation='relu', input_dim=width * 1))
    model.add(Dropout(0.85))
    model.add(Dense(units=10,kernel_initializer='TruncatedNormal',
              activation='relu'))
    model.add(Dropout(0.85))
    model.add(Dense(units=3,kernel_initializer='TruncatedNormal', activation='softmax'))
    model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
    model_name = "big_vanilla-{}".format(lr)
    return model, model_name


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

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_simpleConv',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def claudioNet(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, 20, 11, strides=4, activation='relu')
    network = conv_2d(network, 20, 11, strides=4, activation='relu')
    network = conv_2d(network, 20, 11, strides=4, activation='relu')
    network = fully_connected(network, 10, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_claudio',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def Hinton(width,height,lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, nb_filter=5, filter_size=9, strides=4, activation='relu')
    network = conv_2d(network, 3, 3, strides=3, activation='relu')
    #network = fully_connected(network, 5, activation='relu')
    #network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_Hinton',
                        max_checkpoints=3, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def simpConv2(width,height,lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, 10, 5, strides=4, activation='relu')
    network = conv_2d(network, 5, 4, strides=3, activation='relu')
    network = conv_2d(network, 1, 3, strides=2, activation='relu')
    network = fully_connected(network, 10, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_simpleConv2',
                        max_checkpoints=3, tensorboard_verbose=2, tensorboard_dir='log')

    return model
