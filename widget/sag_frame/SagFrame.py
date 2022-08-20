import tkinter as tk
from sayfa import AnaSayfa, FilmListesi, FilmDetayi



class SagFrame:
    """    ana sayfanın sağ tarafında sayfalrı tutar.    """
    fon_rengi = 'orange'

    def __init__(self, window, name, relief= tk.SUNKEN, side = tk.LEFT):
        self.frame = tk.Frame(
            master=window,
            name=name,
            relief=relief,
            bg=SagFrame.fon_rengi
        )
        self.side = side,
        self.frame_ekle()

    def frame_ekle(self):
        # frame içeriği:
        self.frame_icerigi()
        self.frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)   #BAKKK!! HOCADAN FARKLI

    def frame_icerigi(self, sayfa_adi='anaSayfa'):
        try:
            gelenframe = self.frame
        except:
            gelenframe = self
        finally:
            if sayfa_adi == 'anaSayfa':
                AnaSayfa(gelenframe, SagFrame.fon_rengi)
            elif sayfa_adi == 'filmListesi':
                FilmListesi(gelenframe, SagFrame.fon_rengi)
            elif sayfa_adi == 'filmDetayi':
                # FİLM DETAY:
                FilmDetayi(gelenframe, SagFrame.fon_rengi)

    # film listesine tıklandığında detayların görünmesi için ana sayfadki isim ve logonun silinmesi için:
    def destroy_children(frame):
        for child in frame.winfo_children():
            child.destroy()
