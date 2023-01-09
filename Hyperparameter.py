import random
import time,copy
import numpy as np 

para_pop=[] #parameter_population
para_pop_size = 10 #parameter_population_size

pop_size_max = 300 #population_size_max
n_time = 3 #number of times to run a CHROMOSOME
para_parents_num = 4



#Round: 
Round = 5
match Round:
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

#Calculate chromosome_length:
chromosome_length = 0
for i in map_game: 
   for j in i: 
      if j == 1: chromosome_length+=1
      if j == 2: chromosome_length+=2
      if (j == 3) or (j==5): chromosome_length+=5

#Initial_PARAMETER_population:
for i in range(para_pop_size): 
   pop_size = random.choice(np.arange(20,pop_size_max,10))
   parents_num = random.choice(np.arange(10,pop_size,10))
   lis = [pop_size,parents_num]
   para_pop.append(lis)

#RTF_Find_optimal_parameter_function:
##Run parameter_population and return how many generations needed to find solution:
def run_parameter_population(lis):
    population_size = lis[0]
    parents_number = lis[1] 
    move_list = ['r','l','u','d']
    elite_size = 5
    mutation_rate = 0.6

    #Initial population:
    population = []
    for i in range(int(population_size)):
        chromosome = []
        for x in range(chromosome_length):
            chromosome.append(random.choice(move_list))
        population.append(chromosome)
    generation = 0

    #RTF_Find_Solution_function:
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
                        void += 1
                        continue
                    elif map[b][a] == 0: 
                        b -= 1
                        void += 1
                        continue
                    elif map[b][a] == 1: map[b][a] -= 1
                    elif map[b][a] == 2: map[b][a] -= 1
                elif i == 'd': 
                    b -= 1
                    if (b<0):
                        b += 1 
                        void += 1
                        continue
                    elif map[b][a] == 0: 
                        b += 1
                        void += 1
                        continue
                    elif map[b][a] == 1: map[b][a] -= 1
                    elif map[b][a] == 2: map[b][a] -= 1
                elif i == 'r': 
                    a += 1
                    if (a > len(map[0])-1): 
                        a -= 1 
                        void += 1
                        continue
                    elif map[b][a] == 0: 
                        a -= 1
                        void += 1
                        continue
                    elif map[b][a] == 1: map[b][a] -= 1
                    elif map[b][a] == 2: map[b][a] -= 1
                elif i == 'l':  
                    a -= 1
                    if (a<0): 
                        a += 1 
                        void += 1
                        continue
                    elif map[b][a] == 0: 
                        a += 1
                        void += 1
                        continue
                    elif map[b][a] == 1: map[b][a] -= 1
                    elif map[b][a] == 2: map[b][a] -= 1  
            for y in range(len(map)):
                for x in map[y]:
                    if x==1: match += 1
                    if x==2: match += 2
            distance = abs(a0-a) + abs(b0-b)
            if (match+distance) == 0: result = [chromosome , match + distance]
            else: result = [chromosome , match + distance + void]
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

    while True:
        fitness_scores = fitness(population)
        if min([i[1] for i in fitness_scores]) == 0:
            #solution = [i[0] for i in fitness_scores if i[1] == 0][0] 
            break
        parents = select_parents(fitness_scores) #Chọn ra cặp bó mẹ có điểm cao nhất
        children = create_children(parents) #Tạo thế hệ con từ parents
        population = mutation(children) #Quần thể sau đột biến
        generation += 1
        if generation == 15000:
            generation += 15000
            break
    return generation

def evaluate_para_pop_fitness(para_pop):
    result = []
    for chromosome in para_pop:
        ave_gen = 0 #average_generation
        for i in range(n_time):
            ave_gen += run_parameter_population(chromosome)
        ave_gen /= n_time
        result.append([chromosome,round(ave_gen,2)])
    return sorted(result,key = lambda x: x[1])

def select(result): 
    parents_list = []
    for chromosome in result[:para_parents_num]:
        parents_list.append(chromosome[0])
    return parents_list

def para_crossover(parent1,parent2):
    rate = random.random()
    child = []
    new_pop_num = round(parent1[0]*rate + parent2[0]*(1-rate),-1)
    new_parents_num = round(parent1[1]*rate + parent2[1]*(1-rate),-1)

    #While new_parents_num is too small or bigger than new_pop_num, recreate new_parents_num:
    while (new_parents_num<10) or (new_parents_num*1.1 > new_pop_num): 
        if (new_parents_num<10): new_parents_num += 10
        elif (new_parents_num*1.1 > new_pop_num): new_parents_num -= 10

    child.append(int(new_pop_num))
    child.append(int(new_parents_num))
    return child

def new_gen(parents_list):
    new_gen = []
    for i in range(para_pop_size):
        parent1 = parents_list[random.randint(0,para_parents_num-1)]
        parent2 = parents_list[random.randint(0,para_parents_num-1)]    
        new_gen.append(para_crossover(parent1,parent2))
    return new_gen 

def create_mutation(new_gen): 
    for i in new_gen: 
        if (random.random() > 0.5):
            i[0] += random.choice(np.arange(-50,50,10))
            i[1] += random.choice(np.arange(-50,50,10))
        else: continue
        while (i[1]<10) or (i[1]*1.1 > i[0]): 
            if (i[1]<10): i[1] += 10
            elif (i[1]*1.1 > i[0]): i[1] -= 10
    return new_gen

print('Initial parameter_population: ')
print(evaluate_para_pop_fitness(para_pop),'\n')
for i in range(10): 
    t = time.time()
    result = evaluate_para_pop_fitness(para_pop)
    parents_list = select(result)
    new_geneneration = new_gen(parents_list)
    para_pop = create_mutation(new_geneneration) 
    print('population{}:'.format(i+1))
    print(evaluate_para_pop_fitness(para_pop))
    print("time: ",time.time()-t,'\n')
    

