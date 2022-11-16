import random 

move_list = ['r','l','u','d']

chromosome_length = 20

population_size = 20
#Initial population
population = []
for i in range(population_size):
    chromosome = []
    for x in range(chromosome_length):
        chromosome.append(random.choice(move_list))
    population.append(chromosome)
#Evaluation fitness
def fitness(population):
    fitness_scores = []
    for chromosome in population:
        for i in chromosome: 
        if i == 'u': 
            b+=1
            if (b>len(map)-1): 
                b-=1 
                continue
            if map[b][a] == 0: 
                b-=1
                continue
            if map[b][a] == 1: map[b][a] -= 1
            if map[b][a] == 2: map[b][a] -= 1
            if map[b][a] == 5: 
                kt = 0
                for y in range(len(map)):
                    for x in map[y]: 
                        if (x!=0) and (x!=5) and (x!=3): 
                            kt += 1
                            break
                if kt == 0: 
                    print("Win")
                    kt1 = 1
                    break
                else: continue 
        if i == 'd': 
            b-=1
            if (b<0):
                b+=1 
                continue
            if map[b][a] == 0: 
                b+=1
                continue
            if map[b][a] == 1: map[b][a] -= 1
            if map[b][a] == 2: map[b][a] -= 1
            if map[b][a] == 5: 
                kt = 0
                for y in range(len(map)):
                    for x in map[y]: 
                        if (x!=0) and (x!=5) and (x!=3): 
                            kt += 1
                            break
                if kt == 0: 
                    print("Win")
                    kt1 = 1
                    break
                else: continue
        if i == 'r': 
            a+=1
            if (a>len(map[0])-1): 
                a-=1 
                continue
            if map[b][a] == 0: 
                a-=1
                continue
            if map[b][a] == 1: map[b][a] -= 1
            if map[b][a] == 2: map[b][a] -= 1
            if map[b][a] == 5: 
                kt = 0 #Kiểm tra xem các ô đã đạt yêu cầu chưa
                for y in range(len(map)):
                    for x in map[y]: 
                        if (x!=0) and (x!=5) and (x!=3): 
                            kt += 1
                            break
                if kt == 0: 
                    print("Win")
                    kt1 = 1
                    break
                else: continue
        if i == 'l': 
            a-=1
            if (b<0): 
                a+=1 
                continue
            if map[b][a] == 0: 
                a+=1
                continue
            if map[b][a] == 1: map[b][a] -= 1
            if map[b][a] == 2: map[b][a] -= 1
            if map[b][a] == 5: 
                kt = 0
                for y in range(len(map)):
                    for x in map[y]: 
                        if (x!=0) and (x!=5) and (x!=3): 
                            kt += 1
                            break
                if kt == 0: 
                    print("Win")
                    kt1 = 1
                    break
                else: continue   
        for i in range(len())