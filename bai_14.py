#Python, bài 14, câu lệnh rẽ nhánh if else
score = float(input("Nhập số điểm của học sinh: ")) 
#sử dụng toán tử điều kiện if - else
if score >= 9:
    print("Xếp loại học sinh: Xuất sắc")
#sử dụng câu lệnh rẽ nhánh elif cho nhiều xếp loại học sinh khác
elif score >= 8:
    print("Xếp loại học sinh: Giỏi")
elif score >= 6.5: # lúc khai báo biến score, ta dùng hàm input để chuyển đổi đầu vào từ kiểu dữ liệu string sang float vì có thể có số điểm là số thập phân(thuộc số thực)
    print("Xếp loại học sinh: Khá")
elif score >= 5:
    print("Xếp loại học sinh: Trung bình")
#sử dụng elif cho tới khi chỉ còn 1 điều kiện,khi này ta dùng else.
else:
    print("Xếp loại học sinh: Yếu")
