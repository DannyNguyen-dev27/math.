#Python, bài 19, vòng lặp lồng nhau
#đơn giản là bên trong 1 vòng lặp cũng có thể chứa nhiều vòng lặp khác
#làm bài tập bảng cửu chương để làm ví dụ
for j in range(2,10):
    print("Bảng cửu chương", j)
    for i in range(1,11):
        print("{0} * {1} = {2}".format(i,j,j * i))

