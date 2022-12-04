import random,time,copy
round = 12
match round:
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
    case 7: 
        map_game = [[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1],[1,1,1,1,1,1],[0,0,1,1,1,1],[0,0,1,1,1,1],[0,0,5,1,0,0]] #a=2,b=5
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
    case 12: 
        map_game = [[0,0,0,5,0,0],[0,0,1,1,0,0],[0,1,2,1,1,0],[1,2,2,1,1,0],[1,2,1,0,1,1],[1,1,1,1,1,1],[0,0,1,2,2,1],[0,0,0,1,1,0]] #a=0,b=3
        #Flag:
        a0 = 3
        b0 = 0
        #Initial position:
        a1 = 0
        b1 = 3

map_game[b1][a1] = 0

move_list = ['r','l','u','d']
elite_size = 5
chromosome_length = 0
population_size = 30
parents_number = 15

for i in map_game: 
    for j in i: 
        if j == 1: chromosome_length+=1
        if j == 2: chromosome_length+=2
        if (j == 3) or (j==5): chromosome_length+=4

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
        distance = 0 
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
            elif i == 'd': 
                b-= 1
                if (b<0):
                    b+= 1 
                    continue
                if map[b][a] == 0: 
                    b+= 1
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            elif i == 'r': 
                a+= 1
                if (a > len(map[0])-1): 
                    a-= 1 
                    continue
                if map[b][a] == 0: 
                    a-= 1
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            elif i == 'l':  
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
        result = [chromosome,match+distance]
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

    start = min(positionA, positionB) #start and end position of crossover
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
        children.append(crossover(parent1,parent2)) 
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
        a = [i[0] for i in fitness_scores if i[1] == 0][0] 
        print("Discovered solution for round {} = {}".format(round,))
        print("In {} generations and {} seconds".format(generation,time.time() - t0))
        break
    parents = select_parents(fitness_scores) 
    children = create_children(parents)
    population = mutation(children) #New population
    generation += 1
    if generation % 5000 == 0: print("Running at generation {},time: {} seconds".format(generation,time.time() - t0))
    if generation == 10000:
        print("Break at generation {},in {} seconds".format(generation,time.time() - t0))
        solution = [i[0] for i in sorted(fitness_scores,key = lambda x: x[1])[:1]]
        mark = [i[1] for i in sorted(fitness_scores,key = lambda x: x[1])[:1]]
        print("Best way coud be found for round {}: {}, fitness_score: {}".format(round,solution[0],mark[0]))
        break

