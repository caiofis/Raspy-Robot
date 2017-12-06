import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cv2


class dataHandler(object):
    def __init__(self, file):
        self.data = np.load(file,encoding='bytes')

    def save(self, file = 'training_data.npy'):
        """Save data as numpy file"""
        np.save(file, self.data)

    def merge(self, file = "training_data.npy"):
        """ Merge a datafile to the data set.
              Use before reshape   """
        new_data = np.load(file,encoding='bytes')
        self.data = np.concatenate((self.data,new_data),axis=1)


    def discreteBalance(self):
        """This code reduct the bias in the data set"""
        lefts = []
        rights = []
        forwards = []
        # discretise and reshape
        for i in xrange(len(self.data[0])):
            if self.data[1][i] > 2:
                rights.append([self.data[0][i],[1,0,0]])
            elif self.data[1][i] < -2:
                lefts.append([self.data[0][i],[0,0,1]])
            else:
                forwards.append([self.data[0][i],[0,1,0]])
        #print len(lefts) , len(rights), len(forwards)
        forwards = forwards[:len(lefts)][:len(rights)]
        lefts = lefts[:len(forwards)]
        rights = rights[:len(forwards)]
        final_data = forwards + lefts + rights
        #print len(final_data)

        self.data = final_data

    def reductZeros(self):
        """ take of some examples lableled as zero"""
        max_zeros = (1.0/19) * len(self.data[0])
        print max_zeros
        imgs = []
        labels=[]
        j = 0
        for i in xrange(len(self.data[0])):
            if self.data[1][i] != 0:
                imgs.append(self.data[0][i])
                labels.append(self.data[1][i])
            elif j < max_zeros:
                imgs.append(self.data[0][i])
                labels.append(self.data[1][i])
                j += 1
        self.data = [imgs,labels]

    def singleLine(self,height=10):
        imgs = []
        labels=[]
        for i in xrange(len(self.data[0])):
            imgs.append(self.data[0][i][height,:])
            labels.append(self.data[1][i])
        self.data = [imgs,labels]

    def twoLines(self,height1=3,height2=20):
        imgs = []
        labels=[]
        for i in xrange(len(self.data[0])):
            img = np.concatenate((self.data[0][i][height1,:], self.data[0][i][height2,:]), axis=0)
            imgs.append(img)
            labels.append(self.data[1][i])
        self.data = [imgs,labels]

    def reshape(self):
       samples = []
       for i in xrange(len(self.data[0])):
            samples.append([self.data[0][i],self.data[1][i]])
       self.data = samples

    def shuffle(self):
        """ Only use in reshaped data!"""
        temp = self.data
        np.random.shuffle(temp)
        self.data = temp

    def reflect(self):
        """ Double the dataset by reflecting it"""
        imgs = []
        labels=[]
        for i in xrange(len(self.data[0])):
            imgs.append(self.data[0][i])
            labels.append(self.data[1][i])
            if self.data[1][i] != 0:
                imgs.append(cv2.flip(self.data[0][i],1))
                labels.append(self.data[1][i]*-1)
        self.data = [imgs,labels]

    def one_hot(self):
        labels = []
        for i in xrange(len(self.data[0])):
            code = np.zeros([19])
            code[self.data[1][i]+9] = 1
            labels.append(code)
        self.data[1] = labels
