# Trình bày về game Reach the flag và cách giải game bằng Genetics Algorithm
### Mục lục: 
[1. Mô tả trò chơi](#1)  

[2. Mô phỏng game trên Python](#2)  

[3. Áp dụng Genetic Algorithm để giải game Reach the flag](#3)  
[a. Khởi tạo quẩn thể (Creating Initial Population)](#3a)  
[b. Đánh giá độ phù hợp (Evaluate fitness)](#3b)  
[c. Chọn lọc (Selection)](#3c)  
[d. Lai tạo (Crossover)](#3d)  
[e. Đột biến (Mutation)](#3e)  
[f. Vòng lặp giải thuật di truyền](#3f)

[4. Một số thay đổi để tăng tốc giải thuật](#4)  
[a. Thay đổi cách Mutation](#4a)  
[b. Cập nhật fitness_function](#4b)  

<a name = "1"></a>
## 1. Mô tả trò chơi:
- Mục tiêu: đưa nhân vật từ vị trí ban đầu đến ô có cắm cờ.
- Cách chơi: sử dụng các nút mũi tên lên, xuống, sang trái, sang phải để di chuyển nhân vật giữa các ô khác nhau. Ô màu vàng sẽ rơi xuống khi bạn bước qua chúng, ô màu vàng nâu sẽ rơi xuống khi bạn bước qua chúng 2 lần, ô màu xám sẽ không rơi khi bạn bước qua. 

<a name = "2"></a>
## 2. Mô phỏng game trên Python:
### a. Mô phỏng bản đồ game:
- Sử dụng mảng 2 chiều để tạo hệ trục tọa độ, mỗi điểm trên mặt phẳng tọa độ đánh các số, mỗi số tương ứng với một loại ô vuông trong game.
    + Số 1 tương ứng với ô vàng (đi qua được 1 lần).
    + Số 2 tương ứng với ô vàng nâu (đi qua được 2 lần).
    + Số 3 tương ứng với ô màu xám (đi qua được vô số lần).
    + Số 5 tương ứng với Flag.
    + Số 0 là những vị trí không đi được.
- Code:  
```sh
#Round 5:
map5 = [[0,0,0,1,0],
        [0,0,0,5,1],
        [0,0,0,1,0],    
        [0,0,0,1,0],
        [1,1,1,3,1],
        [0,0,0,1,0]]
#Initial position:
a=0 
b=4
```
### b. Các bước di chuyển: 
- Các nút Up, Down, Right, Left lần lượt tương ứng y+=1; y-=1; x+=1;x-=1
```sh
#Giả sử cho Chromosome:
chromosome = ['r', 'd', 'r', 'd', 'r', 'u', 'd', 'r', 'l', 'd', 'd', 'd', 'd', 'u', 'r', 'r']
```
```sh
for i in chromosome: 
    if i == 'u': 
        b+= 1 
        #Nếu ô mà con trỏ bước lên nằm ngoài khu vực bản đồ, con trỏ sẽ lùi lại vị trí trước.
        if (b > len(map)-1): 
            b-= 1 
            continue
        #Nếu ô mà con trỏ trỏ lên là ô số 0, con trỏ sẽ trở lại vị trí trước đó
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
```
<a name = "3"></a>
## 3. Áp dụng Genetic Algorithm để giải game Reach the flag:
<a name = "3a"></a>
### a. Khởi tạo quẩn thể (Creating Initial Population):
- Khởi tạo quần thể (population) gồm các NST (chromosome) ban đầu là tập các bước di chuyển (r,l,u,d) với độ dài (chromosome_length) và độ lớn quần thể (population_size) cho trước.
```sh
population_size = 20
chromosome_length = 20
#Initial population
population = []
for i in range(population_size):
    chromosome = [] 
    for x in range(chromosome_length):
        chromosome.append(random.choice(move_list))
        population.append(chromosome)
#Kết quả thu được: 
#chromosome1 = ['d', 'l', 'u', 'u', 'l', 'l', 'l', 'l', 'r', 'l', 'd', 'r', 'u', 'd', 'u', 'd', 'u', 'd', 'r', 'r'] 
```
<a name = "3b"></b>
### b) Đánh giá độ phù hợp (Evaluate fitness): 
- Sau khi đã khởi tạo quần thể, cho các chromosome chạy thử trên map. Sau đó, đánh giá độ phù hợp bằng cách cộng tổng số điểm của các ô còn lại trên map (match) với khoảng cách (distance) từ con trỏ (a,b) tới vị trí đích (a0,b0). Điểm số càng cao thì fitness càng thấp.
*Chú thích: 
    + Tổng số điểm của các ô còn lại trên map (match): match += 1 nếu ô còn lại là 1 (vàng)
                                                       match += 2 nếu ô còn lại là 2 (vàng nâu)
    + Khoảng cách: abs(a-a0) + abs(b-b0)
- Ví dụ:
```sh
def fitness(population):
    fitness_scores = []
    for chromosome in population:
        a = a1
        b = b1
        map = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[0,1,1,3,1],[0,0,0,1,0]] 
        result = []
        match = 0 #Số ô còn lại
        distance = 0 #Distance between the last position of player and flag
        for i in chromosome: #Run the chromosome on map
        # Check the number of block left on the map
        for y in range(len(map)):
            for x in map[y]:
                if x==1: match += 1
                if x==2: match += 2
        distance = abs(a0-a) + abs(b0-b)
        result = [chromosome,match*2+distance]
        fitness_scores.append(result)
return fitness_scores    
```
<a name = "3c"></a>
### c) Chọn lọc (Selection):  
* Sử dụng toán tử chọn lọc xếp hạng: Chọn những chromosome có độ phù hợp cao nhất (result có điểm thấp nhất) để làm bố mẹ. Số chromosome bố-mẹ tùy thuộc vào hyperparameter parents_number.
```sh
def select_parents(fitness_scores):
    parents_list = []
    for chromosome in sorted(fitness_scores,key = lambda x: x[1])[:parents_number]:
        parents_list.append(chromosome[0])
    return(parents_list)
```
* Bên cạnh đó, chúng ta truyền nguyên những chromosome có fitness cao nhất cho thế hệ tiếp theo (retain elite). 
<a name = "3d"></a>
### d) Lai tạo (Crossover): 
* Kết hợp 2 chromosome: (ở đây ta sẽ sử dụng Multi-point Crossover) 
    - Chọn ngẫu nhiên 2 NST bố mẹ trong tập. 
    - Chọn 2 vị trí geneA, geneB ngẫu nhiên trên NST
    - Từ vị trí 1 đến vị trí geneA và từ vị trí geneB đến vị trí cuối, ta lấy những gene từ parent1.
    - Từ vị trí geneA đến geneB trên NST ta dùng những gene từ parent2.
    - Code:
 ```sh
def crossover(parent1,parent2):
    child = []

    geneA = random.randint(0,chromosome_length-1)
    geneB = random.randint(0,chromosome_length-1)
    #Start and end position of Crossover
    startGene = min(geneA, geneB) 
    endGene = max(geneA, geneB)

    for i in range(0,chromosome_length):
        if (i < startGene) or (i > endGene):
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child
```
```sh
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
```
<a name = "3e"></a>
### e) Tạo đột biến (Mutation): 
- Sau khi tạo ra thế hệ con, ta đến thành phần tiếp theo của giải thuật di truyền là tạo đột biến. Sau đó, ta tiếp tục quay lại từ bước đánh giá độ phù hợp của quần thể vừa tạo thành. 
- Cách tạo đột biến: 
    + Chọn một tỷ lệ xảy ra đột biến (trong ví dụ dưới đây là 0.3), sử dụng hàm random.random() để chọn một số thập phân x trong khoảng (0,1)
    + Nếu x>0.3, ta bỏ qua.
    + Nếu x<0.3, ta chọn một vị trí ngẫu nhiên trên choromosome sau đó thay vị trí gene đó bằng một gene khác 
- Ví dụ: 
```sh
mutation_rate = 0.3
def mutation(children): 
    for i in range(len(children)):
        if random.random() > 0.3:
            continue
        else: 
            mutated_position = int(random.random() * chromosome_length) #Mutation position
            mutation = random.choice(move_list) #Replace
            children[i][mutated_position] = mutation
return children
```
<a name = "3f"></a>
### f) Vòng lặp Giải thuật Di truyền: 
- Sau khi đã khởi tạo các hàm thành phần của Giải thuật Di truyền, ta đưa các hàm vào vòng lặp và chạy cho đến khi chương trình tìm được kết quả.
```sh
generation = 0
t0 = time.time()
while True:
    fitness_scores = fitness(population) #Evaluate fitness
    if min([i[1] for i in fitness_scores]) == 0:
        solution = [i[0] for i in fitness_scores if i[1] == 0][0] 
        print("Discovered solution for round {} = {}".format(round,solution))
        print("In {} generations and {} seconds".format(generation,time.time() - t0))
        break
    parents = select_parents(fitness_scores) #Selection
    children = create_children(parents) #Crossover
    population = mutation(children) #Mutation
    generation += 1
```
<a name = "4"></a>
## 4. Một số thay đổi để tăng tốc độ tìm lời giải:
<a name = "4a"></a>
### a. Thay đổi cách Mutation: 
- Sử dụng kết hợp Swap mutation và random resetting thay vì chỉ random resetting như trước.
+ Cách mutation mới: 
```sh
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
```
+ Cách mutation cũ: 
```sh
def mutation(children): 
    for i in range(len(children)):
        if random.random() > mutation_rate: 
            continue
        else:
            mutated_position = int(random.random() * chromosome_length) #Mutated position
            mutation = random.choice(move_list) 
            children[i][mutated_position] = mutation
    return children
```
- Lý do em đổi: (dựa trên kết quả chạy thử 2 cách với map 12; population_size = 40,parent_number = 25)
  + Với cách cũ: để tìm ra kết quả chương trình mất TB **34.000 generations, 78 giây**. Em nhận thấy với cách mutation cũ, population nhanh chóng đạt fitness value có giá trị cao (2-4). Tuy nhiên, khi đạt giá trị fitness_value từ 2-4, population **mất đi độ đa dạng**, parents được chọn ra có cùng fitness_value dao động quanh số 2 --> chương trình **mắc kẹt** ở fitness_value = 2 và chạy rất lâu đề tìm kết quả.
=> Cách mutation này chưa làm tốt việc duy trì độ đa dạng cho quần thể.
  + Với cách mới: để tìm ra kết quả chương trình mất TB **10.000 generations, 21,37 giây**. Fitness value của các chromosome trong population có độ phân tán khá cao -> độ đa dạng lớn.
<a name = "4b"></a>
### b. Cập nhật fitness_function: 
- Fitness_value sẽ được cộng thêm điểm void (những gene không di chuyển được), tức là một chromosome có càng nhiều gene không di chuyển được (gene thừa) thì fitness value càng thấp. 
```sh
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
                if map[b][a] == 0: 
                    b -= 1
                    void += void_mark
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            if i == 'd': 
                b -= 1
                if (b<0):
                    b += 1
                    void += void_mark 
                    continue
                if map[b][a] == 0: 
                    b += 1
                    void += void_mark
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            if i == 'r': 
                a += 1
                if (a > len(map[0])-1): 
                    a -= 1 
                    void += void_mark
                    continue
                if map[b][a] == 0: 
                    a -= 1
                    void += void_mark
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1
            if i == 'l':  
                a -= 1
                if (a<0): 
                    a += 1 
                    void += void_mark
                    continue
                if map[b][a] == 0: 
                    a += 1
                    void += void_mark
                    continue
                if map[b][a] == 1: map[b][a] -= 1
                if map[b][a] == 2: map[b][a] -= 1  
        for y in range(len(map)):
            for x in map[y]:
                if x==1: match += 1
                if x==2: match += 2
        distance = abs(a0-a) + abs(b0-b)
        if (match+distance) == 0: result = [chromosome,match+distance]
        else: result = [chromosome,match+distance+void]
        fitness_scores.append(result)
    return fitness_scores
```
