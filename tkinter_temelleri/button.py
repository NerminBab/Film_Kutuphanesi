import tkinter as tk

# önce ana sayfa yaratılmalı

window = tk.Tk()
window.title('tkinter temelleri') # buton adı
window.geometry('600x400')

# her widget in bir master ı olmalı,yeri, text i
btn = tk.Button(master=window,
                text='durdur',
                width=45, # text-unit
                height=5,
                background='red',
                foreground='white',
                command=window.destroy) # kapatacak

# butonu yerleştir:
btn.pack()


window.mainloop()