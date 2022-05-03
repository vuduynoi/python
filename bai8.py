#Nhập xuất dữ liệu
print("Mời bạn nhập giá trị")
s=int(input())
print("Bạn nhập:",s)
print(type(s))  #muốn đưa về số thì ép kiểu

name = input("Mời bạn nhập thêm giấ trị")
print("Bạn vừa nhập là:",name)
print(type(name))


def strtobool(s):       return s.lower() in ("true", "t","1","yes")#đưa chuỗi về in thường nếu 1 trong 4 chữ trên kể cả có chữ hoa thì trả về true

x=input("Mời bạn nhập True /false:")
x=strtobool(x) #Gán giá trị mình vừa nhập= hàm strtobool
print(x) #Xuất giá trị mình vừa nhập
#lưu ý:
"""Sử dụng hàm là: def strtobool(s):  //có thể là biến khác thay cho s
                    return s.lower() in ("yes","t","1","true")
                        nếu đúng khi in ra màn hình trả giá trị true
                        và trả giá trị false"""
