import turtle as ciz
#kalp çizimi
def cizim(kalp,kalem,arkaplan):
    ciz.bgcolor(arkaplan)
    ciz.pensize(2)

    def curve():
        for i in range(200):
            ciz.right(1)
            ciz.forward(1)

    ciz.speed(0)
    ciz.color(kalem,kalp)

    ciz.begin_fill()
    ciz.left(140)
    ciz.forward(111.65)
    curve()

    ciz.left(120)
    curve()
    ciz.forward(111.65)
    ciz.end_fill()
    ciz.hideturtle()
    ciz.done()
while True:
    secim = input("İstediğiniz renkte kalp çizdirmek için 1\n"
                  "Çıkış yapmak için q\n"
                  "Seçiminizi Yapınız = ")
    if secim.lower() == "q":
        break
    elif secim =='1':
        kalp = input("\nKalbin rengini seçin : ")
        kalem = input("Kalemin rengini seçin : ")
        arkaplan = input("Arka plan rengini seçin : ")

        try:
            cizim(kalp,kalem,arkaplan)
            print("\n----------\n")
        except:
            print("\ndüzgün bir renk kodu kombinasyonu girin\n")
    else:
        print("düzgün bir seçim yapın")