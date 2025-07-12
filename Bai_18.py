#Python, Bài 18, Vòng lặp For

#Vòng lặp For đi từ 0 bắt đầu từ đến <N, mỗi lần tăng 1 đơn vị
n = 10
for i in range(n):
    print(i)

#Ví dụ tính tổng từ 0 đến N
N = int(input("Nhập vào N: "))
tong = 0
for i in range(N + 1):
    tong += i
    if tong == N*(N+1) / 2:
        print("Tổng = " ,tong)

#Ví dụ mật khẩu
Password = int(input("Nhập mật khẩu: "))
tries = 3
for i in range(tries):
    if Password != 1710:
        print("Sai mật khẩu")
        Password = int(input("Nhập mật khẩu: "))
        tries -= 1
    if tries == 0:
        print("Sai mật khẩu quá nhiều.")


if Password == 1710:
    print("Pass")
#Vòng lặp for, có bước tăng tùy chỉnh
for i in range(0, 10, 2):
    print(i) #khi print i, từ 0 tới 10, mỗi 1 lần sẽ tăng lên 2 đơn vị hay vì 1 như bình thường
#Vòng lặp for, giảm dần
for i in range(0, 10, -1):
    print(i)
#Vòng lặp for duyệt các phần tử trong list 
colors = ["Pink, Orange, Blue"]
for color in colors:
    print(color)

for color in range(len(colors)):
    print(colors[color])

