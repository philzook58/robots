
from xml.dom import minidom

#Suggestion:python svgwrite.py mysvg >> outputfile
# append a bunch of images to file

import sys
if len(sys.argv) < 2:
    print "***** USAGE: python svgparse.py filename *****"

svg_file = sys.argv[1]

doc = minidom.parse(svg_file)  # parseString also exists
path_strings = [path.getAttribute('d') for path
                in doc.getElementsByTagName('path')]
doc.unlink()
#print path_strings

import re
posStrings = re.findall(r"[-+]?\d*\.\d+|\d+", path_strings[0])

x = []
y = []

for i in range(len(posStrings)):
    if i % 2 == 0:
        x.append(float(posStrings[i]))
    else:
        y.append(float(posStrings[i]))

x[0] = 0.0
y[0] = 0.0

for i in range(1,len(x)):
    x[i] = x[i]+x[i-1]
    y[i] = y[i]+y[i-1]

midx = (max(x)+min(x) )/ 2
midy = (max(y)+min(y) )/ 2


xlen = max(x)-min(x)
ylen = max(y)-min(y)
mylen = max(xlen,ylen)
norm = 200.0 / mylen
for i in range(len(x)):
    x[i] = (x[i] - midx) * norm
    y[i] = (y[i] - midy) * norm

xnew = []
ynew = []

subdivide = 5
N = subdivide
for i in range(len(x)-1):
    for j in range(N-1):
        xnew.append( (x[i+1]-x[i])*j/subdivide + x[i]  )
        ynew.append( (y[i+1]-y[i])*j/subdivide + y[i]  )
for j in range(N-1):
    xnew.append( (x[0]-x[-1])*j/subdivide + x[-1]  )
    ynew.append( (y[0]-y[-1])*j/subdivide + y[-1]  )
x = xnew
y = ynew

t=[]
import math
for i in range(len(x)-1):
    length2 = (x[i+1]-x[i])**2 +(y[i+1]-y[i])**2
    t.append(math.sqrt(length2))
length2 = (x[-1]-x[0])**2 +(y[-1]-y[0])**2
t.append(math.sqrt(length2))

'''
print "x"
print x
print "y"
print y
'''

# Insert math here. Normalization, centering, etc. precomputation of angles.

#print svg_file.split('.')[0]

f = open(svg_file.split('.')[0] + '.json', 'w')
import json
pos = {'x': x, 'y':y, 't':t}

json.dump(pos, f)

#print "float xpos[" + str(len(x)) + "] = {" + ", ".join(map(str,x)) + "};"
#print "float ypos[" + str(len(y)) + "] = {" + ", ".join(map(str,y)) + "};"
