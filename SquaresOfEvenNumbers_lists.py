#Verilen listedeki çift sayıların karelerinden yeni bir liste oluşturalım.

my_list = [1,2,3,4,5,6,7,8,9,10,0]

new_list = []
for item in my_list:
    if item % 2 == 0:
        new_list.append(item**2)

print(new_list)
