import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk


class AnaSayfa:
    """
    anasayfa frame dir.
    """
    def __init__(self, window, fon_rengi, relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='anaSayfa',
            relief=relief,
            bg=fon_rengi
        )

        self.side = side     #BAKKK
        self.frame_icerigi()
        self.frame_ekle()


    def frame_ekle(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True) # BAKKK self.side

    def frame_icerigi(self):

        tanitim = tk.Label(self.frame,
                           text='Temel Python',
                           font=('Helvetica', 18, 'bold'),
                           bg='orange'
                           )
        tanitim.place(x=315, y=50)

        isim = tk.Label(self.frame,
                        text='NERMİN BABALIK',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange')

        isim.place(x=280, y=105)

        self.render_image()

        proje = tk.Label(self.frame,
                        text='Bitirme Projesi: Film Kütüphanesi',
                        font=('Helvetica', 18, 'bold'),
                        bg='black',
                        fg='white')
        proje.place(x=140, y=765)

    def render_image(self):
        load = Image.open("images/home/python_logo.png")
        render = ImageTk.PhotoImage(load)
        img_lbl = tk.Label(self.frame, image=render, bg='orange')
        img_lbl.image = render
        img_lbl.place(x=136,y=180)




