'''
Python bài 16
nhập 3 điểm trên hệ trục tọa độ Oxy
1.xác định 3 điểm có tạo thành 1 tam giác hay không
2.nếu tạo thành 1 tam giác:
2a. tính chu vi tam giác
2b. tính diện tích tam giác
'''
#import thư viện
import math
xA = float(input("Nhập vào xA:"))
yA = float(input("Nhập vào yA:"))
xB = float(input("Nhập vào xB:"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
yB = float(input("Nhập vào yB:"))
xC = float(input("Nhập vào xC:"))
yC = float(input("Nhập vào yC:"))
#tính chiều dài 3 cạnh tam giác
ab = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)
ac = math.sqrt((xC - xA) ** 2 + (yC - yA) ** 2)
bc = math.sqrt((xC - xA) ** 2 + (yC - yA) ** 2)
# xác định 3 điểm có tạo thành 1 tam giác
if (ab + ac > bc) and (bc + ab > ac) and (ac + bc > ab):
    #tính chu vi
    chu_vi = ab + ac + bc
    print("chu vi hình tam giác là ",chu_vi)
    #tính diện tích
    p = chu_vi / 2
    S = math.sqrt(p*(p-ab)*(p-bc)*(p-ac))
    print("diện tích hình tam giác là ", S)
else:
    print("Không phải là hình tam giác")
