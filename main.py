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
    func = lambda x,b:(steps_y/steps_x)*x+b 
    if steps_x == 0:
        func = lambda x,b:b+1 if dy > 0 else b-1
    for x in range(steps_x):
        y = func(x,y1)
        Display.content[int(y)][int(x+x1)] = "X"
points = [(10,10),(20,20)]
draw_line(*points)
Display.show()
for i in range(180):
    Display.clear()
    points =[rotate(points[0],points[1],math.radians(i))]
    draw_line(*points)
    Display.show()
    time.sleep(0.1)
while True:
    pass