#bài toán có liên quan đến sai số

d1=3.22-3.21  #kq=0.0100000000009
d2=2.11-2.10  #kq=0.009999999999787 chỉ sấp dỉ bằng nhau
print('d1=',d1)
print('d2=',d2)
dif=d1-d2
if dif<0:
    diff = -diff #chuyển về số dương để so sánh   
if dif<0.000001:
    print("bằng nhau")
else :
    print("Không bằng nhau")
