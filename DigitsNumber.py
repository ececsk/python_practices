#Bir sayının kaç basamaklı olduğunu hesaplayalım
x=59725
count=0
temp=x

while x !=0:
  count+=1
  x//=10

print(f"{temp} sayısı {count} basamaklıdır." )
