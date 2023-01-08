import random
import time,copy
import pygame,sys
from pygame.locals import *
round = 7 #Round 1-19 
match round:
    case 1:
        map_game = [[1],[1],[1],[1],[1],[5]]
        #Flag:
        a0 = 0
        b0 = 5
        #Initial position:
        a1 = 0
        b1 = 0
    case 2: 
        map_game = [[1,1,1,1,1,5]]
        #Flag:
        a0 = 5
        b0 = 0
        #Initial position:
        a1 = 0
        b1 = 0

    case 3:
        map_game = [[1,1,1,1,1,1,5],[0,0,0,0,0,1,1]] #a=0,b=0
        #Flag:
        a0 = 6
        b0 = 0
        #Initial position:
        a1 = 0
        b1 = 0
    case 4: 
        map_game = [[1,1,1,2,5],[0,0,0,1,0]] #a=0,b=0
        #Flag:
        a0 = 4
        b0 = 0
        #Initial position:
        a1 = 0
        b1 = 0
    case 5:
        map_game = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[1,1,1,3,1],[0,0,0,1,0]]
        #Flag:
        a0 = 4
        b0 = 1 
        #Initial position:
        a1 = 0
        b1 = 4
    case 6:
        map_game = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,5,1,1],[0,0,1,1]] #a=0,b=2
        #Flag: 
        a0 = 1
        b0 = 3
        #Initial position:
        a1 = 0
        b1 = 2
    case 7: 
        map_game = [[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1],[1,1,1,1,1,1],[0,0,1,1,1,1],[0,0,5,1,0,0]] #a=2,b=5
        #Flag:
        a0 = 2
        b0 = 5 
        #Initial position:
        a1 = 2
        b1 = 5
    case 8:
        map_game = [[1,1,1,1,1,0],[1,1,1,1,2,1],[1,1,1,0,1,1],[1,1,1,1,1,1],[5,2,1,1,1,0],[0,1,1,1,1,0]] #a=5,b=3
        #Flag:
        a0 = 0
        b0 = 4
        #Initial position:
        a1 = 5
        b1 = 3
    case 9: 
        map_game = [[0,0,1,1,0,1,1,0,0],[0,1,2,1,1,2,1,0,0],[1,2,1,1,2,1,0,1,1],[0,1,1,1,1,1,1,2,1],[0,0,0,0,1,1,1,1,0],[0,0,0,0,0,0,5,0,0]] #a=0,b=2
        #Flag:
        a0 = 6
        b0 = 5
        #Initial position:
        a1 = 0
        b1 = 2
    case 10: 
        map_game = [[0,1,0,0,0,0],[0,1,0,0,0,0],[0,1,0,0,0,0],[1,2,1,0,0,0],[1,2,3,1,1,5],[0,1,1,0,0,0]]
        #Flag:
        a0 = 5
        b0 = 4
        #Initial position:
        a1 = 1
        b1 = 0
    case 11: 
        map_game = [[0,0,5,0],[0,0,1,0],[1,1,1,1],[1,2,1,1],[1,2,2,1],[1,2,1,0],[0,1,0,0]]
        #Flag:
        a0 = 2
        b0 = 0
        #Initial position:
        a1 = 1
        b1 = 6        
    case 12: 
        map_game = [[0,0,0,5,0,0],[0,0,1,1,0,0],[0,1,2,1,1,0],[1,2,2,1,1,0],[1,2,1,0,1,1],[1,1,1,1,1,1],[0,0,1,2,2,1],[0,0,0,1,1,0]] #a=0,b=3
        #Flag:
        a0 = 3
        b0 = 0
        #Initial position:
        a1 = 0
        b1 = 3
    case 13: 
        map_game = [[0,0,0,0,5,0,0,0],[0,0,0,0,1,1,0,0],[0,0,0,0,1,2,1,0],[0,1,1,0,1,2,2,0],[1,2,2,1,1,0,1,0],[0,1,2,1,1,0,2,1],[0,0,1,2,1,0,2,1],[0,0,0,1,1,1,1,0],[0,0,0,0,1,1,0,0]] #a=0,b=4
        #Flag:
        a0 = 4
        b0 = 0
        #Initial position:
        a1 = 0
        b1 = 4
    case 14: 
        map_game = [[0,0,1,1,0,0,0,0,0],[0,0,1,2,1,1,1,2,1],[1,1,1,1,1,0,1,2,1],[0,0,1,2,1,3,1,1,1],[0,0,0,2,1,0,1,0,0],[0,0,0,1,2,1,1,0,0],[0,0,0,0,5,0,0,0,0]] #a=0,b=2
        #Flag:
        a0 = 4
        b0 = 6
        #Initial position: 
        a1 = 0 
        b1 = 2
    case 15: 
        map_game = [[0,0,1,1,1],[1,1,1,5,1],[1,1,1,2,2],[1,2,3,2,1],[1,1,0,1,0],[1,1,1,1,0],[0,1,2,1,0]] #a=2,b=3
        #Flag: 
        a0 = 3
        b0 = 1
        #Initial position:
        a1 = 2
        b1 = 3
    case 16:
        map_game = [[0,0,0,0,1,2,1,1,0],[0,0,0,1,1,2,1,2,0],[0,1,1,1,2,1,0,2,5],[1,1,2,1,2,1,0,1,0],[0,0,2,0,0,2,1,1,0],[0,0,2,2,1,2,1,0,0],[0,0,0,1,1,1,1,0,0],[0,0,0,0,1,1,0,0,0]] #a=0,b=3
        #Flag: 
        a0 = 8 
        b0 = 2
        #Initial position: 
        a1 = 0 
        b1 = 3
    case 17: 
        map_game = [[0,0,0,0,2,2,0],[0,0,0,0,2,2,0],[0,1,1,1,2,1,0],[1,2,1,2,3,1,1],[2,3,0,0,1,2,1],[1,1,1,1,0,2,1],[0,0,2,2,1,1,5],[0,0,1,0,1,1,0]]
        #Flag: 
        a0 = 6 
        b0 = 6
        #Initial position: 
        a1 = 0 
        b1 = 5   
    case 18: 
        map_game = [[0,0,0,1,1,0,0],[0,0,0,1,2,1,1],[0,0,1,1,1,0,1],[5,1,1,1,1,0,1],[0,1,2,2,1,1,1],[0,0,1,2,1,1,0],[0,0,0,1,1,0,0],[0,0,0,0,1,0,0]]
        #Flag: 
        a0 = 0
        b0 = 3
        #Initial position: 
        a1 = 4
        b1 = 7
    case 19: 
        map_game = [[0,0,0,1,5,0],[0,0,1,1,0,0],[0,0,1,2,1,1],[1,1,1,2,1,1],[1,2,1,0,2,1],[1,1,1,2,2,1],[1,0,1,1,0,1],[1,1,1,0,1,1],[0,0,1,1,1,0],[0,0,1,1,0,0]]
        #Flag: 
        a0 = 4
        b0 = 0
        #Initial position: 
        a1 = 3
        b1 = 5
