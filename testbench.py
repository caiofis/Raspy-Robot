import cv2
import numpy as np
import comm
<<<<<<< HEAD
import time
=======
>>>>>>> sobel

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('Motor 1','image',10,20,nothing)
cv2.createTrackbar('Motor 2','image',10,20,nothing)
cv2.createTrackbar('Steer   ','image',10,20,nothing)
#inicialize the serial controler
<<<<<<< HEAD
controler = comm.FRDM('/dev/ttyACM0')
=======
#controler = comm.FRDM('/dev/ttyACM0')
>>>>>>> sobel
while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    m1 = cv2.getTrackbarPos('Motor 1','image')-10
    m2 = cv2.getTrackbarPos('Motor 2','image')-10
    servo = cv2.getTrackbarPos('Steer   ','image')-10
    print (m1,m2,servo)
<<<<<<< HEAD
    controler.write(m1,m2,servo,0)
    time.sleep(0.02)
=======
    #controler.write(0,0,(r-10),0)
>>>>>>> sobel
cv2.destroyAllWindows()
