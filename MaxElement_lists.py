#Liste içerisindeki en büyük elemanı bulma (max metodu kullanmadan)
my_list = [1,2,3,9,4,5,6,7,8,9,10,0]

temp = 0
for item in my_list:
    if item > temp:
        temp = item

print(temp)

#max metodu ile yapsaydık
#print(max(my_list))
