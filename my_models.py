#import tflearn
#from tflearn.layers.conv import conv_2d, max_pool_2d
#from tflearn.layers.core import input_data, dropout, fully_connected
#from tflearn.layers.estimator import regression
#from tflearn.layers.normalization import local_response_normalization
#from tflearn.optimizers import Momentum, RMSProp
import numpy as np
np.random.seed(2017)
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.losses import categorical_crossentropy, mse
from keras.optimizers import SGD,Adagrad



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
              optimizer=SGD(lr=lr, decay=10e-6, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
    model_name = "two_layers_vanilla-{}".format(lr)
    return model, model_name

def three_layers_vanilla(width, lr):
    model = Sequential()
    model.add(Dense(units=20,kernel_initializer='TruncatedNormal', activation='relu', input_dim=width * 1))
    model.add(Dropout(0.85))
    model.add(Dense(units=10,kernel_initializer='TruncatedNormal', activation='relu'))
    model.add(Dropout(0.85))
    model.add(Dense(units=5,kernel_initializer='TruncatedNormal', activation='relu'))
    model.add(Dropout(0.85))
    model.add(Dense(units=3, activation='softmax'))
    model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-5, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
    model_name = "three_layers_vanilla-{}".format(lr)
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
  model = Sequential()
  model.add(Conv2D(filters=20,kernel_size=(11, 11),
                 strides=4, activation='relu',
                 kernel_initializer='TruncatedNormal',
                 input_shape=(height,height,1)))
  model.add(MaxPooling2D(pool_size=(3, 3),strides=2))
  model.add(Conv2D(10, (5, 5), activation='relu',padding='same',kernel_initializer='TruncatedNormal'))
  model.add(MaxPooling2D(pool_size=(3, 3),strides=2))
  model.add(Dropout(0.25))
  model.add(Flatten())
  model.add(Dense(100, activation='relu',kernel_initializer='TruncatedNormal'))
  model.add(Dropout(0.5))
  model.add(Dense(10, activation='relu',kernel_initializer='TruncatedNormal'))
  model.add(Dropout(0.5))
  model.add(Dense(3, activation='softmax',kernel_initializer='TruncatedNormal'))

  model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-5,momentum=0.9, nesterov=True),
              metrics=['accuracy'])
  model_name = "simpleConv-{}".format(lr)
  return model, model_name

def claudioNet(width, height, lr):  # 76.92%
  model = Sequential()
  model.add(Conv2D(filters=20,kernel_size=(11, 11),
                 strides=4, activation='relu',
                 kernel_initializer='TruncatedNormal',
                 input_shape=(height,height,1)))
  model.add(Conv2D(20, (11, 11), strides=4, activation='relu',padding='same',
            kernel_initializer='TruncatedNormal'))
  model.add(Conv2D(20, (11, 11), strides=4, activation='relu',padding='same',
            kernel_initializer='TruncatedNormal'))
  model.add(Flatten())
  model.add(Dense(10, activation='relu',kernel_initializer='TruncatedNormal'))
  model.add(Dropout(0.5))
  model.add(Dense(3, activation='softmax',kernel_initializer='TruncatedNormal'))

  model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-5,momentum=0.9, nesterov=True),
              metrics=['accuracy'])
  model_name = "Claudios_net-{}".format(lr)
  return model, model_name


def Hinton(width,height,lr): # 616 par 71.46% 71.13%
    model = Sequential()     # 706 par 71.83%
    model.add(Conv2D(filters=5,kernel_size=(9, 9),
                 strides=4, activation='relu', padding='valid',
                 kernel_initializer='TruncatedNormal',
                 input_shape=(width,height,1)))
    model.add(Conv2D(3, (3, 3), strides=3, activation='relu',padding='valid',
              kernel_initializer='TruncatedNormal'))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(5, activation='relu',kernel_initializer='TruncatedNormal'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax',kernel_initializer='TruncatedNormal'))

    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-5,momentum=0.9, nesterov=True),
              metrics=['accuracy'])

    model_name = "Conv1-{}".format(lr)
    return model, model_name

