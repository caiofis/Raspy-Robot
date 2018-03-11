import numpy as np
np.random.seed(2017)

# Load training data
train_data = np.load('data/doubleLineData.npy')
#train_data = np.load('data/singleLineData.npy')
#train_data = np.load('data/ROIData.npy')
#train_data = np.load('data/ImageData.npy')
#train_data = np.load('data/training_data.npy')
np.random.shuffle(train_data)

import tensorflow as tf
import matplotlib.pyplot as plt
import my_models
from keras.callbacks import TensorBoard,ModelCheckpoint
import cPickle as pickle

import time

# Setup the model
WIDTH = 100
HEIGHT = 1
LR = 1e-4
EPOCHS = 50

model,model_name = my_models.vanilla(WIDTH, LR)
#model,model_name = my_models.small_vanilla(WIDTH, LR)
#model,model_name = my_models.two_layers_vanilla(WIDTH, LR)
#model,model_name = my_models.three_layers_vanilla(WIDTH, LR)
#model,model_name = my_models.big_vanilla(WIDTH, LR)

#model, model_name = my_models.Hinton(WIDTH, HEIGHT, LR)
#model, model_name = my_models.Conv2(WIDTH, HEIGHT, LR)
#model, model_name = my_models.Conv3(WIDTH, HEIGHT, LR)
#model, model_name = my_models.Conv4(WIDTH, HEIGHT, LR)
#model,model_name = my_models.claudioNet(WIDTH,HEIGHT,LR)
model.summary() #Show models details




train = train_data[:-2400]
test = train_data[-2400:]

#X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
#x_train = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
x_train = np.array([i[0] for i in train]).reshape(-1,WIDTH) #Single Line
y_train = [i[1] for i in train]

#x_test = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
x_test = np.array([i[0] for i in test]).reshape(-1,WIDTH) # Single Line
y_test = [i[1] for i in test]

# define the callbacks
tensorboard = TensorBoard(log_dir='./logs/doubleLine/{}-{}-epochs'.format(model_name,EPOCHS))
checkpoint = ModelCheckpoint('./logs/doubleLine/{}-{}-epochs/weights-improvement.hdf5'.format(model_name,EPOCHS), verbose=1, save_best_only=True)

# Train models
start = time.time()
history = model.fit(x_train,y_train, epochs=EPOCHS, validation_data=(x_test, y_test),
          verbose = 2,callbacks=[tensorboard,checkpoint],shuffle=False)
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=2400)

end = time.time()
with open('./logs/doubleLine/{}-{}-epochs/results.pickle'.format(model_name,EPOCHS), 'wb') as f:
    pickle.dump(history.history, f)

print ("Run time: {}".format(end-start))
# tensorboard --logdir=log
#model.save(MODEL_NAME)
