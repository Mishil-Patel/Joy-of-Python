from turtle import *
speed(100)

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


# Now let us make a color box
color_box = ["red", "blue", "green", "yellow", "orange", "cyan","black","brown","teal","peru"]


#Now let us draw multiple stars below
for i in range(1,10):
    star(i*50,i*50,50,color_box[i])
hideturtle()