if (map_game[b1][a1] == 1) or (map_game[b1][a1] == 2): map_game[b1][a1] -= 1

move_list = ['r','l','u','d']
elite_size = 5
chromosome_length = 0
population_size = 40
parents_number = 25
mutation_rate = 0.6
void_mark = 1.1

for i in map_game: 
    for j in i: 
        if j == 1: chromosome_length+=1
        if j == 2: chromosome_length+=2
        if (j == 3) or (j==5): chromosome_length+=5

#Initial population
population = []
for i in range(population_size):
    chromosome = []
    for x in range(chromosome_length):
        chromosome.append(random.choice(move_list))
    population.append(chromosome)

#Evaluate fitness
def fitness(population):
    fitness_scores = []
    for chromosome in population:
        a = a1
        b = b1
        map = copy.deepcopy(map_game)
        result = []
        match = 0 
        void = 0
        distance = 0 #Distance between the last position of player and flag
        for i in chromosome: 
            if i == 'u': 
                b += 1
                if (b > len(map)-1): 
                    b -= 1 
                    void += void_mark
                    continue
                elif map[b][a] == 0: 
                    b -= 1
                    void += void_mark
                    continue
                elif map[b][a] == 1: map[b][a] -= 1
                elif map[b][a] == 2: map[b][a] -= 1
            elif i == 'd': 
                b -= 1
                if (b<0):
                    b += 1 
                    void += void_mark
                    continue
                elif map[b][a] == 0: 
                    b += 1
                    void += void_mark
                    continue
                elif map[b][a] == 1: map[b][a] -= 1
                elif map[b][a] == 2: map[b][a] -= 1
            elif i == 'r': 
                a += 1
                if (a > len(map[0])-1): 
                    a -= 1 
                    void += void_mark
                    continue
                elif map[b][a] == 0: 
                    a -= 1
                    void += void_mark
                    continue
                elif map[b][a] == 1: map[b][a] -= 1
                elif map[b][a] == 2: map[b][a] -= 1
            elif i == 'l':  
                a -= 1
                if (a<0): 
                    a += 1 
                    void += void_mark
                    continue
                elif map[b][a] == 0: 
                    a += 1
                    void += void_mark
                    continue
                elif map[b][a] == 1: map[b][a] -= 1
                elif map[b][a] == 2: map[b][a] -= 1  
        for y in range(len(map)):
            for x in map[y]:
                if x==1: match += 1
                if x==2: match += 2
        distance = abs(a0-a) + abs(b0-b)
        if (match+distance) == 0: result = [chromosome , match + distance]
        else: result = [chromosome , match + distance*1.7 + void]
        fitness_scores.append(result)
    return fitness_scores 
    
