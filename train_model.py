import numpy as np
np.random.seed(20)

# Load training data
train_data = np.load('data/doubleLineData.npy')
#train_data = np.load('data/singleLineData.npy')
np.random.shuffle(train_data)

import tensorflow as tf
import matplotlib.pyplot as plt
import my_models
from keras.callbacks import TensorBoard,ModelCheckpoint


import time

# Setup the model
WIDTH = 50
HEIGHT = 50
LR = 1e-4
EPOCHS = 50

#model,model_name = my_models.vanilla(WIDTH*2, LR)
#model,model_name = my_models.small_vanilla(WIDTH*2, LR)
#model,model_name = my_models.two_layers_vanilla(WIDTH*2, LR)
model,model_name = my_models.big_vanilla(WIDTH*2, LR)

model.summary() #Show models details




train = train_data[:-2400]
test = train_data[-2400:]

#X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
x_train = np.array([i[0] for i in train])#.reshape(-1,1,WIDTH,1)
y_train = [i[1] for i in train]

x_test = np.array([i[0] for i in test])#.reshape(-1,WIDTH,HEIGHT,1)
y_test = [i[1] for i in test]

# define the callbacks
tensorboard = TensorBoard(log_dir='./logs/doubleLine/{}-{}-epochs'.format(model_name,EPOCHS))
checkpoint = ModelCheckpoint('./logs/doubleLine/{}-{}-epochs/weights-improvement.hdf5'.format(model_name,EPOCHS), verbose=1, save_best_only=True)

# Train models
start = time.time()
model.fit(x_train,y_train, epochs=EPOCHS, validation_data=(x_test, y_test),
    verbose = 2,callbacks=[tensorboard,checkpoint],shuffle=False)
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=1000)

end = time.time()
print ("Run time: {}".format(end-start))
# tensorboard --logdir=log
#model.save(MODEL_NAME)
