import pygame as pg
import random
pg.init()
SCRN = (1366,768)
mpos = (SCRN[0],SCRN[1])
boidcount = 50
size = 9
screen = pg.display.set_mode(SCRN)
clock = pg.time.Clock()
boidimage = pg.image.load("myboidpng")
boidimage = pg.transform.scale(boidimage,(1 * size,2 * size))

class Being:
    global SCRN
    def __init__(self,pos,vect,mass):
        self.pos = pos
        self.vect = vect
        self.mass = mass

    def ang_x_axis(self):
        ang = self.vect.angle_to((100,0))
        return ang

def eventhandler():
    global running, paused,mpos
    for event in pg.event.get():
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print("Exiting")
                running = False
            if event.key == pg.K_SPACE:
                mpos = (-1000,-1000)

        if event.type == pg.MOUSEMOTION:
            mpos = event.pos
            
            
            

        
def createboids(n):
    for i in range(n):
        bpos = (random.randrange(0,SCRN[0]+1),
        random.randrange(0,SCRN[1]+1)) 
        
        bvect = pg.math.Vector2( random.randrange(-6,5) + random.randrange(0,100)/100,
        random.randrange(-6,5) + random.randrange(0,100)/100)
        bmass = 3
        beinglist.append(Being(bpos,bvect,bmass))

def updatebeings():
    global SCRN

    for being in beinglist:
        xpos = being.pos[0]
        ypos = being.pos[1]
        

        beingindex = beinglist.index(being)
        ol = beinglist[:beingindex] + beinglist[beingindex+1:] #other boids
        cl = [] #close boids
        for j in ol:
            dist = int((j.pos[0] - being.pos[0])**2 + (j.pos[1] - being.pos[1])**2)
            if dist < 5000:
                cl.append(j)

        if len(cl) != 0: #other boid alignment
            anglesum = 0
            for j in cl:
                anglesum += j.ang_x_axis()
            avgangle = (anglesum/len(cl))
            angledifference = ( being.ang_x_axis() - avgangle)
   
            threshold = 90


            if angledifference <= threshold and angledifference >= -(threshold):
                #turnbyangle = pg.math.lerp(1,20,lerpval)
                being.vect.rotate_ip(angledifference/2)
                #print(f"rotated by {angledifference}")


            
            for j in cl: #separation & cohesion
                

                dist = int((j.pos[0] - being.pos[0])**2 + (j.pos[1] - being.pos[1])**2)
                if dist < 500:
                    
                    oppvect = pg.math.Vector2( -(j.pos[0] - being.pos[0]), -(j.pos[1] - being.pos[1]))
                    oppangle = int(oppvect.angle_to((0,1)))
                    angledifference = int(being.ang_x_axis() - oppangle)
                    being.vect.rotate_ip(angledifference/10)

               



        
        mdistance = (being.pos[0] - mpos[0])**2 + (being.pos[1] - mpos[1])**2
        if mdistance < 4000:

            oppvect = pg.math.Vector2( (mpos[0] - being.pos[0]), (j.pos[1] - mpos[1]))
            oppangle = oppvect.angle_to((0,1))
            angledifference = int(being.ang_x_axis() - oppangle)

            being.vect.rotate_ip(angledifference/10)

                  
        

        if xpos > SCRN[0]: #border teleportation
            being.pos = (0,being.pos[1])
        elif xpos < 0:
            being.pos = (SCRN[0],being.pos[1])
        if ypos > SCRN[1]:
            being.pos = (being.pos[0],0)
        elif ypos < 0:
            being.pos = (being.pos[0],SCRN[1])


        being.pos = (being.pos[0] + being.vect.x,
        being.pos[1] + being.vect.y)

        

def drawbeings():
    global screen, SCRN, boidimage
    for being in beinglist:
        thisboidimage = pg.transform.rotate(boidimage,-90 +  being.ang_x_axis())
        brect = thisboidimage.get_rect()
        brect.center = being.pos
        #pg.draw.circle(screen,(255,0,255),being.pos,being.mass)
        
        screen.blit(thisboidimage,brect)



beinglist = []
createboids(boidcount)
running = True
paused = False
while True:
    
    screen.fill((0,0,0))
    eventhandler()
    if running == False:
        pg.quit()
        break
    if paused == False:
        updatebeings()
        
    drawbeings()
    pg.display.flip()
    clock.tick(60)

