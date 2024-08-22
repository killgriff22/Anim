import os
print(os.get_terminal_size())
input("Press Enter to continue...")
from MultiTerm import *
import math
Display = Screen(tuple(os.get_terminal_size()),(0,0))
Display.clear()

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def draw_line(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    steps_x = abs(dx)
    steps_y = abs(dy)
    func = lambda x,b:(steps_y/steps_x if steps_y>steps_x else steps_x/steps_y)*x+b
    for x in range(steps_x):
        y = func(x,y1)
        Display.content[int(y)][int(x)] = "X"
points = [(0,0),(0,10),(10,10),(10,0),(0,0)]
for i in range(len(points)):
    p1 = points[i]
    p2 = points[(i+1)%len(points)]
    draw_line(p1,p2)
    Display.draw()
    time.sleep(.5)
while True:
    pass