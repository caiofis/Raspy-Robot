import time
import comm

frdm = comm.FRDM('/dev/ttyACM0')
frdm.write(M1=0,M2=0,steer=0,leds=0)
time.sleep(1)
dist = 0
steps=0
while steps< 100:
    enc = frdm.write(M1=4,M2=4,steer=0,leds=4)
    print enc
    dist = dist+enc
    steps = steps + 1
enc = frdm.write(M1=0,M2=0,steer=0,leds=0)
dist = dist+enc
print enc
time.sleep(0.05)
enc = frdm.write(M1=0,M2=0,steer=0,leds=0)
print enc
dist = dist+enc
print dist
print (dist*((3.14*5)/40))
