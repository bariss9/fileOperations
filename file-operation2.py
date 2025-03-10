with open("datas.txt", "a", encoding="utf-8") as file:         #karakter bazlı hata almamak için utf-8 ile dosyaya yazdık
                                                               #append ile önceki verileri koruduk
    print("\n5 satır veri girin:")
    for i in range(5):
        row = input(f"{i+1}. satır: ")
        file.write(row + "\n")

print("5 satır dosyaya kaydedildi.")


with open("datas.txt", "r", encoding="utf-8") as file:         
    print("\nDosyanın güncel içeriği:")
    for row in file:
        print(row.strip())        #strip() foksiyonu ile gereksiz boşluk olmasına karşılık önlem aldım
