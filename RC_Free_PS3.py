import pygame,os
from time import sleep
import comm

#control the freescale cup car using the serial module


def main():
    frdm = comm.FRDM('/dev/ttyUSB0')
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
    while True:
        pygame.event.pump()
        steer = int(round(joystick.get_axis(0)*9))
        #speed = int(round(joystick.get_axis(13)*8))#-int(round(joystick.get_axis(12)*5))
	speed = 0
	print steer
        enc = frdm.write(M1=speed,M2=speed,steer=steer,leds=0)
        #print enc
    enc = frdm.write(M1=0,M2=0,steer=0,leds=0)    

if __name__ == "__main__":
    main()
