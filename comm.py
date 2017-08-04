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

    def writeByte(self, value,delay=0):
        self.ser.write(value)
        time.sleep(delay)
    def write(self,M1,M2,steer,leds):
        self.commands[1] =  str((M1+10)).zfill(2)
        self.commands[2] =  str((M2+10)).zfill(2)
        self.commands[3] =  str((steer+10)).zfill(2)
        self.commands[4] =  str(leds)
        steps = "EB";
        while steps == "EB":
            self.writeByte(self.commands[0],delay=0.03)
            soma = 0
            self.writeByte(self.commands[1])
            self.writeByte(self.commands[2])
            self.writeByte(self.commands[3])
            self.writeByte(self.commands[4])
            for i in range(1,5,1):
                #self.writeByte(self.commands[i])
                soma += int(self.commands[i])
            self.writeByte(str(soma).zfill(2))
            steps = self.ser.read(2)
        steps = int(steps)
        return (steps)

class mouse(object):
	"""docstring for FRDM"""
	def __init__(self,port):
		self.ser = serial.Serial(port,baudrate=9600,timeout=0.05)
		time.sleep(5)
		self.ser.flush()
	def writeByte(self, value,delay=0):
		self.ser.write(value)
		time.sleep(delay)
	def read(self):
		self.writeByte("r")
		steps = int(self.ser.read(6))
		return steps-200000
	
#frdm = FRDM('/dev/ttyACM0')
#while True:
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