def select_parents(fitness_scores):
    parents_list = []
    for chromosome in sorted(fitness_scores,key = lambda x: x[1])[:parents_number]:
        parents_list.append(chromosome[0])
    return(parents_list) 

def crossover(parent1,parent2):
    child = []
    
    positionA = random.randint(0,chromosome_length-1)
    positionB = random.randint(0,chromosome_length-1)

    start = min(positionA, positionB) #Start and end position of Crossover
    end = max(positionA, positionB)

    for i in range(0,chromosome_length):
        if (i < start) or (i > end):
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

def create_children(parents): #parents = select_parents(fitness_scores)
    children = []
    num_new_children = len(population) - elite_size

    for i in range(0,elite_size):
        children.append(parents[i]) #Retain elite parents

    for i in range(0,num_new_children): 
        parent1 = parents[random.randint(0,len(parents)-1)]
        parent2 = parents[random.randint(0,len(parents)-1)]
        children.append(crossover(parent1,parent2)) 
    return children

def mutation(children): 
    for i in range(len(children)):
        if random.random() > mutation_rate:
            swap_position1 = int(random.random() * chromosome_length)
            swap_position2 = int(random.random() * chromosome_length)
            t = children[i][swap_position1]
            children[i][swap_position1] = children[i][swap_position2] 
            children[i][swap_position2] = t
        else:
            mutated_position = int(random.random() * chromosome_length) #Mutated position
            mutation = random.choice(move_list) 
            children[i][mutated_position] = mutation
    return children
generation = 0
t0 = time.time()
while True:
    fitness_scores = fitness(population)
    if min([i[1] for i in fitness_scores]) == 0:
        solution = [i[0] for i in fitness_scores if i[1] == 0][0] 
        #print("Discovered solution for round {} = {}".format(round,solution))
        print("Solved round {} at generation {},in {} seconds".format(round,generation,time.time() - t0))
        break
    parents = select_parents(fitness_scores) #Chọn ra cặp bó mẹ có điểm cao nhất
    children = create_children(parents) #Tạo thế hệ con từ parents
    population = mutation(children) #Quần thể sau đột biến
    generation += 1
    if generation % 5000 == 0: print("Running at generation {},time: {} seconds".format(generation,time.time() - t0))
    if generation == 15000:
        print("Break at generation {},in {} seconds".format(generation,time.time() - t0))
        solution = [i[0] for i in sorted(fitness_scores,key = lambda x: x[1])[:1]]
        mark = [i[1] for i in sorted(fitness_scores,key = lambda x: x[1])[:1]]
        solution = solution[0]
        print("Best way coud be found for round {}: {}, fitness_score: {}".format(round,solution,mark[0]))
        break

#Print Solution: 
a=a1
b=b1
map = copy.deepcopy(map_game)
i=0
while True:
    if i >= len(solution): break
    if solution[i] == 'u': 
        b+= 1
        if (b >= len(map)): 
            b -= 1
            solution.pop(i)
            continue
        if map[b][a] == 0: 
            b -= 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1
    elif solution[i] == 'd': 
        b-= 1
        if (b<0):
            b += 1
            solution.pop(i) 
            continue
        if map[b][a] == 0: 
            b += 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1        
    elif solution[i] == 'r': 
        a+= 1
        if (a >= len(map[0])): 
            a -= 1 
            solution.pop(i)
            continue
        if map[b][a] == 0: 
            a-= 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1  
    elif solution[i] == 'l':  
        a -= 1
        if (a<0): 
            a+= 1 
            solution.pop(i)
            continue
        if map[b][a] == 0: 
            a += 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1  
    i+=1

print("Move = {}".format(solution))

print('\a')
#Build UI:
map = copy.deepcopy(map_game)
size = 60 #block_size
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

FPS = 1.5
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('Reach_the_flag_Round{}'.format(round))

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

