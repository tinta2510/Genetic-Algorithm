# Genetic-Algorithm
1. Mô tả trò chơi:
- Mục tiêu: đưa nhân vật từ vị trí ban đầu đến ô có cắm cờ.
- Cách chơi: sử dụng các nút mũi tên lên, xuống, sang trái, sang phải để di chuyển nhân vật giữa các ô khác nhau. Ô màu vàng sẽ rơi xuống khi bạn bước qua chúng, ô màu vàng nâu sẽ rơi xuống khi bạn bước qua chúng 2 lần, ô màu xám sẽ không rơi khi bạn bước qua. 

2. Mô phỏng game trên Python:
a. Mô phỏng bản đồ game:
- Sử dụng mảng 2 chiều để tạo hệ trục tọa độ, mỗi điểm trên trục tọa độ đánh các số, mỗi số tương ứng với một loại ô vuông trong game.
    + Số 1 tương ứng với ô vàng (đi qua được 1 lần)
    + Số 2 tương ứng với ô vàng nâu (đi qua được 2 lần)
    + Số 3 tương ứng với ô màu xám
    + Số 5 tương ứng với Flag
    + Số 0 là những vị trí không đi được
- Ví dụ: 
    #Mô phỏng Round 5:
    map5 = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[1,1,1,3,1],[0,0,0,1,0]]
    #vị trí ban đầu:
    a=0 
    b=4
b. Các bước di chuyển: 
- Các nút Up, Down, Right, Left lần lượt tương ứng y+=1; y-=1; x+=1;x-=1

3. Giải thuật di truyền để giải game Reach the flag:
a) Khởi tạo quẩn thể (Initial Population):
- Khởi tạo quần thể (population) gồm các NST (chromosome) ban đầu là tập các bước di chuyển (r,l,u,d) với độ dài (chromosome_length) và độ lớn quần thể (population_size) cho trước.
    population_size = 20
    chromosome_length = 20
    #Initial population
    population = []
    for i in range(population_size):
        chromosome = []
        for x in range(chromosome_length):
            chromosome.append(random.choice(move_list))
        population.append(chromosome)

b) Đánh giá độ phù hợp (Evaluate fitness): 
- Sau khi đã khởi tạo quần thể, cho các chromosome chạy thử trên map. Sau đó, đánh giá độ phù hợp bằng cách cộng tổng số điểm của các ô còn lại trên map (match) với khoảng cách (distance) từ con trỏ (a,b) tới vị trí đích (a0,b0). 
*Chú thích: 
    + Tổng số điểm của các ô còn lại trên map (match): match += 1 nếu ô còn lại là 1 (vàng)
                                                       match += 2 nếu ô còn lại là 2 (vàng nâu)
    + Khoảng cách: abs(a-a0) + abs(b-b0)
- Ví dụ:
def fitness(population):
    fitness_scores = []
    for chromosome in population:
        a = a1
        b = b1
        map = [[0,0,0,1,0],[0,0,0,5,1],[0,0,0,1,0],[0,0,0,1,0],[0,1,1,3,1],[0,0,0,1,0]] 
        result = []
        match = 0 #Số ô còn lại
        distance = 0 #Khoảng cách từ vị trí cuối đến vị trí đích       
        for i in chromosome: #Chạy thử các bước di chuyển trên bản đồ
        for y in range(len(map)):
            for x in map[y]:
                if x==1: match += 1
                if x==2: match += 2
        distance = abs(a0-a) + abs(b0-b)
        result = [chromosome,match*2+distance]
        fitness_scores.append(result)
    return fitness_scores    

c) Sinh sản (Crossover):                                                   