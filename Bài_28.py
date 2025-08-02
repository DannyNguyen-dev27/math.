'''
Bài tập:
xây dựng 1 từ điển có các chức năng như sau(người dùng nhập chức năng muốn dùng qua menu)
1.Thêm 1 từ vừng mới(kèm nghĩa của từ đó)
2.tra cứu nghĩa của 1 từ vựng
3.cập nhật ý nghĩa của 1 từ vựng
4.cho phép người dùng xóa đi từ vựng trong từ điển
5.cho phép người dùng xóa toàn bộ từ vựng
6.cho phép người dùng in ra toàn bộ từ vựng
7.cho phép người dùng in ra từ điển theo cấu trúc: "TỪ VỰNG"
8.kết thúc chương trình
'''
#bài giải
tudien = {} #khai báo từ điển

while(True):
    print("Vui lòng lựa chọn chức năng(số): ")
    print('''
    1.Thêm 1 từ vừng mới(kèm nghĩa của từ đó)\n  
    2.tra cứu nghĩa của 1 từ vựng\n
    3.cập nhật ý nghĩa của 1 từ vựng\n
    4.cho phép người dùng xóa đi từ vựng trong từ điển\n
    5.cho phép người dùng xóa toàn bộ từ vựng\n
    6.cho phép người dùng in ra toàn bộ từ vựng\n
    7.cho phép người dùng in ra từ điển theo cấu trúc: "TỪ VỰNG" : "Ý NGHĨA"\n
    8.kết thúc chương trình
    ''',"từ điển" ,tudien)
    luachon = int(input("Nhập lựa chọn: "))

    if (luachon == 1):
        new_word = input("Nhập từ vựng mới: ")
        meaning = input("Nhập nghĩa của từ vựng mới: ")
        tudien[new_word] = meaning
        print("đã thêm từ vựng", new_word, "với ý nghĩa:", meaning )
        print("Từ điển hiện tại:", tudien)
    elif (luachon == 2):
        new_word = input("Nhập vào từ vựng muốn tra nghĩa: ")
        print("Ý nghĩa:", tudien[new_word])
    elif (luachon == 3):
        new_word = input("Nhập từ vựng: ")
        meaning = input("Nhập nghĩa của từ vựng: ")
        tudien[new_word] = meaning
    elif (luachon == 4):
        new_word = input("Nhập từ vựng cần xóa: ")
        tudien.pop(new_word)
        print("đã xóa từ vựng yêu cầu.")
    elif (luachon == 5):
        tudien.clear()
        print("Đã xóa tất cả từ vựng và ý nghĩa.")
    elif (luachon == 6):
        print("tất cả từ vựng có trong từ điển:")
        for h in tudien.keys():
            print(h)
    elif (luachon == 7):
        print("tất cả từ vựng kèm ý nghĩa có trong từ điển:")
        for h,d in tudien.items():
            print(h,":",d)
    elif (luachon == 8):
        break
    else:
        print("Nhập lựa chọn không đúng")

    tieptuc = input("Nhập phím bất kỳ để tiếp tục: " )