import serial
import numpy as np
import math
import time
from scipy import optimize


#totally illogical naming scheme. Sweet.
a = 1
b = 9.625
c = 6.5
d = 6.5
e = 6.625
f = 6.625

device = '/dev/cu.usbmodem1411'


def func(theta, x):
    return [(x[0]+ c * np.cos(theta[0]))**2 + (x[1] - c * np.sin(theta[0]))**2 - e**2 ,
     ( x[0]- b + d * np.cos(theta[1]))**2 + (x[1] - d * np.sin(theta[1]))**2 - f**2]

originAngle = [np.pi/2,np.pi/2]



def findPos(theta):
    sol = optimize.root(lambda x: func(originAngle,x), [0,0])
    return sol.x



sol = optimize.root(lambda x: func(originAngle,x), [0,0])
origin = sol.x

def findAngles(x):
    sol = optimize.root(lambda theta: func(theta,x + origin), originAngle)
    return sol.x





ser = serial.Serial(device, 9600, timeout=1)

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

def goto(x):
    angles = findAngles(x)
    sendA(angles[0])
    sendB(angles[1])

def calcX(angleA,angleB):
    return np.cos(angleA)+np.cos(angleA + angleB)

def calcY(angleA,angleB):
    return np.sin(angleA)+np.sin(angleA + angleB)

def printPosition():
    print("X: " + str(calcX(angleA,angleB)) + " Y: " + str(calcY(angleA,angleB)) )

stepNum = 100
dist = 4.
#sendA(angleA)
#sendB(angleB)
print(angleA)
print(angleB)
time.sleep(5)
x = [-2,-2]
goto(x)
for i in range(25):
    x[0] = x[0]+ dist/stepNum
    goto(x)
    time.sleep(.2)

#ser.write(str(angleA)+'a')
#ser.write(str(angleB)+'b')

ser.close()
