import random 
#Map game 5:
map5 = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[1,1,1,3,1],[0,0,0,1,0]]
#Vị trí đích:
a0 = 4
b0 = 1 
#Vị trí ban đầu: 
a1 = 0
b1 = 4
map5[b1][a1] = 0

move_list = ['r','l','u','d']

chromosome_length = 20

population_size = 5
#Initial population
population = []
for i in range(population_size):
    chromosome = []
    for x in range(chromosome_length):
        chromosome.append(random.choice(move_list))
    population.append(chromosome)

#Evaluation fitness
def fitness(population):
    
    a = a1
    b = b1
    fitness_scores = []
    for chromosome in population:
        map = map5
        result = []
        match = 0 #Do phu hop cua tung Chromosome
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
        distance = (abs(a1-a) + abs(b1-b))/2
        result = [chromosome,match,distance]
        fitness_scores.append(result)
    return fitness_scores

'''
for y in range(len(map)-1,-1,-1):
    for x in range(len(map[y])):
        print(map[y][x],end=' | ')
    print()
print(result,"\n","\n","\n")
'''

