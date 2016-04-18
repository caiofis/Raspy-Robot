import serial
import time

class FRDM(object):
    """docstring for FRDM"""
    def __init__(self,port):
        self.ser = serial.Serial(port,baudrate=115200)
        self.sb = "S"
        self.eb = "E"
        self.commands = [self.sb,'0','0','0','4']
        #self.ser.flush()

    def write(self,M1,M2,steer,leds):
        self.commands[1] =  str((M1+10)).zfill(2)
        self.commands[2] =  str((M2+10)).zfill(2)
        self.commands[3] =  str((steer+10)).zfill(2)
        self.commands[4] =  str(leds)
        self.ser.write(self.commands[0])
        soma = 0
        for i in range(1,5,1):
            self.ser.write(self.commands[i])
            soma += int(self.commands[i])
        self.ser.write(str(soma).zfill(2))

# frdm = FRDM('/dev/ttyACM0')
# #frdm.write(M1=0,M2=0,steer=0,leds=4)
# while True:
#     for i in range(-5,5,1):
#         frdm.write(M1=0,M2=0,steer=i,leds=0)
#         frdm.write(M1=0,M2=0,steer=i,leds=0)
#         frdm.write(M1=0,M2=0,steer=i,leds=0)
#         frdm.write(M1=0,M2=0,steer=i,leds=0)
#         time.sleep(0.5)
#         print i
#     for i in range(5,-5,-1):
#         frdm.write(M1=0,M2=0,steer=i,leds=4)
#         frdm.write(M1=0,M2=0,steer=i,leds=4)
#         frdm.write(M1=0,M2=0,steer=i,leds=4)
#         frdm.write(M1=0,M2=0,steer=i,leds=4)
#         time.sleep(0.5)
#         print i
