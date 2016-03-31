from Veri_Cekme import *
from tkinter import *
#sudo apt-get install python3-tk


def buton_basildi():
    label_ad = Label(frame2, text = "ad = " + entry_ad.get())
    label_soyad = Label(frame2, text = "soyad = " + entry_soyad.get())
    label_ad.grid(row = 1, column = 1)
    label_soyad.grid(row = 2, column = 1)
    kisi = Veri_Cekme(entry_ad.get() , entry_soyad.get())   #"Ecir Uğur" , "Küçüksille"
    sayfa = kisi.schoolar_url_getir()
    label = Label(frame3, text = sayfa)
    label.grid(row = 1, column = 1)

pencere = Tk()
pencere.title("Google Schoolar")

frame1 = Frame(pencere)
frame2 = Frame(pencere)
frame3 = Frame(pencere)
frame1.pack()
frame2.pack()
frame3.pack()

entry_ad = Entry(frame1)
entry_soyad = Entry(frame1)

buton = Button(frame1, text = "Veriyi Getir", command = buton_basildi)

entry_ad.grid(row = 1, column = 1)
entry_soyad.grid(row = 2, column = 1)
buton.grid(row = 3, column = 1)

pencere.mainloop()


