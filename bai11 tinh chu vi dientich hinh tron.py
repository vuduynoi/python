#bài 11 tính chu vi diện tích
import math
try:
    r=float(input("Mời bạn nhập bán kính hình tròn = "))
    cv=round(2*math.pi*r,2)#có thể dùng hàm round
    dt=r*r*math.pi
    print("chu vi =",cv)
    print("Diện tích =",dt)
except:
    print("Bạn nhập sai rồi")#khi chúng ta nhập bán kính là :3,5 thì báo lỗi

