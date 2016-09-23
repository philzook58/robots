
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

'''
print "x"
print x
print "y"
print y
'''

# Insert math here. Normalization, centering, etc. precomputation of angles.

#print svg_file.split('.')[0]

print "float xpos[" + str(len(x)) + "] = {" + ", ".join(map(str,x)) + "};"
print "float ypos[" + str(len(y)) + "] = {" + ", ".join(map(str,y)) + "};"
