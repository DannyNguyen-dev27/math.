#Python, Bài 27, kiểu dữ liệu Dictionary
#Dictionary là tập hợp lưu trữ dữ liệu trong các cặp Key: value, được sắp xếp theo thứ tự
#Dictionary dùng cầm ngoặc nhọn {}
#Dictionary có thể thay đổi,thêm bớt dữ liệu, khác với tuple
#Dictionary không được có 2 value với cùng 1 khóa

#ví dụ 1
Hoa = {
    "Age": 13,
    "Gender": "Female",
    "Hobby": "Playing Basketball"
}
print(Hoa)

print(Hoa["Hobby"])
#sử dùng hàm get, get() để lấy giá trị
print(Hoa.get("Gender"))

#ta có thể thay đổi giá trị của 1 khóa bằng cách tham khảo tên khóa của nó
Hoa["Hobby"] = "Cooking"
#hoặc dùng hàm update()
Hoa.update({"Hobby": "Studying", "Name": "Hoa" })
print(Hoa)
#thêm các mục, ta có thể dùng thêm 1 mục(key) và gán giá trị(value) cho nó trực tiếp
Hoa["Date of Birth"] = 1710 #mục được thêm phải có tên khác, vì không thể có 2 giá trị có cùng một khóa
#hoặc dùng hàm update để thêm mục
Hoa["Hair Color"] = "Black"
print(Hoa)
#xóa các mục, ta dùng hàm pop() để xóa key được chỉ định
Hoa.pop("Name")
#hoặc dùng hàm popitem() để xóa mục xếp cuối cùng, ở các phiên bản python trước 3.7,popitem() sẽ xóa ngẫu nhiên 1 mục
Hoa.popitem()
#từ del dùng để xóa 1 mục chỉ định giống pop(), hoặc xóa hoặc toàn bộ từ điển
del Hoa["Date of Birth"]
print(Hoa)
#dùng clear() để làm trống từ điển
Hoa.clear()
print(Hoa)
#vòng lặp 
Hoa = {
    "Age" : 13,
    "Gender" : "Female",
    "Hobby" : "Cooking"
}
#In tên của tất cả mục trong từ điển, từng cái một
for c in Hoa:
    print(c)
print("tiếp theo:giá trị")
#duyệt cái giá trị trong từ điển:
for c in Hoa.values():
    print(c)
print("tiếp theo:khóa")
#duyệt cái khóa trong từ điển:
for c in Hoa.keys():
    print(c)
print("tiếp theo: khóa-giá trị")
#duyệt các khóa-giá trị trong từ điển:
for c,d in Hoa.items():
    print(c,d)