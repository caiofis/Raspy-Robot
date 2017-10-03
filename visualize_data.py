import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#data = np.load('data.npy',encoding='bytes')
data = np.load('data_left.npy',encoding='bytes')
def show_Video():
	fig = plt.figure()
	# make axesimage object
	im = plt.imshow(data[0][0],cmap='gray')
	# function to update figure
	def updatefig(j):
	    # set the data in the axesimage object
	    im.set_array(data[0][j])
	    # return the artists set
	    return [im]
	# kick off the animation
	ani = animation.FuncAnimation(fig, updatefig, frames=range(len(data[0])), 
                              interval=30, blit=True)
	plt.show()

def show_Chart():
	fig = plt.figure()
	for i in xrange(6):
	     j=np.random.randint(0,len(data[0]))
	     ax = fig.add_subplot(2,3,i+1)
	     ax.title.set_text(str(data[1][j]))
	     plt.imshow(data[0][j],cmap='gray')
	plt.show()

def show_Histogram():
	fig = plt.figure()
	plt.hist(data[1])
	plt.show()

while True:
	print "How would you like to visualize?"
	print "1 - A video animation"
	print "2 - A brief chart"
	print "3 - A histogram of the labels"
	print "4 - Exit"
	a = raw_input()
	if a == "1":
		show_Video()
	if a == "2":
		show_Chart()
	if a == "3":
		show_Histogram()
	if a == "4":
		break
