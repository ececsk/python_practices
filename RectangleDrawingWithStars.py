#1

rowCount=int(input("Satır ve sütun sayısını giriniz: "))

for rowIndex in range(rowCount+1):
  if rowIndex==0 or rowIndex==rowCount: #başında mıyım sonunda mıyım bunu kontrol ediyorum yani baştaysam veya sondaysam hepsini yıldız bas
    print(rowCount*"*")
  else:
    print("*"+(rowCount-2)*" "+"*")
    
#2

for rowIndex in range(rowCount):
  for columnIndex in range(rowCount):
    if (rowIndex == 0 or rowIndex == rowCount -1 or columnIndex == 0 or columnIndex == rowCount -1 or rowIndex == columnIndex or columnIndex == (rowCount - rowIndex - 1)):
      print("*",end="")
    else:
      print(" ",end="")
  print()
