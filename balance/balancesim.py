import numpy as np


#ok. Let's use a simple angle robot. We control the angle.


'''



	theta 2
    - - - - -
 l1/m    2
  /
 /theta 1


'''

l1 = 1.
l2 =  1.
m1 =1.
m2 =1.
m = 5.
g = 9.8
def moment(theta1, theta2):
	return m * l1 **2

def centerofmass(theta1, theta2):
	n1 = np.array([np.cos(theta1), np.sin(theta1)])
	n2 = np.array([np.cos(theta2+ theta1), np.sin(theta2 + theta1)])
	#return n1 * l1 / 2
	return (m1 * l1/2 * n1 + m2 * (l2/2 * n2 + l1*n1) +  m * l1* n1 ) / (m1+ m2 + m)

def torque(theta1, theta2):
	return g * np.dot(centerofmass(theta1, theta2), np.array([ 1. , 0]) ) #some horseshit
	print torque
def deriv(theta1,theta2,omega):
	theta1dot = omega
	omegadot = torque(theta1, theta2) / moment(theta1,theta2)
	return theta1dot, omegadot

theta1  = np.pi+0.01
theta2  = np.pi/2
omega=0.

def accel(omega):
	pass
def 

import pygame
import sys


pygame.init()

screen = pygame.display.set_mode((640,480))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
points = [(100,100), (150,200), (200,100)]

dt=0.01

def updatePoints(points):
	global theta1
	global omega
	theta1dot, omegadot= deriv(theta1,theta2,omega)
	theta1 = theta1 + theta1dot * dt
	omega = omega + omegadot*dt
	n1 = np.array([np.cos(theta1), np.sin(theta1)])
	n2 = np.array([np.cos(theta2+theta1), np.sin(theta2+ theta1)])
	origin = np.array([200,200])
	points = [origin, origin + n1* l1 * 100,origin + n1* l1 * 100 + n2 * l2 * 100]
	point = map(tuple, points)
 	return points
while (True):

   # check for quit events
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();

   # erase the screen
   screen.fill(white)

   # draw the updated picture

   points = updatePoints(points)  # changes the location of the points
   pygame.draw.lines(screen,black,False,points,1)  # redraw the points

   # update the screen
   pygame.display.update()







