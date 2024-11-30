import pygame as pg
import random as r
import math as m

pg.init()
gray = (128,128,128)
white = (255,255,255)
res = (1366,768)
screen = pg.display.set_mode(res)
clock = pg.time.Clock()
startpoint = (res[0]/2,res[1]/2)
ll = []
wl = []
writelimit = False
for i in range(10): # length,turnspeed
    length = r.randint(0,70)
    turnspeed = (length/4)/500
    ll.append( ( length,0,turnspeed) )
##ll.extend( [(50,1,5/500),
##            (25,1,50/500),
##            (40,1,10/500)]
##           )

def loop(startpoint,c):
    if c == len(ll) :
        if startpoint not in wl:
            wl.append(startpoint)
    else:
        cl = ll[c]
        endpoint = (cl[0] * m.sin(cl[1]) + startpoint[0],cl[0] * m.cos(cl[1]) + startpoint[1])
        pg.draw.line(screen,white,startpoint,endpoint)
        loop(endpoint,c+ 1)
c = 0
for n in ll:
    print(n)
    
while True:
    screen.fill(0)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                print("EXIT")
                pg.quit()
            if event.key == pg.K_SPACE:
                if writelimit == False:
                    writelimit = True
                else:
                    writelimit = False


            
    loop(startpoint,0)
    for j in ll:
        ccl = ll.index(j)
        ll[ccl] = ( j[0] , j[1] + j[2],j[2])
        wlen = len(wl)
        if len(wl) > 2:
            pg.draw.lines(screen,gray,0,wl)
            
        if writelimit == True:               
            if wlen > 500:
                wl.pop(0)
    
    pg.display.flip()
    clock.tick(600)
