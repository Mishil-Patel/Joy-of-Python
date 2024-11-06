from turtle import *

speed(100)

def star(x, y, l, color):
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor(color)

    for _ in range(5):
        forward(l)
        right(144)
    end_fill()

colors = ["red", "blue", "green", "yellow", "orange"]

for i in range(-10, 10):
    color = colors[i % len(colors)]
    star(i * 30, i * 30, 20, color)

done()
