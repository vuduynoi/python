#bài 10 các loại lỗi trong python
#lỗi cú pháp
#y=2
#x=y+2
#y+2=x
#lỗi thực thi
#x=5
#y=0
#z=x/y
#print(z)
#lỗi nghiệp vụ
#t=10
#l=9
#h=7.5
#dtb=t+l+h/3 #không có dấu ngoặc
#print(dtb)
#dùng try except
try:
    x=5
    y=0
    z=x/y
    print(z)
    
except:
    print("Bị lỗi rồi")
    print("Cám ơn bạn đã dùng phần mềm")
