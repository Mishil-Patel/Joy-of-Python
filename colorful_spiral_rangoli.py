from turtle import *

c = ['red','purple','blue','green','orange','yellow']
bgcolor('black')
speed(0)
for i in range(360*2):
    pencolor(c[i%6])
    pensize(1+i/100)
    forward(i/2)
    left(59)
hideturtle()
