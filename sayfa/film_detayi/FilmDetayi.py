import tkinter as tk
from data.renkler import RENKLER
from PIL import Image, ImageTk


class FilmDetayi:
    """ Film detay frame idir """
    def __init__(self, window, fon_rengi, imdbID=None, filmler=[], relief=tk.SUNKEN, side=tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name='filmDetayi',
            relief=relief,
            bg=fon_rengi
        )
        self.side = side
        self.imdbID = imdbID
        self.filmler = filmler
        self.frame_ekle()

    def frame_ekle(self):
        self.frame_icerigi()
        self.frame_basligi('Film Detayı')
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_basligi(self, baslik):
        if self.imdbID != None:
            bsl = tk.Label(self.frame, text=self.film['Title'], height=3,
                       bg=RENKLER.SIYAH, fg=RENKLER.BEYAZ, font=('Arial',12,'bold'))
            bsl.grid(row=0, column=0, columnspan=8, padx=1, pady=(0, 8), sticky='we')
        else:
            bsl = tk.Label(self.frame, text=baslik, height=3,
                       bg=RENKLER.SIYAH, fg=RENKLER.BEYAZ, font=('Arial',12,'bold'))
            bsl.pack(fill=tk.X, padx=(1,0))

    def frame_icerigi(self):
        # film listesinden filme tıklanmadan direkt ana sol framedeki film detayına tıklanırsa eğer:
        if self.imdbID != None:
            self.render_image()
            self.get_film()
            self.render_keys()
            self.render_values()
        else:
            pass

    def render_image(self):
        try: # resim eklerken try da yap olmayailir diye
            # her filmin resmi ıd ile geliyor JPG dosyaları
            load = Image.open("images/posters_large/" + str(self.imdbID) + ".jpg")
        except:
            # yoksa no image ı al
            load = Image.open("images/posters_large/no_image.jpg")
        finally:
            render = ImageTk.PhotoImage(load)
            img_label = tk.Label(self.frame, image=render, bg='orange')
            img_label.image = render
            img_label.grid(row=1, column=0, columnspan=2, pady=(0,10))

    def get_film(self):
        for f in self.filmler:
            if f['imdbID'] == self.imdbID:
                self.film = f
                break

    def render_keys(self):
        for i,key in enumerate(self.film.keys()):
            txt = str(key)
            lbl = tk.Label(self.frame, text=txt, height=2, width=12, anchor='w')
            self.fill_bg(lbl, i)
            lbl.grid(row=i+2, column=0, padx=(10,1))

    def fill_bg(self,widget, i):
        if i % 2 == 1:
            widget.configure(bg=RENKLER.LIST_SATIR_TEK)
        else:
            widget.configure(bg=RENKLER.LIST_SATIR_CIFT)

    def render_values(self):
        for i,value in enumerate(self.film.values()):
            txt = str(value)
            lbl = tk.Label(self.frame, text=txt, height=2, width=96, anchor='w')
            self.fill_bg(lbl, i)
            lbl.grid(row=i+2, column=1, padx=(0,8))

