from turtle import *
colormode(255)
pensize(5)
speed(0)

for i in range(200):
    x=255-i
    y=i
    pencolor(x,y,int(y/2))
    forward(3)
