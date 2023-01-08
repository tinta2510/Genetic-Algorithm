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
- Ví dụ: [ [200,50] , [100,75] , [150,30] ]. Đây là một population gồm 3 chromosome. Choromosome đầu tiên chứa 2 giá trị là 200 (population_size) và 50 (parents_number). 
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
- Sắp xếp các Chromosome theo thứ tự *fitness_value* tăng dần (số ***generation*** giảm dần).
- Sau đó, chọn những chromosome có *fitness_value* cao nhất để thêm vào parents_list.

<a name = '4'></a>
## 4. Sinh sản (Crossover):
- Chọn bất kỳ 2 parents trong parents_list. Sau đó, chọn một số rate bất kỳ trong đoạn từ [0,1]. 
- 

```sh
def para_crossover(parent1,parent2):
    rate = random.random()
    child = []
    new_pop_num = round(int(parent1[0]*rate + parent2[0]*(1-rate)),-1)
    new_parent_num = round(int(parent2[1]*rate + parent1[1]*(1-rate)),-1)

    #While new_parent_num is too small or bigger than new_pop_num, recreate new_parent_num:
    while (new_parent_num<10) or (new_parent_num > new_pop_num*1.2): 
        new_parent_num = round(int(parent2[1]*rate + parent1[1]*(1-rate)),-1)

    child.append(new_pop_num)
    child.append(new_parent_num)
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
