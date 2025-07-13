#Python, bài 23, câu lệnh break và continue trong vòng lặp
# câu lệnh break sử dụng để kết thúc vòng lặp chứa nó
# ví dụ
for Hoa in range(0, 10):
    print(Hoa)
    if Hoa > 5:
        break #lẽ ra phải in tới 9, nhưng vì Hoa > 5 (tức là in tới số 6), và dưới đó là câu lệnh break, nên vòng lặp kết thúc
#câu lệnh break trong vòng lặp for và while đều có khả năng dừng vòng lặp và cách sử dụng giống nhau

#câu lệnh continue dùng để bỏ qua phần còn lại của vòng lặp hiện tại,vòng lặp vẫn không kết thúc lặp lại đoạn code phía trên
for Hoa in range(0, 10):
    if Hoa % 2 == 1:
        continue
    print(Hoa)
    #vì 1,3,5 khi chưa cho 2 thì phần dư bằng 1, nên khi print hoa có lệnh continue ở trên, nên máy tính sẽ chỉ xuất ra số chẵn