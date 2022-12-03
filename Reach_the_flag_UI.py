import random,time,copy,pygame,sys
from pygame.locals import *
#Map game 5:
map_game = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[1,1,1,3,1],[0,0,0,1,0]]
#Vi tri dich
a0 = 4
b0 = 1 
#Vi tri ban dau
a1 = 0
b1 = 4
map_game[b1][a1] = 0

move_list = ['r','l','u','d']
elite_size = 3
chromosome_length = 0

population_size = 20
parents_number = 10

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
        match = 0 #Số ô còn lại
        distance = 0 #Khoảng cách từ vị trí cuối đến vị trí đích
        #Chạy thử các bước di chuyển trên bản đồ
        for i in chromosome: 
            if i == 'u': 
                b+= 1
                if (b > len(map)-1): 
                    b-= 1 
                    continue
                if map[b][a] == 0: 
                    b-= 1
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            if i == 'd': 
                b-= 1
                if (b<0):
                    b+= 1 
                    continue
                if map[b][a] == 0: 
                    b+= 1
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            if i == 'r': 
                a+= 1
                if (a > len(map[0])-1): 
                    a-= 1 
                    continue
                if map[b][a] == 0: 
                    a-= 1
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            if i == 'l':  
                a-= 1
                if (a<0): 
                    a+= 1 
                    continue
                if map[b][a] == 0: 
                    a+= 1
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1  
        for y in range(len(map)):
            for x in map[y]:
                if x==1: match += 1
                if x==2: match += 2
        distance = abs(a0-a) + abs(b0-b)
        result = [chromosome,match*2+distance]
        fitness_scores.append(result)
    return fitness_scores

#Chọn những Choromosome có fitness_score cao nhất để làm thể hệ bố mẹ
def select_parents(fitness_scores):
    parents_list = []
    for chromosome in sorted(fitness_scores,key = lambda x: x[1])[:parents_number]:
        parents_list.append(chromosome[0])
    return(parents_list)

def crossover(parent1,parent2):
    child = []
    
    positionA = random.randint(0,chromosome_length-1)
    positionB = random.randint(0,chromosome_length-1)

    start = min(positionA, positionB) #điểm bắt đầu và kết thúc crossover
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
        children.append(parents[i]) #Giữ lại những NST bố (mẹ) tốt (những NST xếp đầu trong list parents)

    for i in range(0,num_new_children): #Những NST còn lại đem đi tạo thế hệ con 
        parent1 = parents[random.randint(0,len(parents)-1)]
        parent2 = parents[random.randint(0,len(parents)-1)]
        children.append(crossover(parent1,parent2)) #Dùng hàm breed() ở trên
    return children

def mutation(children): 
    for i in range(len(children)):
        if random.random() > 0.3:
            continue
        else:
            mutated_position = int(random.random() * chromosome_length) #Vị trí xảy ra đột biến
            mutation = random.choice(move_list) #Chọn số bất kỳ để thay 
            children[i][mutated_position] = mutation
    return children
generation = 0
t0 = time.time()
while True:
    fitness_scores = fitness(population)
    if min([i[1] for i in fitness_scores]) == 0:
        solution = [i[0] for i in fitness_scores if i[1] == 0][0] 
        print("Discovered solution = {}".format(solution))
        print("In {} generations and {} seconds".format(generation,time.time() - t0))
        break
    parents = select_parents(fitness_scores) #Chọn ra cặp bó mẹ có điểm cao nhất
    children = create_children(parents) #Tạo thế hệ con từ parents
    population = mutation(children) #Quần thể sau đột biến
    generation += 1
    if generation == 200000:
        print("Break at generation: {}".format(generation))
        break

#Print Solution: 
a=a1
b=b1
map = copy.deepcopy(map_game)
i=0
while True:
    if solution[i] == 'u': 
        b+= 1
        if (b > len(map)-1): 
            b-= 1
            solution.pop(i)
            continue
        if map[b][a] == 0: 
            b-= 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1
    elif solution[i] == 'd': 
        b-= 1
        if (b<0):
            b+= 1
            solution.pop(i) 
            continue
        if map[b][a] == 0: 
            b+= 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1        
    elif solution[i] == 'r': 
        a+= 1
        if (a > len(map[0])-1): 
            a-= 1 
            solution.pop(i)
            continue
        if map[b][a] == 0: 
            a-= 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1  
    elif solution[i] == 'l':  
        a-= 1
        if (a<0): 
            a+= 1 
            solution.pop(i)
            continue
        if map[b][a] == 0: 
            a+= 1
            solution.pop(i)
            continue
        if map[b][a] == 1: map[b][a] -= 1
        if map[b][a] == 2: map[b][a] -= 1  
    i+=1
    if i == len(solution): break

print("Discovered solution = {}".format(solution))

#Build UI:
map = copy.deepcopy(map_game)
size = 100 #block_size
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
        time.sleep(5)
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

