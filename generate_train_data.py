# to transfer the datafile over the internet
# scp pi@192.168.1.100:/home/pi/code/data.npy /home/caio/Desktop/

import cv2
import numpy as np
import pygame,os
import comm
#control the freescale cup car using the serial module
# and the PS3 control, collecting camera and control data
frdm = comm.FRDM('/dev/ttyACM0')
print "comunicando"
frdm.write(M1=0,M2=0,steer=0,leds=0)
print "comm ok"      
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('The amazing remote control')
joystick = pygame.joystick.Joystick(0)
joystick.init()
#ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1);
enc = 0
print("Wait for the first command") # Triangle button is the start 
while not joystick.get_button(12):
	pygame.event.pump()

data = []
print "Colecting data"
while joystick.get_button(12): # Release the button to finish
	pygame.event.pump() #Joystick reads from -1 to 1 
	steer = int(round(joystick.get_axis(0)*9))
	speed = int(round((joystick.get_axis(13)+1)*0.5*8))
	speed -= int(round((joystick.get_axis(12)+1)*0.5*5))
	#speed = int(round((joystick.get_axis(13)+joystick.get_axis(12)+2)*0.5*$
	#speed = 0
	#print steer
	#print speed
	enc = frdm.write(M1=speed,M2=speed,steer=steer,leds=4)
	#print enc
	img=cv2.imread("/var/www/html/cam.jpg")
	data.append(img)
	#time.sleep(0.05)
print "Would you like to save "+len(data)+" pictures?[y/n]"
a= raw_input()
if a == "y"
	print "Saving"
	data_array = np.array(data)
	np.save('data',data_array)
else:
	print "Don't saved"

