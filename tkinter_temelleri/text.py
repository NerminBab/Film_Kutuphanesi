import tkinter as tk
from tkinter import Text


# önce ana sayfa yaratılmalı

window = tk.Tk()
window.title('tkinter temelleri -Text') # buton adı
window.geometry('600x400')

# text widget yatarma: Text Area
txt = Text(window, height=2, width=40)


# yerleştir:
txt.pack()



window.mainloop() # kapatma