import tkinter as tk
from tkinter import ttk
from data.renkler import RENKLER
import csv
from PIL import Image, ImageTk
from sayfa.film_detayi.FilmDetayi import FilmDetayi


class FilmListesi:
    """ film listesi frame dir """
    # FİLM LİSTESİNİ ANASAYFAYA YÜKLEDİKTEN SONRA SAYFALARA BÖLMEK İÇİN "def combo_box_olustur(self):" İÇİN:
    sayfa_no = 1
    sayfa_basina_adet = 10
    toplam_sayfa_sayisi = 0

    sutunlar = ['imdbID', 'Id', 'Title', 'Year', 'imdbRating', 'imdbVotes']

    def __init__(self, master, fon_rengi, relief=tk.SUNKEN, side=tk.LEFT):
        self.i = None
        self.combo_box_selected_event = None
        self.frame=tk.Frame(
            master=master,
            name='filmListesi',
            relief=relief,
            bg=fon_rengi
        )
        self.side = side
        self.filmler = []
        self.frame_ekle()


    def frame_ekle(self):
        self.frame_basligi('Film Listesi')
        self.csv_oku()
        self.sayfa_olustur()
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)


    def frame_basligi(self, baslik):
        bsl = tk.Label(self.frame, text=baslik, height=3,
                       bg=RENKLER.SIYAH, fg=RENKLER.BEYAZ, font=('Arial',12,'bold'))
        bsl.grid(row=0, column=0, columnspan=8,padx=1, pady=(0,8),sticky='we')

    def csv_oku(self):
        film_oku = "data/imdb_top_250.csv"
        with open(film_oku, 'r') as dosya:
            film_dict = csv.DictReader(dosya, delimiter = ";")
            for film in film_dict:
                self.filmler.append(film)
        # TOPLAM SAYFA SAYISINI HESAPLA:
        FilmListesi.toplam_sayfa_sayisi = len(self.filmler) // FilmListesi.sayfa_basina_adet + 1

    def sayfa_olustur(self):
        self.add_title_row()
        self.tablo_olustur()
        # TÜM FİLMLERİ FİLM LİSTESİNE YÜKLEDİKTEN SONRA SAYFALARA AYIRMAK İÇİN COMBO BOX YAPILIR(SAYFALARI OLUŞTURURUZ):
        self.combo_box_olustur()


    def add_title_row(self):
        for j, sutun in enumerate(FilmListesi.sutunlar):
            if sutun != 'imdbID':
                lbl = tk.Label(self.frame, text=str(sutun), width=54, height=2, bg=RENKLER.SIYAH, fg='white',
                               font=('Arial',10,'bold'))
                if sutun == 'Id':
                    lbl.configure(text='#', width=4)
                elif sutun == 'Title':
                    lbl.configure(text='Film Adı')
                elif sutun == 'Year':
                    lbl.configure(text='Yıl', width=8)
                elif sutun == 'imdbRating':
                    lbl.configure(text='Puanı', width=8)
                elif sutun == 'imdbVotes':
                    lbl.configure(text='Oy Sayısı', width=12)
                if sutun == 'imdbVotes':
                    lbl.grid(row=1, column=j, sticky='we', padx=(0,10))
                else:
                    lbl.grid(row=1, column=j, sticky='we', padx=(0, 1))

    def tablo_olustur(self):
        for i, film in enumerate(self.filmler):
            # COMBOBOX OLUŞTURULDUKTAN SONRA FİLMLERİN HEPSİNİN İLK SAYFADA OLMASINI ENGELELMEK SAYFALARA BÖLMEK İÇİN:
            if (FilmListesi.sayfa_no - 1) * FilmListesi.sayfa_basina_adet <= i < \
                    FilmListesi.sayfa_no * FilmListesi.sayfa_basina_adet:
                for j, key in enumerate(FilmListesi.sutunlar):
                    name = 'table_row_' + str(i) + str(j) + '_' + film['imdbID'] # table_row_ mi??????
                    if j == 0:
                        #resim bastır
                        self.render_image(film, i, j, name)
                    else:
                        #yazı bastır
                        self.write_label(film, i, j, key, name)

            self.i = i+3

    def render_image(self, film, i, j, name):
        try: # resim eklerken try da yap olmayailir diye
            # her filmin resmi ıd ile geliyor JPG dosyaları
            load = Image.open("images/posters_small/" + film['imdbID'] + ".jpg")
        except:
            #yoksa no image
            load = Image.open("images/posters_small/no_image.jpg")
        finally:
            render = ImageTk.PhotoImage(load)
            img_label = tk.Label(self.frame, name=name, image=render, bg='orange')
            img_label.image = render
            img_label.grid(row=i+2, column=j, padx=(7,0),sticky='we') # resimlerin diyezin altından başlamsı için +2 dedik


    def write_label(self, film, i, j, key, name):
        lbl = tk.Label(self.frame, name=name, text=str(film[key]), height=4, fg='black',
                       font=('Arial',10,'bold'), cursor='hand2')
