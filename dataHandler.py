import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2
from random import shuffle

class dataHandler(object):
    def __init__(self, file):
        self.data = np.load(file,encoding='bytes')

    def save(self, file = 'training_data.npy')
        np.save(file, final_data)

    def balance(self):
        """This code reduct the bias in the data set"""
        lefts = []
        rights = []
        forwards = []
        # discretise and reshape
        for i in xrange(len(data[0])):
            if data[1][i] > 2:
                rights.append([data[0][i],[1,0,0]])
            elif data[1][i] < -2:
                lefts.append([data[0][i],[0,0,1]])
            else:
                forwards.append([data[0][i],[0,1,0]])
        #print len(lefts) , len(rights), len(forwards)
        forwards = forwards[:len(lefts)][:len(rights)]
        lefts = lefts[:len(forwards)]
        rights = rights[:len(forwards)]
        final_data = forwards + lefts + rights
        #print len(final_data)

        self.data = shuffle(final_data)

        def reshape(self):
            samples = []
            for i in xrange(len(data[0])):
                samples.append([data[0][i],[1,0,0]])
            self.data = samples

        def shuffle(self,save):
            """ Only use in reshaped data!"""
            self.data = shuffle(sefl.data)

        def compress(self):
            """This code reduct the dataset images by resizing then"""
            images = []
            for im in data[0]:
                compressed = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                compressed = cv2.resize(compressed,(50,50))
                images.append(compressed)
            self.data[0] = images
