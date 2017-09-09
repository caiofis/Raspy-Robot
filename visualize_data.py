import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

data = np.load('data.npy')

def show_Video():
	fig = plt.figure()
	# make axesimage object
	im = plt.imshow(data[0][0])
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
	     plt.imshow(data[0][j])
	plt.show()

print "How would you like to visualize?"
print "1 - A video animation"
print "2 - A brief chart"
a = raw_input()
if a == "1":
	show_Video()
if a == "2":
	show_Chart()
