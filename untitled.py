from turtle import *
from time import sleep

speed_increment = 2
turn_increment = 5
speed_limit = 10
border_size = 275

turn_sensitivity = 4
turn_count = 4
turn_count_limit = 5

border = 250
class ball():

    def __init__(self):
        self.vel = 0
        self.dir = 0
        self.pos = (0,0) #initial position

def status():
    print(f"\nVELOCITY = {big.vel}\nANGLE = {big.dir}\nPOSITION = {big.pos}\n,")
    print(f"turncount = {turn_count}")

def draw_border():
    global border
    penup()
    goto(border,border)
    pendown()
    goto(border,-border)
    goto(-border,-border)
    goto(-border,border)
    goto(border,border)
    penup()
    home()
    seth(0)


def accelerate():
    global big,speed_increment
    if big.vel < speed_limit:
        big.vel = (big.vel + speed_increment)
def reverse():
    global big,speed_increment
    if big.vel > -(speed_limit):
        big.vel = (big.vel - speed_increment)
def steer_left():
    global big,turn_sensitivity, turn_count
    big.dir = (big.dir + (turn_sensitivity * turn_count)) % 360  #positive change = leftward(anti clockwise) and vice versa
    turn_count += 2
def steer_right():
    global big,turn_sensitivity, turn_count
    big.dir = (big.dir - (turn_sensitivity * turn_count)) % 360
    turn_count += 2

def correct_border_collision():
    global big,border
    #if current position is greater than the border, set position to border
    #additionally "reflect" it by 180'ing the direction
    
    # check +/- x axes
    if big.pos[0] > border:
        big.pos = ( border , big.pos[1] ) #only changes the x value
        #we know that for angle between 0 and 90, the reflectant angle will be obtuse 
        big.dir = 180 - big.dir
        
    if big.pos[0] < -(border):
        big.pos = ( -(border) , big.pos[1] )
        big.dir = 180 - big.dir

    # check +/- y axes
    if big.pos[1] > border:
        big.pos = ( big.pos[0] , border ) #only changes the y value
        big.dir = 360 - big.dir
        
    if big.pos[1] < -(border):
        big.pos = ( big.pos[0] , -(border) )
        big.dir = 360 - big.dir


big = ball()
tracer(0,0)
#hideturtle()
bgcolor("black")
pencolor("white")
onkeypress(accelerate,"Up")
onkeypress(reverse,"Down")
onkeypress(steer_left,"Left")
onkeypress(steer_right,"Right")
onkeypress(status,"r")
listen()
while True:
    draw_border()
    #penup()
    setpos(big.pos)
    seth(big.dir)
    fd(big.vel)
    big.pos = pos()
    correct_border_collision()
    if turn_count > turn_count_limit:
        turn_count = turn_count_limit
        
    if turn_count > 1:
        turn_count -= 0.5
    update()
    #sleep(1/120)
        
        
