import tkinter as tk

# önce ana sayfa yaratılmalı

window = tk.Tk()
window.title('tkinter temelleri -Checkbutton') # buton adı
window.geometry('600x400')

# checkButton widget yatarma:
chkbtn1 = tk.Checkbutton(master=window, text='doğru')
chkbtn2 = tk.Checkbutton(master=window, text='yanlış')

# yerleştir:
chkbtn1.grid(row=0, column=0)
chkbtn2.grid(row=1, column=0)


window.mainloop() # kapatma