print(("-" * 30) + "\nArea Calculator\n" + ("-" * 30))

print("\n1 - Kare\n2 - Dikdörtgen\n3 - Çember ")
seçim = input("Seçiminiz :")

if seçim == '1':
    kenarUzunluğu = int(input("Karenin Bir Kenar Uzunluğu :"))
    kareAlani = kenarUzunluğu ** 2
    print("Karenin Alanı = " + str(kareAlani))
elif seçim == '2':
    aKenarUzunluğu = int(input("Dikdörtgenin A Kenarı Uzunluğu :"))
    bKenarUzunluğu = int(input("Dikdörtegenin B Kenarı Uzunluğu :"))
    dikdörtgeninAlani = aKenarUzunluğu * bKenarUzunluğu
    print("Dikdörtgenin Alanı = " + str(dikdörtgeninAlani))
elif seçim == '3':
    çemberinYarıçapı = int(input("Çemberin Yarıçapı :"))
    piSayisi = 3
    çemberinAlani = piSayisi * çemberinYarıçapı**2
    print("Çemberin Alanı =" + str(çemberinAlani))
else:
    print("İŞLEM YAPILAMAZ!!!")