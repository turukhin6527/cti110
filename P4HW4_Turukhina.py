# This program uses turtle graphics and nested loops to draw a snowflake.

import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# set pen size and color
t.pensize(10)           
t.pencolor("purple")

# Using nested loops, draw a snowflake
for i in range(6):
    # Turn the other direction
    for j in range(6):
        t.forward(130)
        # Hexagon, sides are 360 / 6 = 60 degrees
        t.left(60)
    t.left(60)

