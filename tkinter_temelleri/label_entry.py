import tkinter as tk
from tkinter import Label, Entry

# label: metin yazar
# entry : tek satır metin giriş alanı

# önce ana sayfa yaratılmalı

window = tk.Tk()
window.title('tkinter temelleri -Label-Entry') # buton adı
window.geometry('600x400')

# Label, Entry widget yatarma:
lblad = Label(master=window,text='Adı')
lblsoyad = Label(master=window,text='Soyadı')

# Entry widget yaratma:
entad = Entry(window)
entsoyad = Entry(window)


# yerleştir:
lblad.grid(row=0)
lblsoyad.grid(row=1)
entad.grid(row=0,column=1)
entsoyad.grid(row=1,column=1)


window.mainloop() # kapatma