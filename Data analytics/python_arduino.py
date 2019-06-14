from serial import *

try:
    arduino=serial.Serial("/dev/ttyACMO",timeout=1)
except:
    print('Check the port')

rawdata=[]
count=0

while count<3:
    rawdata.append(str(arduino.readline()))
    count+=1
print(rawdata)
