"""  Frame : container, başka widget leri tutar  """

import tkinter as tk
from tkinter import Frame, Button

# önce ana sayfa yaratılmalı

window = tk.Tk()
window.title('tkinter temelleri -Frame') # buton adı
window.geometry('600x400')

# frame widget yatarma:
frame = Frame(master=window)

# frame içini doldur:
btnL = Button(master=frame, text='frame butonu left',bg='black',fg='white')  # frame olduğu için master ı window değil
btnR = Button(master=frame, text='frame butonu Right',bg='black',fg='white')

# yerleştir:
frame.pack()
btnR.pack(side=tk.RIGHT)
btnL.pack(side=tk.LEFT)


window.mainloop() # kapatma