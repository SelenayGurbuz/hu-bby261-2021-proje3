from tkinter import *
from PIL import ImageTk, Image

pencere = Tk()
pencere.title("Resimlerim")
pencere.geometry("1000x720")
pencere.iconbitmap("ico/car.ico.ico")
pencere.configure(bg="white")

baslik = Label(pencere, text="Araba Fotoğrafları",fg="red", bg="white")
baslik.grid(row=0, column=0, padx= 10, pady=10)
baslik.config(font=("Arial", 30))

image_names = ["images/araba1.png", "images/araba2.png", "images/araba3.png", "images/araba4.png"]

araba1 = Label(pencere, text="Kırmızı Araba")
araba1.grid(row=5, column=0)
araba1.config(font=("Arial", 30))

kapak = 0

def goster():
    gorsel = ImageTk.PhotoImage(Image.open(image_names[kapak]))
    cerceve = Label(image=gorsel)
    cerceve.image = gorsel
    cerceve.grid(row=1, column=0, padx= 10, pady=10)

goster()

def sonraki():
    global kapak
    if kapak < len(image_names)-1:
        kapak +=1
    else:
        kapak = 0
    print(kapak)
    goster()

def onceki():
    global kapak
    if kapak < len(image_names)+1:
        kapak -=1
    else:
        kapak = 0
    print(kapak)
    goster()

    Button(text="Sonraki Foto", command=onceki)
    buton.grid(row=0, column=10, padx=10, pady=10)
    buton.config(font=("Arial", 20))

    Button(text="Önceki Foto", command=sonraki)
    buton.grid(row=0, column=20, padx=10, pady=10)
    buton.config(font=("Arial", 20))

geri = Button(pencere, text="Geri", command=onceki, fg="white", bg="grey")
geri.config(font=("Arial", 15))
geri.grid()

ileri= Button(pencere, text= "İleri", command=sonraki, fg="white", bg="black")
ileri.config(font=("Arial", 15))
ileri.grid()

cikis = Button(pencere, text="Çıkış", command=pencere.quit, fg="white", bg="red")
cikis.config(font=("Arial", 15))
cikis.grid(column=0, row=20)
cikis.grid()

pencere.mainloop()