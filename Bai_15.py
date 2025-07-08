#Python, bài 15, bài tập giải phương trình bậc 2
print("Giải phương trình ax^2 + bx + c = 0")
#nhập dữ liệu
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
#import thư viện
import math

if a != 0:
    delta = b ** 2 - 4 * a * c
    print("delta = ", delta)
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print("Có nghiệm kép, x1 = x2 =" , x)
    else:
        x1 = -b + math.sqrt(delta) / (2 * a)
        x2 = -b - math.sqrt(delta) / (2 * a)
    print("Có nghiệm kép x1 = {0} và x2 = {1}".format (x1,x2))
else:
    print("Không phải phương trình bậc 2")
