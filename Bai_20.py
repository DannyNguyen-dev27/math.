#Python, bài 20, tìm hiểu sâu hơn về Kiểu dữ liệu string 
#Cộng chuỗi
s1 = "Hi"
s2 = "Hoa"
s3 = s1 + " " + s2
print(s3)
#tạo chuỗi trên nhiều dòng
lines = '''
Em hứa làm bài tập đầy đủ
'''
print(lines)
#Lặp lại chuỗi
chep_phat = lines * 20
print(chep_phat)
#Kiếm tra chuỗi này có bên trong chuỗi kia
h1 = "Hi Hoa"
h2 = "Hoa"
h3 = "Dương"
#dùng hàm in
if h2 in h1:
    print("h2 là chuỗi con của h1")
else:
    print("h2 không phải chuỗi con của h1")

if h3 in h1:
    print("h3 là chuỗi con của h1")
else:
    print("h3 không phải chuỗi con của h1")

#viết hoa chữ đầu của chuỗi(hàm capitalize)
h4 = "hoa"
h4 = str.capitalize(h4)
print(h4)
#viết hoa toàn bộ chuỗi(hàm upper)
h4 = h4.upper()
print(h4)
#tìm và đếm số lượng của chuỗi con(dùng hàm find và count)
s = "Hôm nay là 1 ngày đẹp trời; 1 chú chim đang hót;1 bông hoa đang nở rộ"
print(s.find("1"))
print(s.find("tôi"))
#Trả về -1 nếu không tìm thấy, và ngược lại trả về vị trí của đầu tiên của chuỗi đó
print(s.count("1")) # dùng hàm count để kiểm tra có bao nhiêu chuỗi con ở bên trong.
print(s.count("2"))
#Thay thế chuỗi(hàm replace)
s = s.replace("Hôm nay", "Ngày mai")
s = s.replace("đang","sẽ")
print(s)
#phân tách chuỗi thành 1 list
list1 = s.split(";")
print(list1)

list2 = s.split(" ")
print(list2)
#Format
print("{0} + {1} = {2} ".format(751,959, 751 + 959))
#lấy chuỗi con
print(list2[12:14])