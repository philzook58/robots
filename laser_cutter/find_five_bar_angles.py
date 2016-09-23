from scipy import optimize
import numpy as np

#totally illogical naming scheme. Sweet.
a = 1
b = 1
c = 1
d = 1
e = 1
f = 1


def func(theta, x):
    return [(x[0]+ c * np.cos(theta[0]))**2 + (x[1] - c * np.sin(theta[0]))**2 - e**2 ,
     ( x[0]- b + d * np.cos(theta[1]))**2 + (x[1] - d * np.sin(theta[1]))**2 - f**2]

originAngle = [np.pi/2,np.pi/2]

def findAngles(x):
    sol = optimize.root(lambda theta: func(theta,x), originAngle)
    return sol


sol = optimize.root(lambda x: func(originAngle,x), [0,0])
origin = sol.x
print origin
print findAngles([0,0]+origin)
