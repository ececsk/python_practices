def perfectNum(num1,num2):
  for sayi in range(num1,num2):
    total=0
    for i in range(1,sayi):
        if sayi%i==0:
            total+=i
        
    if total==sayi:
        print(sayi)


number1=int(input("Başlangıç değerini giriniz: ")) #Enter the initial value
number2=int(input("Bitiş değerini giriniz: ")) #Enter the end value

perfectNum(number1,number2)
