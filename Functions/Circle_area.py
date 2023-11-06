# python program to calculate the circle of a python.

import math


def circle_area(radius):
    area = math.pi * radius * radius
    return area


radius = float(input('Enter the radius of the circle: '))

ans = circle_area(radius)

print('Araea of the circle is ', ans)
