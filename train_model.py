import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import tflearn
import my_models

import time

# Setup the model
WIDTH = 50
HEIGHT = 50
LR = 1e-4
EPOCHS = 50
MODEL_NAME = 'raspy-car-{}-{}-{}-epochs.model'.format(LR, 'simpConv2',EPOCHS)
model = my_models.simpConv2(WIDTH, HEIGHT, LR)

# Load training data
train_data = np.load('data/training_data.npy')


train = train_data[:-300]
test = train_data[-300:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

# Train model
start = time.time()
model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}),
    snapshot_step=1000, show_metric=True, run_id=MODEL_NAME)
end = time.time()
print (end-start)
# tensorboard --logdir=log
model.save(MODEL_NAME)
