#Python, bài 13 ,toán tử điều kiện
x = int(input("Nhập số nguyên: ")) # nhập số nguyên cho biến x từ bàn phím
#dùng toán tử % để thực hiện phép chia lấy dư
print(x , "là số" , "chẵn" if x % 2 == 0 else "lẻ") # nếu phần dư của x chia hết cho 2 là 0,tức số đó là số chẵn và ngược lại nếu x là số lẻ.