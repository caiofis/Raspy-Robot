import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization
from tflearn.optimizers import Momentum, RMSProp

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

def vanilla(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    #network = local_response_normalization(network)
    network = fully_connected(network, 4, activation='relu')
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_vanilla',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def singleLayer(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_vanilla',
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

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_small_vanilla',
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

def deepTesla(width,height,lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, nb_filter=8, filter_size=3, strides=3, activation='relu')
    network = conv_2d(network, 8, 3, strides=3, activation='relu')
    network = conv_2d(network, 8, 3, strides=3, activation='relu')
    network = max_pool_2d(network, 4, strides=2)
    network = dropout(network, 0.5)
    network = fully_connected(network, 3, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_deepTesla',
                        max_checkpoints=3, tensorboard_verbose=2, tensorboard_dir='log')

    return model

def default_categorical(width,height,lr):

    network = input_data(shape=[None, width, height, 1], name='input')# First layer, input layer
    network = conv_2d(network, nb_filter=24, filter_size=5, strides=2, activation='relu') # 24 features, 5 pixel x 5 pixel kernel (convolution, feauture) window, 2wx2h stride, relu activation
    network = conv_2d(network, nb_filter=32, filter_size=5, strides=2, activation='relu') # 32 features, 5px5p kernel window, 2wx2h stride, relu activatiion
    network = conv_2d(network, nb_filter=64, filter_size=5, strides=2, activation='relu') # 64 features, 5px5p kernal window, 2wx2h stride, relu
    network = conv_2d(network, nb_filter=64, filter_size=3, strides=2, activation='relu') # 64 features, 3px3p kernal window, 2wx2h stride, relu
    network = conv_2d(network, nb_filter=64, filter_size=3, strides=1, activation='relu') # 64 features, 3px3p kernal window, 1wx1h stride, relu

    # Possibly add MaxPooling (will make it less sensitive to position in image).  Camera angle fixed, so may not to be needed
    network = fully_connected(network, 100, activation='relu') # Classify the data into 100 features, make all negatives 0
    network = dropout(network, 0.1) # Randomly drop out (turn off) 10% of the neurons (Prevent overfitting)
    network = fully_connected(network, 50, activation='relu') # Classify the data into 50 features, make all negatives 0
    network = dropout(network, 0.1) # Randomly drop out (turn off) 10% of the neurons (Prevent overfitting)
    #categorical output of the angle
    network = fully_connected(network, 3, activation='softmax', name='output')        # Connect every input with every output and output 15 hidden units. Use Softmax to give percentage. 15 categories and find best one based off percentage 0.0-1.0

    #continous output of throttle
    #throttle_out = Dense(1, activation='relu', name='throttle_out')(x)      # Reduce to 1 number, Positive number only

    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')
    model = tflearn.DNN(network, checkpoint_path='checkpoints/model_default_cat',
                        max_checkpoints=3, tensorboard_verbose=2, tensorboard_dir='log')

    return model
