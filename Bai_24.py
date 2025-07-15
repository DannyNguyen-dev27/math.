#Python, Bài 24, Kiểu dữ liệu tuple
#Tuple là chuỗi các phần tử có thứ tự giống như list, nhưng giá trị trong tuple là các hằng số
#Tuple một khi được tạo ra thì không thể sửa đổi giá trị của nó
#phần tử của Tuple nằm trong dấu ngoặc đơn, các phần tử được ngăn cách bằng dấu phẩy
#phần tử trong tuple có thể trùng lặp
Basketball_Team = ("An","Dương","Hoa","Đạt","Dương","Hoa","Phát")
Score = (1,2,69,1710,2705)
#Các thao tác với Tuple

#ta có lấy dữ liệu trong tuple bằng cách xác định số thứ tự của phần tử đó
print(Basketball_Team[2])
print(Score[0:2])
#ta có thể duyệt các phần tử trong tuple bằng vòng lặp
for Hoa in Basketball_Team:
    print(Hoa)
#cộng hai tuple
Hoa = Basketball_Team + Score
print(Hoa)
#nhân hai tuple
hoa = Score * 2
print(hoa)
#kiểm tra 1 phần tử có nằm trong tuple hay không
print("Hoa" in Basketball_Team)
print("Phong" in Basketball_Team)
#Tìm min,max,và tính sum
#Min Max là để tìm phần tử có giá trị nhỏ và lớn nhất, với chuỗi ký tự xếp theo alphabet,nhỏ nhất từ A đến Z
print(min((Basketball_Team)))
#Với số là từ số bé đến số lớn
print(max(Score))
#hàm sum dùng để tính tổng, ta chỉ dùng được hàm sum với những con số(kiểu dữ liệu int,float)
print(sum(Score))