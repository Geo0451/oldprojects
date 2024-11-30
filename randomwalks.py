import pygame as pg
import random as r 
import time as t

#seed can be any number, different seed generates different walks every time
while True:
    seed = input("Enter seed to use")
    if seed.isnumeric():
        seed = int(seed)
        print("Seed is ", seed)
        break
    else:
        print("Invalid input")
        continue

#screen dimensions & init
scr = (1080,1080) 
screen = pg.display.set_mode(scr)

#game clock
clock = pg.time.Clock()

#data structure of { (X1,Y1) : (R,G,B), (X2,Y2) : (R,G,B),... }
#where each pixel-key onscreen is stored with corresponding rgb-value
#coords are adjusted to make 0 in the middle
scr_info = {}

#no. of walks
walkcount = 4
#how many pixels each walk takes in total
steps_per_walk = 100000

#magnification between pixels where 1 means 1:1 correspondence with screen resolution
zoom_offset = 1
#which coords are drawn to the center
translation_offset = [0,0]
move_val = 10
zoom_increment = 0.2


#walkgen
def walkgen(seed,wcount,stepspwalk):
    r.seed(seed)
    for i in range(wcount):
        color = 255
        prev_step=  [0,0] 
        c = 0
        for j in range(stepspwalk): #a step can either be backwards or forwards
            n1 = r.randint(0,1)
            n2 = r.randint(0,1)
            if n1 == 0:
                n1 = -1
            else:
                n1 = 1
            if n2 == 0:
                n2 = -1
            else:
                n2 = 1
            
            #linear interpolation between 2 color extremes
            color = int(pg.math.lerp(0,255,c * 1/stepspwalk)) 
            prev_step = [n1 + prev_step[0] , n2 + prev_step[1]]
            scr_info[ ( prev_step[0], prev_step[1] ) ] = (color , 0 , 255 - color) #red-blue
            c += 1

walkgen_init_time = t.time()
walkgen(seed,walkcount,steps_per_walk)
walkgen_end_time = t.time()

def Draw_frame(): # render scr_info into the screen
    global zoom_offset,scr

    screen.fill(0)

    for coord in scr_info: #key-x,y value value- r,g,b
        pg.draw.circle(screen,scr_info[coord],
        ( (((coord[0] * zoom_offset) - translation_offset[0]) + (scr[0]/2)  ),
          (( coord[1] * zoom_offset) - translation_offset[1]) + (scr[1]/2)  ), #correct coords to center on 0
        1)
        
Draw_frame()
print(f"Walkgen time = {round(walkgen_end_time - walkgen_init_time,3)}")

running = True
while running == True:
    pg.event.get()

    keys = pg.key.get_pressed() #list of keys where index no. = key no., True = held down
                                #pg.event MUST be run for this to work

    #escape to quit
    if keys[pg.K_ESCAPE]:
        running = False

    #up and down increments and decrements current walkgen seed and regenerates it
    if keys[pg.K_UP]:
        seed += 1
        scr_info = dict()
        walkgen(seed,walkcount,steps_per_walk)
    if keys[pg.K_DOWN]:
        seed -= 1
        scr_info = dict()
        walkgen(seed,walkcount,steps_per_walk)


    # r to zoom in, f to zoom out
    if keys[pg.K_r]:
        zoom_offset += zoom_increment           
    if keys[pg.K_f]:
        zoom_offset -= zoom_increment
    
    #wasd to move camera
    if keys[pg.K_w]:
        translation_offset[1] -= move_val * zoom_offset
    if keys[pg.K_s]:
        translation_offset[1] += move_val * zoom_offset
    if keys[pg.K_a]:
        translation_offset[0] -= move_val * zoom_offset
    if keys[pg.K_d]:
        translation_offset[0] += move_val * zoom_offset
        
    Draw_frame()

    pg.display.flip()
    clock.tick(60)
        
pg.quit()