def Conv2(width,height,lr):  # 1343 parameters  77.33%  76.38%
    model = Sequential()     # 1,973 par 76.79%
    model.add(Conv2D(filters=5,kernel_size=(15, 15),
                 strides=5, activation='relu', padding='valid',
                 kernel_initializer='TruncatedNormal',
                 input_shape=(width,height,1)))
    model.add(Conv2D(5, (2, 2), strides=1, activation='relu',padding='valid',
              kernel_initializer='TruncatedNormal'))
    model.add(Dropout(0.5))
    model.add(Flatten())
    #model.add(Dense(5, activation='relu',kernel_initializer='TruncatedNormal'))
    #model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax',kernel_initializer='TruncatedNormal'))

    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-5,momentum=0.9, nesterov=True),
              metrics=['accuracy'])

    model_name = "Conv2-{}".format(lr)
    return model, model_name

def Conv3(width,height,lr):  # 940 parameters  77.96% 75.83%
    model = Sequential()     # 1,588 par 75.67%
    model.add(Conv2D(filters=5,kernel_size=(10, 10),
                 strides=2, activation='relu', padding='valid',
                 kernel_initializer='TruncatedNormal',
                 input_shape=(width,height,1)))
    model.add(Conv2D(6, (3, 3), strides=2, activation='relu',padding='valid',
              kernel_initializer='TruncatedNormal'))
    model.add(Conv2D(3, (2, 2), strides=1, activation='relu',padding='valid',
              kernel_initializer='TruncatedNormal'))
    model.add(Dropout(0.25))
    model.add(Flatten())
    #model.add(Dense(5, activation='relu',kernel_initializer='TruncatedNormal'))
    #model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax',kernel_initializer='TruncatedNormal'))

    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-5,momentum=0.9, nesterov=True),
              metrics=['accuracy'])

    model_name = "Conv3-{}".format(lr)
    return model, model_name

def Conv4(width,height,lr):  # 1,014 parameters
    model = Sequential()     # 2,094 par 76.38%
    model.add(Conv2D(filters=5,kernel_size=(10, 10),
                 strides=2, activation='relu', padding='valid',
                 kernel_initializer='TruncatedNormal',
                 input_shape=(width,height,1)))
    model.add(Conv2D(6, (3, 3), strides=2, activation='relu',padding='valid',
              kernel_initializer='TruncatedNormal'))
    model.add(Conv2D(3, (2, 2), strides=1, activation='relu',padding='valid',
              kernel_initializer='TruncatedNormal'))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(5, activation='relu',kernel_initializer='TruncatedNormal'))
    model.add(Dropout(0.5))
    model.add(Dense(3, activation='softmax',kernel_initializer='TruncatedNormal'))

    model.compile(loss=categorical_crossentropy,
              optimizer=SGD(lr=lr, decay=10e-6,momentum=0.9, nesterov=True),
              metrics=['accuracy'])

    model_name = "Conv4-{}".format(lr)
    return model, model_name

def Disc_to_Cont(width,lr):
    model = Sequential()
    model.add(Dense(5,activation='relu',input_dim=(width),kernel_initializer='normal'))
    model.add(Dropout(0.5))
    model.add(Dense(1,activation='tanh',kernel_initializer='TruncatedNormal'))
    model.compile(loss='mean_absolute_error',optimizer=Adagrad())
    model_name = "Disc_to_Cont-{}".format(lr)
    return model, model_name

def Disc_to_Cont_small(width,lr):
    model = Sequential()
    model.add(Dense(2,activation='relu',input_dim=(width),kernel_initializer='normal'))
    model.add(Dropout(0.5))
    model.add(Dense(1,activation='tanh',kernel_initializer='TruncatedNormal'))
    model.compile(loss='mean_absolute_error',optimizer=Adagrad())
    model_name = "Disc_to_Cont_small-{}".format(lr)
    return model, model_name
