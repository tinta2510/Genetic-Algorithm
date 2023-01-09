# Trình bày về cách sử dụng Genetic Algorithm để tìm parameter Population_size và Parents_number tối ưu nhất cho giải thuật tìm lời giải Reach the flag

### Mục lục:
[1. Khởi tạo quần thể (Create initial_population)](#1)   
[2. Đánh giá độ phù hợp (Evaluate fitness)](#2)  
[3. Chọn lọc (Selection)](#3)  
[4. Sinh sản (Crossover)](#4)   
[5. Tạo đột biến (Mutation)](#5)  


<a name = '1'></a>
## 1. Khởi tạo quần thể (Create initial_population): 
- Mỗi Choromosome là 1 list bao gồm population_size và parents_number cho Genetics Agorithm RTF.
- Ví dụ: ` [[200,50] , [100,75] , [150,30]] `. Đây là một population gồm 3 chromosome. Choromosome đầu tiên chứa 2 giá trị là 200 (*population_size*) và 50 (*parents_number*). 
```sh
#Initial_PARAMETER_population:
for i in range(para_pop_size): 
   pop_size = random.choice(np.arange(20,pop_size_max,10))
   parents_num = random.choice(np.arange(10,pop_size,10))
   lis = [pop_size,parents_num]
   para_pop.append(lis)
```
<a name = '2'></a>
## 2. Đánh giá độ phù hợp (Evaluate fitness): 
- Lần lượt cho các *Chromosome* vào GAs và chạy thử (mỗi *Chromosome* chạy 3 lần). 
- Sau khi GAs đã tìm ra lời giải ta ghi lại số **generation** trung bình GAs ứng với *chromosome* đó cần để tìm được lời giải.  

<a name = '3'></a>
## 3. Chọn lọc (Selection):  Sử dụng *Rank selection*
- Sắp xếp các *Chromosome* theo thứ tự *fitness_value* tăng dần (số ***generation*** giảm dần).
- Sau đó, chọn những *chromosome* có *fitness_value* cao nhất để thêm vào *parents_list*.

<a name = '4'></a>
## 4. Sinh sản (Crossover):
- Chọn bất kỳ *parent1* và *parent2* trong *parents_list*. Sau đó, chọn một tỉ lệ *rate* bất kỳ trong đoạn từ [0,1]. 
- Sau đó, tạo ra *chromosome con* với *population_size* và *parents_num* mới bằng cách cộng *population_size* và *parents_num* của *parent1* và *parent2* theo tỉ lệ *rate*.
- Ví dụ: 
```sh
rate = 0.6 #rate = random.random()
parent1 = [200,50] # [population_size,parents_num]
parent2 = [150,75]
new_pop_size = 200*0.6 + 150*0.4
new_parent_num = 50*0.4 + 75*0.6
child = [new_pop_size,new_parents_num]
```
- Code: 
```sh
def para_crossover(parent1,parent2):
    rate = random.random()
    child = []
    new_pop_num = round(parent1[0]*rate + parent2[0]*(1-rate),-1)
    new_parents_num = round(parent1[1]*rate + parent2[1]*(1-rate),-1)

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
```

<a name = '5'></a>
## 5. Gây đột biến (Mutation):
- Đối với mỗi *chromosome* trong tập *new_gen*, ta cho tỉ lệ xảy ra đột biến là 50%. 
- Nếu đột biến xảy ra, *population_size* và *parents_number* của *chromosome* sẽ được thêm hoặc bớt một giá trị ngẫu nhiên trong khoảng từ (0,50).  
```sh
def create_mutation(new_gen): 
    for i in new_gen: 
        if (random.random() > 0.5):
            i[0] += random.choice(np.arange(-50,50,10))
            i[1] += random.choice(np.arange(-50,50,10))
        else: continue
    return new_gen
```
