
text = input("Bir metin girin: ")

with open("datas.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Metin dosyaya yazıldı.")

with open("datas.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nDosyanın içeriği:")
print(content)


