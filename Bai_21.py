#Python, bài 21, Vòng lặp While
#Vòng lặp while là 1 vòng lặp giúp ta thực hiện 1 đoạn code nhiều lần, ta dùng while thay vì for khi không biết trước số lần lặp lại
# ví dụ yêu cầu người dùng nhập mật mã
Hoa = 10
while Hoa == 10:
    Password =int(input("Nhập mật mã: "))
    if Password == 1710:
        Hoa -= 9
        print("Mật mã đúng")
    else:
        print("Sai mật mã")


#ta có thể dùng else với vòng lặp while để thực hiện 1 đoạn mã nào đó nếu điều kiện là false
answer = input("Phrêđêric Sôpanh sinh ngày mấy: ")
while answer == "Ngày 17 tháng 10":
    # ta có thể dùng hàm break để dừng vòng lặp
    print("Câu trả lời đúng") 
    break
else:
    print("Câu trả lời sai")