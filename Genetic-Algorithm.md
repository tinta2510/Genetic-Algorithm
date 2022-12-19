# Genetic Algorithm  - Giải thuật di truyền  
## 1. Genetic Algorithm - Giải thuật di truyền là gì?  
- GA là phương pháp tìm kiếm tối ưu ngẫu nhiên được phát triển dựa trên quá trình tiến hóa của các quần thể sinh vật theo học thuyết Darwin ("Survival of the fittest”).
- Khác biệt quan trọng giữa Giải thuật di truyền và các phương pháp tìm kiếm ngẫu nhiên khác là GA duy trì và xử lý một tập các lời giải (**Nhiễm sắc thể - Chromosome**), gọi là một **Quần thể (Population**).   
- Sau các thế hệ được **Chọn lọc (Selection)**, **lai tạo (Crossover)** và **Đột biến ngẫu nhiên (Mutation)**, những *cá thể (individuals)* thích ứng tốt sẽ được giữ lại và làm nguyên liệu  cho các thế hệ sinh sản kế tiếp, ngược lại những cá thể kém thích nghi sẽ bị đào thải.

## 2. Các thành phần của Genetic Algorithm: 
Pseudocode Code:

**START**  
*Generate the initial population;*  
**REPEAT**    
*Evaluate fitness;*  
*Selection;*  
*Crossover;*    
*Mutation;*  
**UNTIL** *population has converged;*  
**END.**  
### a. Generate the initial population - Khởi tạo quần thể: 
- Quần thể (Population) là tập các lời giải, các giả thuyết ban đầu (Nhiễm sắc thể - Chromosome) cho vấn đề cần giải quyết.   
- Mỗi NST (Chromosome) là một chuỗi các gen nhằm thể hiện một đặc tính của NST.  
- Quần thể ban đầu trong GA thường được khởi tạo một cách ngẫu nhiên.  
### b. Evaluate fitness - Đánh giá độ phù hợp: 
- Là quá trình đánh giá độ phù hợp (độ thích nghi) của từng NST với đáp án cần tìm.  
- Việc đánh giá độ phù hợp (**fitness**) của mỗi NST trong quần thể diễn ra lặp lại sau mỗi thế hệ chính vì vậy tốc độ và kết quả của của hàm fitness evaluation ảnh hưởng lớn tới tốc độ của Genetic Algorithm. 
### c. Selection - Chọn lọc: 
- Đây là quá trình chọn ra những NST có độ phù hợp  cao để lai tạo cho thế hệ kế tiếp cũng như loại bỏ những NST có độ phù hợp thấp ra khỏi quần thể. 
- Các cách Chọn lọc - Selection: 
  + *Chọn lọc xếp hạng (rank selection)*: Sắp xếp các NST theo thứ tự mức độ thích nghi giảm dần. Loại bỏ các nhiễm sắc thể ở cuối dãy. Giữ lại n cá thể tốt nhấ t. 
  + *Chọn lọc tỉ lệ (Roulette wheel selection)*: những cá thể có độ phù hợp càng cao sẽ có xác suất được chọn làm bố mẹ càng cao. 
### d. Lai tạo - Crossover: 
- Là quá trình tạo 1 hay nhiều nhiễm sắc thể mới từ 2 NST bố - mẹ trở lên bằng cách kết hợp những đoạn gene từ NST bố - mẹ. 
- Các cách lai tạo: 
  + Single - point crossover
  + Multi - point crossover
  + Uniform crossover 
### e. Tạo đột biến - Mutation: 
- Là quá trình chọn ngẫu nhiên một hay một vài gene trên NST để thay thế bằng gene khác, tạo ra thế hệ con có một vài điểm khác so với NST bố - mẹ, giúp duy trì và làm tăng thêm độ đa dạng của quần thể. 
- Các cách tạo đột biến: 
  + Random resetting
  + Swap mutation
  + Scramble mutation
  + Inversion mutation
  



