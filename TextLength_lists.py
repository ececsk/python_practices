#text içerisinde yer alan kelimelerden uzunluğu altıdan büyük eşit olanları aynı bir listeye atalım.
text = "Sisterslab Women in tech Python akademimiz tüm hızıyla devam etmektedir"

words = text.split(" ")
print(words)

new_list = []
for i in words:
    if len(i) >= 6:
        new_list.append(i)

print(new_list)
