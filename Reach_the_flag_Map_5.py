import random 
#Map game 5:
map5 = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[1,1,1,3,1],[0,0,0,1,0]]
#Vi tri dich
a0 = 4
b0 = 1 
#Vi tri ban dau
a1 = 0
b1 = 4
map5[b1][a1] = 0

move_list = ['r','l','u','d']
elite_size = 3
chromosome_length = 15

population_size = 15
parents_number = 10
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
        map = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[0,1,1,3,1],[0,0,0,1,0]] 
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

    #parent1 = parents[0]
    #parent2 = parents[1]
    
    geneA = int(random.random() * chromosome_length)
    geneB = int(random.random() * chromosome_length)

    startGene = min(geneA, geneB) #điểm bắt đầu và kết thúc crossover
    endGene = max(geneA, geneB)

    for i in range(0,chromosome_length):
        if (i < startGene) or (i > endGene):
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
        parent1 = parents[int(random.random() * len(parents))]
        parent2 = parents[int(random.random() * len(parents))]
        children.append(crossover(parent1,parent2)) #Dùng hàm breed() ở trên
    return children

def mutation(children): 
    for i in range(len(children)):
        if random.random() > 0.5:
            continue
        else:
            mutated_position = int(random.random() * chromosome_length) #Vị trí xảy ra đột biến
            mutation = random.choice(move_list) #Chọn số bất kỳ để thay 
            children[i][mutated_position] = mutation
    return children
generation = 0
while True:
    fitness_scores = fitness(population)
    if min([i[1] for i in fitness_scores]) == 0:
        a = [i[0] for i in fitness_scores if i[1] == 0][0] 
        print("Discovered solution = {}".format(a))
        print(generation)
        break
    parents = select_parents(fitness_scores) #Chọn ra cặp bó mẹ có điểm cao nhất
    children = create_children(parents) #Tạo thế hệ con từ parents
    population = mutation(children) #Quần thể sau đột biến
    generation +=1