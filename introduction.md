<!-- TITLE 1 --> <h2>1 Giới thiệu</h2>
<!-- TITLE 2 >-----  --> <h3>Quá trình huấn luyện thường bao gồm:</h3>
- Khởi tạo mô hình một cách ngẫu nhiên
- Thu thập dữ liệu đã dược gán nhãn (vd: đoạn âm thanh kèm nhãn dán {có, không})
- Thay đổi các núm vặn (tối ưu hóa các tham số) để mô hình dự đoán chính xác hơn trên các mẫu
- Lặp lại cho tới khi có một mô hình hoạt động tốt

<!-- TITLE 2 >-----  --> <h3>Các thành phần cốt lõi:</h3>
- Dữ liệu
- Mô hình
- Hàm mục tiêu
- Các thuật toán tối ưu

<!-- TITLE 1 --> <h2>2 Các dạng học máy</h2>
<!-- TITLE 2 >-----  --> <h3>2.1 Supervised Learning</h3>
- Dự đoán <b>mục tiêu</b> với <b>đầu vào</b> cho trước
- <b>Nhãn (label)</b>: mục tiêu cần dự đoán
- <b>Đặc trưng (feature)</b>: dữ liệu đầu vào
- <b>Mẫu</b>: cặp (feature, label)
- (xi, yi): một mẫu cụ thể
> Mục đích: xây dựng mô hình f sao cho f(xi) -> yi
- Quá trình học:
    - Lấy một tập mẫu lớn với các features đã biết. Chọn ra tập con ngẫu nhiên, thu thập label gốc => <b>Train dataset</b>
    - Đưa train dataset vào thuật toán học có giám sát (hàm số đầu vào là tập dữ liệu và đầu ra là hàm số khác thể hiện mô hình đã học được)
    - Cuối cùng, đưa dữ liệu chưa nhìn thấy vào mô hình đã học được để dự đoán các label tương ứng
    <img src="/images/hoc-co-giam-sat.png" alt="image" width="500"/>
- Các dạng của học có giám sát:
    - Hồi quy (Regression)
        - Hàm mất mát: L1 loss function, L2 loss function
    - Phân loại (Classification)
        - Hàm mất mát: Entropy chéo (cross-entropy)
    - ...

> Bài toán trả lời cho câu hỏi "bao nhiêu, bao lâu, bao xa, ...?" là <b>Hồi quy</b>
> Bài toán trả lời cho câu hỏi "đây có phải là ...?" thì khả năng cao là <b>Phân loại</b>

<!-- TITLE 2 >-----  --> <h3>2.2 Unsupervised Learning</h3>
<!-- TITLE 2 >-----  --> <h3>2.3 Học tăng cường (Reinforcement learning)</h3>
...
<a href="https://d2l.aivivn.com/">Reference</a>

