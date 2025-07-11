#Python, bài 17, kiểu dữ liệu list
#tạo list rỗng
emptylist = []
#tạo ra 1 đối tượng list
list2 = list()
#tạo ra list có dữ liệu
weapons = ["Sword","Spear","Shield","Gun"]
print(weapons)
#list có thứ tự, thứ tự phần tử bắt đầu từ 0, từ trái sang phải
#vd: mình muốn xuất ra phần tử "Spear", mình sẽ làm như sau:
print(weapons[1])
#vì thứ tự bắt đầu bằng 0,nên số thứ tự của "Spear" là 1 chứ không phải 2.

#list[x:y], lấy ra từ x và dừng lại ở y
print(weapons[0:3])
#khi chạy, máy tính sẽ chỉ lấy ra từ "Sword" tới "Shield" vì "Gun" nằm ở vị số 3,máy tính sẽ chỉ lấy từ x tới số lớn nhất trước y
#thêm phần tử vào cuối list.
weapons.append("Hammer")
#thêm nhiều phần tử vào cuối list.
weapons[len(weapons):2] = ["Knife","Axe","Knife","Bomb","Bomb"]
#thêm phần tử vào thứ tự theo ý muốn, ví dụ mình muốn thêm "Bomb" vào vị trí số 3
weapons.insert(3,"Bomb")
print(weapons)
#xóa phần tử khỏi list
weapons.remove("Shield")
print(weapons)
#đếm số phần tử có trong list
print(len(weapons))
#đếm số lượng của phần tử thỏa điều kiện
print("Số dao: ", weapons.count("Knife"))
print("Số súng: ", weapons.count("Gun"))
print("Số Bom: ", weapons.count("Bomb"))
#kiếm tra phần tử có trong list hay không, dùng hàm in
for i in range(4):
    if "Bomb" in weapons:
        weapons.remove("Bomb")
        print(weapons)
    else:
        print("Không còn Bomb")
#xóa phần tử ra khỏi list bằng vị trí
weapons.pop(2)
print(weapons) #phần tử "Gun" bị xóa khỏi list vì nằm ở vị số 2
# đảo ngược list
weapons.reverse()
print(weapons)
#sắp xếp lại list, dùng hàm sort, với ký tự sắp xếp theo bảng alphabet, còn số từ nhỏ tới lớn
date_of_birth = [1710,2012,2705,2012]
weapons.sort()
date_of_birth.sort()
print(weapons)
print(date_of_birth)
#sắp xếp lại list, nhưng đảo ngược lại, ký tự theo bảng alphabet từ z-a, còn số từ lớn tới bé
weapons.sort(reverse=True)
date_of_birth.sort(reverse=True)
print(weapons)
print(date_of_birth)
#xóa hết dữ liệu trong list
weapons.clear()
date_of_birth.clear()
print(weapons)
print(date_of_birth)