# FİLM DETAYI.PY SAYFASINI OLUŞTURURKEN FİLMLERE TIKLANINCA DETAY VERMESİ İÇİN:
        lbl.bind('<Button-1>', self.film_click)

        if key == 'Id':
            lbl.configure(width=4)
        elif key == 'Title':
            lbl.configure(width=54, anchor='w')
        elif key == 'Year':
            lbl.configure(width=8)
        elif key == 'imdbRating':
            lbl.configure(width=8)
        elif key == 'imdbVotes':
            lbl.configure(width=12)

        self.fill_bg(lbl, i)

        if key == 'imdbVotes':
            lbl.grid(row=i+2, column=j, sticky='we', padx=(0, 10))
        else:
            lbl.grid(row=i+2, column=j, sticky='we', padx=(0, 1))

    def fill_bg(self,widget, i):
        if i % 2 == 1:
            widget.configure(bg=RENKLER.LIST_SATIR_TEK)
        else:
            widget.configure(bg=RENKLER.LIST_SATIR_CIFT)

            # COMBOBOX DA SAYFA NUMARALARINA TIKLAYINCA MEVCUT SAYFANIN SİLİNMESİ İÇİN:

    def tablo_bosalt(self, event):
        master = event.widget.master
        for child in master.children.copy():
            if 'table_row' in child:
                master.children[child].destroy()



    def combo_box_selected_event(self, event):
        FilmListesi.sayfa_no = int(event.widget.get())
        self.tablo_bosalt(event)
        self.tablo_olustur()


    def combo_box_olustur(self):
        values = list(range(1, FilmListesi.toplam_sayfa_sayisi))
        sayfalar = ttk.Combobox(self.frame, width=4, values=values)
        sayfalar.current(FilmListesi.sayfa_no - 1)
        sayfalar.bind('<<ComboboxSelected>>', self.combo_box_selected_event)
        sayfalar.grid(row=self.i, column=2, pady=(15,0))



    def film_click(self,event):
        imdbID =str(event.widget).split('_')[3]
        # önce sağ frame içini düzenle
        self.sag_frame_duzenle(event, imdbID)
        # sol frame i düzenle:
        self.sol_frame_duzenle(event)


    def sag_frame_duzenle(self, event, imdbID):
            sagFrame = event.widget.master
            for child in sagFrame.winfo_children():
                child.destroy()

            # film detayını yaz, sayfaların içinden
            FilmDetayi(sagFrame,'orange', imdbID=imdbID, filmler=self.filmler)

    def sol_frame_duzenle(self, event):
        root = event.widget.master.master.master
        for child in root.winfo_children():
            if str(child) == '.solFrame':
                for ch in child.winfo_children():
                    if str(ch) == '.solFrame.filmDetayi':
                        ch.configure(bg=RENKLER.TURUNCU, fg=RENKLER.BEYAZ)
                    else:
                        ch.configure(bg=RENKLER.SIYAH, fg=RENKLER.TURUNCU)








