import comm
import csv


frdm = comm.FRDM('/dev/ttyUSB0')
print "comunicando FRDM"
frdm.write(M1=0,M2=0,steer=0,leds=0)
frdm.write(M1=0,M2=0,steer=0,leds=0)
print "comunicando Mouse"
mouse = comm.mouse('/dev/ttyUSB1')
print mouse.read()
print "comm ok"    
odom = []  
enc = 0
pxl = 0
for i in xrange(75):
	enc = frdm.write(M1=5,M2=5,steer=0,leds=0)#frdm.write(M1=0,M2=0,steer=0,leds=0)
	pxl = int(mouse.read())
	print (enc,pxl)
	odom.append([enc,pxl])
enc = frdm.write(M1=0,M2=0,steer=0,leds=0)    
#print enc
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(odom)
