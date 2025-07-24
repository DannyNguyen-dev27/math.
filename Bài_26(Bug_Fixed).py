#Thư viện random
import random
#khai báo set
Thung_Phieu = set()
#vòng lặp
while(True):
    print("- - - - - MENU - - - - -")
    print("Vui lòng chọn chức năng (nhập số tương ứng với chức năng)")
    print("1: Thêm 1 số vào điện thoại vào thùng phiếu thưởng")
    print("2: Bỏ 1 số điện thoại ra khỏi thùng phiếu thưởng")
    print("3: Quay 1 số ngẫu nhiên lấy ra 1 số điện thoại trúng thưởng")
    print("4: Kết thúc chương trình")
    print("Thùng phiếu hiện tại:", Thung_Phieu)
#Lựa chọn chức năng
    Lua_chon = int(input("Lựa chọn: "))
    if (Lua_chon == 1): #Thêm 1 số điện thoại vào thùng phiếu
        SĐT = (input("Nhập vào số điện thoại dự thưởng: "))
        Thung_Phieu.add(SĐT)
        print("Thùng phiếu hiện tại:" , Thung_Phieu)
    elif (Lua_chon == 2): #Xóa 1 số điện thoại khỏi thùng phiếu
        SĐT = (input("Nhập số điện thoại dự thưởng cần xóa: "))
        Thung_Phieu.discard(SĐT)
    elif (Lua_chon == 3): #Quay ngẫu nhiên 1 số điện thoại trúng thưởng
        Hoa = random.randint(0,len(Thung_Phieu))
        print("Vị trí trúng thưởng là " + str(Hoa))

        H = 0
        for h in Thung_Phieu:
            if(H == Hoa):
                break
            H = H + 1

        print("Xin chúc mừng số điện thoại " + h + " đã trúng thưởng!")
        Thung_Phieu.discard(h)
    else:
        break
    
    HOA = (input("Nhập phím bất kỳ để tiếp tục: " )) #sau khi nhập số đt,hoặc các chức năng khác,vòng lặp sẽ lặp lại
    #nên thêm chỗ này vào để người dùng nhập phím cho vòng lặp lặp lại và chọn chức năng muốn dùng, giúp người dùng để bối rối
        
    

    
