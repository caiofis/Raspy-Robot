import serial


class FRDM(object):
    """docstring for FRDM"""
    def __init__(self,port):
        self.ser = serial.Serial(port,baudrate=115200)
        self.sb = "S"
        self.eb = "E"
        self.commands = [self.sb,'0','0','0','4']
        self.ser.flush()

    def write(self,M1,M2,steer,leds):
        self.commands[1] =  str(chr(M1+10))
        self.commands[2] =  str(chr(M2+10))
        self.commands[3] =  str(chr(steer+10))
        self.commands[4] =  str(leds)
        for i in self.commands:
            self.ser.write(i)

frdm = FRDM('/dev/ttyACM0')
while(True):
    frdm.write(M1=3,M2=5,steer=-5,leds=0)
