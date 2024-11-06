from turtle import *
import random

# Generate a random integer from 0 to 9
speed(0)
for i in range(1000):
    r = random.randint(-800, 800)
    k = random.randint(-400,400)
    goto(r,k)
print("Over")
