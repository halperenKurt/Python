import tkinter as tk

window = tk.Tk()
window.title("BMI CALCULATOR")
window.geometry("400x250")

def calculation():
    boy = e1.get()
    kilo = e2.get()
    boy = float(boy)
    kilo = float(kilo)
    endeks = (kilo / boy ** 2) if boy != 0 else 0
    if endeks <= 18.4:
        sonuc2.config(text="UNDERWEİGHT" + "\n" + str(endeks), fg="black")
    elif 18.4 < endeks < 25:
        sonuc2.config(text="NORMAL" + "\n" + str(endeks), fg="black")
    elif 25 <= endeks < 30:

        sonuc2.config(text="OVERWEİGHT" + "\n" + str(endeks), fg="black")
    elif 30 <= endeks < 35:

        sonuc2.config(text="FAT.FİRST DEGREE!!" + "\n" + str(endeks), fg="black")
    elif 35 <= endeks < 45:

        sonuc2.config(text="FAT.SECOND DEGREE!!!!" + "\n" + str(endeks), fg="black")
    elif endeks >= 45:

        sonuc2.config(text="OBESITY" + "\n" + str(endeks), fg="black")

#HEİGHT BAR
boyVerisi = tk.Label(text="HEİGHT(m) =")
boyVerisi.place(x=77,y=15)
e1 = tk.Entry()
e1.place(x=160,y=15)

#WEİGHT BAR
kiloVerisi = tk.Label(text="WEİGHT(kg) =")
kiloVerisi.place(x=77,y=60)
e2=tk.Entry()
e2.place(x=160,y=60)

#RESULT BAR
sonuc = tk.Label(text="RESULT")
sonuc.place(x=20,y=120)
sonuc2 = tk.Label()
sonuc2.place(x=20,y=140)

#CALCULATİON BUTTON
hesaplamaTusu = tk.Button(text ="CALCULATE", command=calculation)
hesaplamaTusu.place(x=232,y=90)


btn3 = tk.Button(text="ÇIKIŞ",command=window.quit)
btn3.place(x=250,y=150)

window.mainloop()



