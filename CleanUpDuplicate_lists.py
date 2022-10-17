#Duplicate verileri temizleyerek yeni bir liste oluşturalım
my_list = [10, 10, 20, 30, 10, 20, 40, 50]
uniqe_list = []

for item in my_list:
    if item not in uniqe_list:
        uniqe_list.append(item)

print(uniqe_list)
