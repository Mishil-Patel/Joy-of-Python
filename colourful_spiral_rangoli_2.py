from turtle import *
c = ["red","orange","yellow","green","blue","indigo","violet"]
bgcolor("black")
speed(0)
for i in range(360):
    pencolor(c[i%7])
    pensize(1+i/100)
    forward(i)
    left(50.428)
