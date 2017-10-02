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
