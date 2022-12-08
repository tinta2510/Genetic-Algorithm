import pygame,sys 
from pygame.locals import *
import time 

map = [[0,0,0,0,5,0,0,0],[0,0,0,0,1,1,0,0],[0,0,0,0,1,2,1,0],[0,1,1,0,1,2,2,0],[1,2,2,1,1,0,1,0],[0,1,2,1,1,0,2,1],[0,0,1,2,1,0,2,1],[0,0,0,1,1,1,1,0],[0,0,0,0,1,1,0,0]] #a=0,b=4
#Initial position:
a1 = 0
b1 = 4
solution = ['r', 'u', 'r', 'r', 'r', 'd', 'l', 'l', 'l', 'd', 'r', 'u', 'u', 'u', 'r', 'r', 'l', 'u', 'r', 'u', 'r', 'd', 'r', 'd', 'd', 'r', 'u', 'l', 'd', 'd', 'd', 'l', 'r', 'd', 'l', 'd', 'u', 'u', 'l', 'd', 'd', 'd']
size = 70 #block_size
WINDOWHEIGHT = len(map)*size
WINDOWWIDTH  = len(map[0])*size

BLACK   = (  0,   0,   0)
WHITE   = (255, 255, 255)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)
YELLOW  = (255, 255,   0)  
BROWN   = (184, 134,  11)
GRAY    = (169, 169, 169)

pygame.init() 

FPS = 1
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Reach_the_flag')

x = a1*size
y = WINDOWHEIGHT-(b1+1)*size

k = -1
a = a1
b = b1

while True: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(BLACK)
    for j in range(len(map)): 
        for i in range(len(map[j])): 
            if map[j][i] == 1: pygame.draw.rect(DISPLAYSURF,YELLOW, ((i*size,WINDOWHEIGHT-(j+1)*size,size,size)))
            if map[j][i] == 2: pygame.draw.rect(DISPLAYSURF, BROWN, ((i*size,WINDOWHEIGHT-(j+1)*size,size,size)))
            if map[j][i] == 3: pygame.draw.rect(DISPLAYSURF,  GRAY, ((i*size,WINDOWHEIGHT-(j+1)*size,size,size)))
            if map[j][i] == 5: pygame.draw.rect(DISPLAYSURF,   RED, ((i*size,WINDOWHEIGHT-(j+1)*size,size,size)))
   
    surface = pygame.Surface((size,size),SRCALPHA)
    pygame.draw.circle(surface, BLUE, (size/2,size/2), size/2)
    DISPLAYSURF.blit(surface, (x,y))
    pygame.display.update()

    if k < len(solution)-1: k+=1
    else: 
        time.sleep(3)
        break    
    if map[b][a] == 1: map[b][a] = 0
    elif map[b][a] == 2: map[b][a] = 1
    if solution[k] == 'r': 
        x += size
        a += 1 
    elif solution[k] == 'l': 
        x -= size
        a -= 1
    elif solution[k] == 'u': 
        y -= size
        b += 1
    elif solution[k] == 'd': 
        y += size
        b -= 1
       
    fpsClock.tick(FPS) 

