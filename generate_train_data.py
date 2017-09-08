# to transfer the datafile over the internet
# scp pi@192.168.1.100:/home/pi/code/data.npy /home/caio/Desktop/

import cv2
import numpy as np
import time
data = []
print "Colecting data"
for i in xrange(100):
        img=cv2.imread("/var/www/html/cam.jpg")
        data.append(img)
        time.sleep(0.05)
print "Saving"
data_array = np.array(data)
np.save('data',data_array)

