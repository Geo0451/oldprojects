import math
import turtle
from time import sleep
 
win = turtle.Screen()
win.bgcolor("white")
 
# coordinate setting
win.setworldcoordinates(0, -2, 3600, 2)
t = turtle.Turtle()
turtle.tracer(0,0)
 
# Draw a vertical line
t.goto(0, 2)
t.goto(0, -2)
t.goto(0, 0)
 
# Draw a Horizontal line
t.goto(3600, 0)
t.penup()
t.goto(0, 0)
t.pendown()
t.pencolor("blue")
t.pensize(4)
 
# Generate wave form
a = 0
while True:
    t.reset()
    turtle.hideturtle()
    for x in range(3600):
        y = math.sin(math.radians(x) + a)
        t.goto(x, y)
    turtle.update()
    a  += 2
    #sleep(1/60)
