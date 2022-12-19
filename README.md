# Một số thay đổi để tăng tốc độ tìm lời giải 
## 1. Thay đổi cách Mutation:  
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
