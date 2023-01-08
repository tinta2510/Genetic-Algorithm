import pygame,sys 
from pygame.locals import *
import time 

round = 5 #Round 1-18 #Cannot solve round 7,15,16   17?
match round:
    case 1:
        map = [[1],[1],[1],[1],[1],[5]]
        #Initial position:
        a1 = 0
        b1 = 0
    case 2: 
        map = [[1,1,1,1,1,5]]
        #Initial position:
        a1 = 0
        b1 = 0
    case 3:
        map = [[1,1,1,1,1,1,5],[0,0,0,0,0,1,1]] #a=0,b=0
        #Initial position:
        a1 = 0
        b1 = 0
    case 4: 
        map = [[1,1,1,2,5],[0,0,0,1,0]] #a=0,b=0
        #Initial position:
        a1 = 0
        b1 = 0
    case 5:
        map = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[1,1,1,3,1],[0,0,0,1,0]]
        #Initial position:
        a1 = 0
        b1 = 4
    case 6:
        map = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,5,1,1],[0,0,1,1]] #a=0,b=2
        #Initial position:
        a1 = 0
        b1 = 2
    case 7: 
        map = [[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1],[1,1,1,1,1,1],[0,0,1,1,1,1],[0,0,5,1,0,0]] #a=2,b=5
        #Initial position:
        a1 = 2
        b1 = 5
    case 8:
        map = [[1,1,1,1,1,0],[1,1,1,1,2,1],[1,1,1,0,1,1],[1,1,1,1,1,1],[5,2,1,1,1,0],[0,1,1,1,1,0]] #a=5,b=3
        #Initial position:
        a1 = 5
        b1 = 3
    case 9: 
        map = [[0,0,1,1,0,1,1,0,0],[0,1,2,1,1,2,1,0,0],[1,2,1,1,2,1,0,1,1],[0,1,1,1,1,1,1,2,1],[0,0,0,0,1,1,1,1,0],[0,0,0,0,0,0,5,0,0]] #a=0,b=2
        #Initial position:
        a1 = 0
        b1 = 2
    case 10: 
        map = [[0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[1,2,1,0,0,0],[1,2,3,1,1,5],[0,1,1,0,0,0]]
        #Initial position:
        a1 = 1
        b1 = 0
    case 11: 
        map = [[0,0,5,0],[0,0,1,0],[1,1,1,1],[1,2,1,1],[1,2,2,1],[1,2,1,0],[0,1,0,0]]
        #Initial position:
        a1 = 1
        b1 = 6        
    case 12: 
        map = [[0,0,0,5,0,0],[0,0,1,1,0,0],[0,1,2,1,1,0],[1,2,2,1,1,0],[1,2,1,0,1,1],[1,1,1,1,1,1],[0,0,1,2,2,1],[0,0,0,1,1,0]] #a=0,b=3
        #Initial position:
        a1 = 0
        b1 = 3
    case 13: 
        map = [[0,0,0,0,5,0,0,0],[0,0,0,0,1,1,0,0],[0,0,0,0,1,2,1,0],[0,1,1,0,1,2,2,0],[1,2,2,1,1,0,1,0],[0,1,2,1,1,0,2,1],[0,0,1,2,1,0,2,1],[0,0,0,1,1,1,1,0],[0,0,0,0,1,1,0,0]] #a=0,b=4
        #Initial position:
        a1 = 0
        b1 = 4
    case 14: 
        map = [[0,0,1,1,0,0,0,0,0],[0,0,1,2,1,1,1,2,1],[1,1,1,1,1,0,1,2,1],[0,0,1,2,1,3,1,1,1],[0,0,0,2,1,0,1,0,0],[0,0,0,1,2,1,1,0,0],[0,0,0,0,5,0,0,0,0]] #a=0,b=2
        #Initial position: 
        a1 = 0 
        b1 = 2
    case 15: 
        map = [[0,0,1,1,1],[1,1,1,5,1],[1,1,1,2,2],[1,2,3,2,1],[1,1,0,1,0],[1,1,1,1,0],[0,1,2,1,0]] #a=2,b=3
        #Initial position:
        a1 = 2
        b1 = 3
    case 16:
        map = [[0,0,0,0,1,2,1,1,0],[0,0,0,1,1,2,1,2,0],[0,1,1,1,2,1,0,2,5],[1,1,2,1,2,1,0,1,0],[0,0,2,0,0,2,1,1,0],[0,0,2,2,1,2,1,0,0],[0,0,0,1,1,1,1,0,0],[0,0,0,0,1,1,0,0,0]] #a=0,b=3
        #Initial position: 
        a1 = 0 
        b1 = 3
    case 17: 
        map = [[0,0,0,0,2,2,0],[0,0,0,0,2,2,0],[0,1,1,1,2,1,0],[1,2,1,2,3,1,1],[2,3,0,0,1,2,1],[1,1,1,1,0,2,1],[0,0,2,2,1,1,5],[0,0,1,0,1,1,0]]
        #Initial position: 
        a1 = 0 
        b1 = 5   
    case 18: 
        map = [[0,0,0,1,1,0,0],[0,0,0,1,2,1,1],[0,0,1,1,1,0,1],[5,1,1,1,1,0,1],[0,1,2,2,1,1,1],[0,0,1,2,1,1,0],[0,0,0,1,1,0,0],[0,0,0,0,1,0,0]]
        #Initial position: 
        a1 = 4
        b1 = 7
solution = ['l', 'd', 'd', 'l', 'u', 'u', 'r', 'u', 'l', 'u', 'r',
'u', 'r', 'r', 'l', 'd', 'r', 'd', 'd', 'd', 'r', 'd', 'd', 'l', 'l', 'u', 'u', 'u', 'r', 'r', 'd', 'l', 'd']
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

FPS = 0.5
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
    if map[b][a] == 1: map[b][a] -= 1
    elif map[b][a] == 2: map[b][a] -= 1
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

