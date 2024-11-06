from turtle import*
speed(0)    

for i in range(100):
    if i<50:
        circle(i,180)
    else:
        forward(i)
        left(90)
        forward(2*i)
        left(90)
        forward(2*i)
        left(90)
        forward(2*i)
        left(90)
        forward(i)
        
