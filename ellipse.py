from turtle import *
from math import *

def ellipse(a,b):
    penup()
    x0 = a
    y0 = 0
    goto(x0,y0)
    pendown()

    for i in range(361):
        x = a*cos(radians(i))
        y = b*sin(radians(i))
        goto(x,y)


ellipse(50,100)
ellipse(80,130)
