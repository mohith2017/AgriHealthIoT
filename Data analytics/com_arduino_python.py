# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 13:25:46 2017

@author: glassbox
"""


"""Module importation"""
import serial
import time

while True:
    """Opening of the serial port"""
    try:
        arduino = serial.Serial("COM4",timeout=1)
    except:
        print('Please check the port')

    """Initialising variables"""
    rawdata=[]
    count=0

    """Receiving data and storing it in a list"""
    while count<3:
        rawdata.append(str(arduino.readline()))
        count+=1
        print(rawdata)

    def clean(L):
        newl=[]#initialising the new list
        for i in range(len(L)):
            temp=L[i][2:]
            newl.append(temp[:-5])
        return newl

    cleandata=clean(rawdata)

    def write(L):
        file=open("E:/Softwares/tomcat for j2ee/tomcat 7.0.47/webapps/ROOT/hi2.html",mode='w')
        for i in range(len(L)):
            file.write(L[i]+'\n')
        file.close()

    write(cleandata)
    time.sleep(0.25)
