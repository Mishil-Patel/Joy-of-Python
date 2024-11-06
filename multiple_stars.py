from turtle import *
speed(0)

# Let us define our function
def star(x,y,l,color):
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    fillcolor(color)

    for i in range(5):
        forward(l)
        right(180-180/5)
    end_fill()
# Defining of the function is done.

color_box = ["red", "blue", "green", "yellow", "orange", "cyan","black","brown","teal","peru","gold","violet","lavender","coral","darkgray","snow","mediumblue","chocolate","darkorange","palevioletred"]

#Now let us draw multiple stars below

for i in range(1,20):
    color=color_box[i]
    star(i*30-200,i*30-200,20,color)
    
hideturtle()
