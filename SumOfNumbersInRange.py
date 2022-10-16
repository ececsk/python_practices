#Klavyeden girilen iki sayı arasındaki sayıları toplayan kodu yazınız
a=int(input("1. Sayıyı Giriniz:"))
b=int(input("2. Sayıyı Giriniz:"))
toplam=0 
if(a>b):
  baslangic_degeri=b
  bitis_degeri=a

else:
  baslangic_degeri=a
  bitis_degeri=b

for i in range(baslangic_degeri+1,bitis_degeri):
  toplam+=i
print("{} değeri ile {} değeri arasındaki sayıların toplamı {} dır".format(baslangic_degeri,bitis_degeri,toplam))
