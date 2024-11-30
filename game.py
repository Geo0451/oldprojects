import pygame as pg
import random as rd
pg.init()

def eventhandler():
    global running,boidcount
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print("EXITING")
                running = False
            if event.key == pg.K_r:
                print("RESET")
                boidlist.clear()
                createboids(boidcount)
            if event.key == pg.K_UP:
                createboids(1)
            if event.key == pg.K_DOWN:
                boidlist.pop()
            if event.key == pg.K_SPACE:
                boidlist.clear()
          

def createboids(n):
    for i in range(n):
        boidlist.append(Boid(dimensions))
def drawboid(boid):
    global image
    #pg.draw.circle(screen,boid.color,boid.pos,boid.size)
    screen.blit(image,boid.pos)
def updateboid(boid):
    global dimensions,speedlimit
    

    #border clipping
    #negative x
    if boid.pos[0] < 0:
        boid.pos = ( dimensions[0], boid.pos[1] )
        
    #positive x
    if boid.pos[0] > dimensions[0]:
        boid.pos = ( 0, boid.pos[1] )
      
    #negative y(up, in our case, as pygame uses inverse y axis)
    if boid.pos[1] < 0:
        boid.pos = ( boid.pos[0], dimensions[1] )
    #positive y(down)
    if boid.pos[1] > dimensions[1]:
        boid.pos = ( boid.pos[0], 0 )


    
    #avoidance(boid)  
    boid.pos = (
        boid.pos[0] + boid.vect.x,
        boid.pos[1] + boid.vect.y)

def avoidance(boid):
    global avoidance_val,speedlimit
    #IMPLEMET RAYCAST BASED AVOIDANCE HERE
            
    
    
class Boid:
    def __init__(self,dimensions):
        self.pos = ( rd.randrange(0,dimensions[0] + 1), rd.randrange(0,dimensions[1] + 1))
        self.vect = pg.Vector2(rd.randrange(-speedlimit,speedlimit+1),rd.randrange(-speedlimit,speedlimit+1))
        self.color = (255,255,255)

    
dimensions = (720,640)
speedlimit = 5
boidcount = 500
size = 10
image = pg.image.load("boid.png")
image = pg.transform.scale(image,(size,size))

clock = pg.time.Clock()
screen = pg.display.set_mode(dimensions)

avoidance_val = 50
cohesion_val = 0
alighment_val = 0

boidlist = []
running = True
while True:
    screen.fill(0)
    eventhandler()
    if running == False:
        break
    
    for i in boidlist:
        
        updateboid(i)
          
        drawboid(i)
        
    pg.display.flip()
    clock.tick(60)
pg.quit()
