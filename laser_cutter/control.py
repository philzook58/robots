import serial
import numpy as np
import math
import time
ser = serial.Serial('/dev/cu.usbmodem1411', 9600, timeout=1)

angleA = 0#np.pi/6
angleB = np.pi/6

a0 = 7
a180 = 180
b0 = 7
b180 = 180

def sendA(angle):
    newangle = int(180./ np.pi * 180. *angle/(a180-a0) + a0)
    print(newangle)
    ser.write(str(newangle)+'a')
def sendB(angle):
    newangle = int(180. / np.pi * angle * 180. / (b180-b0) + b0)
    print(newangle)
    ser.write(str(newangle)+'b')

def calcX(angleA,angleB):
    return np.cos(angleA)+np.cos(angleA + angleB)

def calcY(angleA,angleB):
    return np.sin(angleA)+np.sin(angleA + angleB)

def calcDTheta(dx,dy,angleA,angleB):
        J = np.array([[ np.sin(angleA)+ np.sin(angleA+angleB),  np.sin(angleA+angleB) ],
                      [  -np.cos(angleA) - np.cos(angleA+angleB),  - np.cos(angleA+angleB) ]])
        return np.linalg.solve(J, np.array([dx,dy]))

def printPosition():
    print("X: " + str(calcX(angleA,angleB)) + " Y: " + str(calcY(angleA,angleB)) )

stepNum = 100
dist = .5
#sendA(angleA)
#sendB(angleB)
print(angleA)
print(angleB)
time.sleep(5)
for i in range(25):
    temp = calcDTheta(dist/stepNum, 0, angleA, angleB)
    angleA = angleA + temp[0]
    angleB = angleB + temp[1]
    sendA(angleA)
    sendB(angleB)
    print(angleA)
    print(angleB)
    printPosition()
    time.sleep(.2)

#ser.write(str(angleA)+'a')
#ser.write(str(angleB)+'b')

ser.close()
