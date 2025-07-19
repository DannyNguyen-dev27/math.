#Python bài 25,kiểu dữ liệu Set
#Set lưu trữ dữ liệu giống như list(sử dụng dấu ngoặc nhọn : {} ), nhưng giá trị phần tử trong Set không có thứ tự
#các giá trị trong set không được trùng lặp nếu, thì sẽ bị ghi đè lên
#giá trị trong set không thể thay đổi,nhưng có thể thêm và xóa

#tạo Set mới
Hoa = {"Cute", "Carrot", "Pretty"}
#Duyệt các phần tử trong set
for H in Hoa:
    print(H)
#thêm phần tử vào set
Hoa.add(1710) #thêm phần tử đơn lẻ
Hobby = ["Cooking, Playing Basketball","Sleeping","Talking"]
Hoa.update(Hobby) #thêm tập hợp phần tử của 1 list khác
print(Hoa)
#xóa phần tử 
Hoa.remove("Sleeping") #nếu phần tử không tồn tại sẽ báo lỗi
Hoa.discard("Talking") #nếu phần tử không tồn tại sẽ không báo lỗi
Hoa.pop() #xóa phần tử đầu tiên trong set
print(Hoa)
#xóa toàn bộ dữ liệu trong set(làm rỗng set)
Hoa.clear
print(Hoa)
#xóa tập hợp set (dùng từ khóa del)
del Hoa