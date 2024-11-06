from turtle import *
import random

c = ["#FF69B4", "#33CC33", "#66CCCC", "#FFCC00", "#CCCCFF", "#FF99CC", "#0099CC"]
bgcolor("black")
speed(0)

for i in range(360):
    r = random.random()
    if r < 0.5:
        pencolor(random.choice(c))
    else:
        pencolor("#FFFFFF")  # White
    pensize(1+i/100)
    forward(i)
    left(50.428)