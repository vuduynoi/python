#bài 12 tính giờ phút giây
#1h=60p=3600s và chia lấy dư cho 24 vì quá 1 ngày chuyển sang ngày ms
#
t=int(input("Nhập vào số giây bất kì"))
hour=(t//3600)%24# cần phải chia cho 24 vì giờ quá 24 sẽ chuyển sang giờ ms
minute=(t%3600)//60#lấy số giây chia lấy dư cho 1 giờ<=>3600s dư ra số giây<3600
#sau đó chia lấy nguyên ch0 60 vì 1 phút = 60 giây (số phút )
second=(t%3600)%60#chia cho 3600 =>số giây <3600 và lấy số giây đó chia lấy
#dư cho 60s(1 phút) => số giây <60 (số giây )
print(hour,":",minute,":",second)
