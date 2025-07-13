#Python, bài 22, Bài tập chuyển đổi số thập phân sang số nhị phân
#sử dụng hàm while
#Nhập vào n (n>0)
n = -1
while n == -1:
    n = int(input("Nhập vào n>0: "))

#chuyển đổi số thập phân sang nhị phân
Ket_qua = ""
while n>0:
    Ket_qua = str(n%2) + Ket_qua
    print("n%2 = ", n % 2)
    n = n // 2
    print("n//2 = ", n)

print("Kết quả", Ket_qua )