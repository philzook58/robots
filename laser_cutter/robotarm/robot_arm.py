

#9,10,11

from scipy import optimize
import numpy as np
import serial

device = '/dev/cu.usbmodem1411'
L = 1.


def pos(theta, x):
    rho = L* (np.sin(theta[0]) + np.sin(theta[0] + theta[1]))
    z = L * (np.cos(theta[0]) + np.cos(theta[0] + theta[1]))
    return np.array([rho - x[0], z - x[1]])

def objective(theta,x):
    temp = pos(theta,x)
    return temp[0]**2+temp[1]**2




anglerange = (-np.pi/2,np.pi/2)
bnds = (anglerange,anglerange)

#cons = [{'type':'ineq', 'fun': con},
#        {'type':'eq', 'fun': con_real}]

def cleanAngle(angle):
    angle = (angle + np.pi) % (2 * np.pi) - np.pi
    return angle


def findAngles(x,y,z):

    rho = np.sqrt(x**2 + y**2)
    theta0 = np.arctan2(y,x)
    sol = optimize.root(lambda theta: pos(theta, [rho,z] ), [0,np.pi/2])
    #sol = optimize.minimize(lambda theta: objective(theta, [rho,z]), np.array([0,0]), method='SLSQP', bounds=bnds)
    print sol.success
    theta = sol.x
    theta = cleanAngle(theta)
    return [theta0, theta[0], theta[1]]


ser = serial.Serial(device, 19200, timeout=1)

import signal
import sys
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        ser.close()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

import time
'''
while True:
    x = float(input('x: '))
    y = float(input('y: '))
    z = float(input('z: '))
    theta = findAngles(x,y,z)
    print(theta)
    ser.write(str(theta[0])+ ',')
    ser.write(str(theta[1])+ ',')
    ser.write(str(theta[2])+ ';\r\n')
    '''
while True:
    theta = np.random.rand(3) * np.pi - np.pi/2
    ser.write(str(theta[0])+ ',')
    ser.write(str(theta[1])+ ',')
    ser.write(str(theta[2])+ ';\r\n')
    time.sleep(1)



ser.close()
