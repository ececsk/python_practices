#Bir sayının asal olup olmadığını veren bir fonksiyon yazalım
def isPrime(number):
  result=True
  for i in range(2,number):
    if number%i==0:
      result=False
      break
  return result

print(isPrime(15))
print(isPrime(17))
