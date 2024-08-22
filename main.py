import os
print(os.get_terminal_size())
input("Press Enter to continue...")
import math
from MultiTerm import *
Display = Screen(tuple(os.get_terminal_size()), (0, 0))
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
    qx = int(qx//1)
    qy = int(qy//1)
    return qx, qy


def draw_line(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    steps_x = abs(dx)
    steps_y = abs(dy)
    if steps_x >= steps_y:
        step = steps_x
    else:
        step = steps_y

    x_increment = dx / step
    y_increment = dy / step

    x = x1
    y = y1

    for _ in range(step):
        Display[int(y)][int(x)] = "X"
        x += x_increment
        y += y_increment


points = [(10, 10), (20, 20)]
draw_line(*points)
Display.draw()
for i in range(180):
    Display.clear()
    points = [rotate(points[0], points[1], math.radians(i)), points[1]]
    draw_line(*points)
    Display.draw()
    time.sleep(0.1)
while True:
    pass
