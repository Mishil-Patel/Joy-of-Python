from turtle import*
speed(20)

#lower two boxes of house from here
goto(300,0)
goto(300,150)
goto(0,150)
home()
goto(200,0)
goto(200,150)

#now triangle in top right
left(60)
forward(100)
right(120)
forward(100)

#now box in top left
goto(0,150)
left(120)
forward(100)
right(60)
forward(200)

#now window
penup()
goto(75,50)
pendown()
goto(125,50)
goto(125,100)
goto(75,100)
goto(75,50)

#now door
penup()
goto(235,0)
pendown()
goto(235,70)
goto(265,70)
goto(265,0)

hideturtle()
