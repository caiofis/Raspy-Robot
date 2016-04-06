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
        self.commands[1] =  str((M1+10)).zfill(2)
        self.commands[2] =  str((M2+10)).zfill(2)
        self.commands[3] =  str((steer+10)).zfill(2)
        self.commands[4] =  str(leds)
        for i in self.commands:
            self.ser.write(i)
