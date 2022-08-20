import tkinter as tk
from data.renkler import RENKLER
from data.menuler import MENU

from widget.button.Button import Button
from widget.sag_frame.SagFrame import SagFrame


# handle_click bu sayfada tanımlandığı için film listesine tıklanınca göstereceği filmler için bu sayfada işlem yaptık.


class SolFrame:
    """
    sayfanın sol tarafında menü butonlarını tutar.
    """
    def __init__(self,window, name):
        self.frame = tk.Frame(
            master=window,
            name=name,
            bg =RENKLER.SIYAH
        )
        self.master = window
        self.menuleri_ekle()
        self.frame_ekle()

    def frame_ekle(self):
        self.frame.pack(side=tk.LEFT, fill=tk.Y, pady=(62,0))

    def handle_click(self, event):
        self.button_renklerini_yonet(event)
        sayfa_adi = str(event.widget).split('.')[2] # film listesinden sonra buraya ekledik.
        # print(sayfa_adi,'tıklandı.')


        # film listesi py oluşturduktan sonra sol frame dekilere basınca silinip tıklanan bilgilerin gelmesi için:
        sgFrame = self.master.children['sagFrame'] # basınca sag frame çalışacağı için buraya ekledik.
        # sag frame içindeki çockları destroy et(sil)
        SagFrame.destroy_children(sgFrame)
        SagFrame.frame_icerigi(sgFrame, sayfa_adi)


    def menuleri_ekle(self):
        #BUTONLARI DÖNGÜ İLE EKLE:
        for menu_key, menu_text in MENU.items():

            if menu_key == 'uygulamaHakkinda':
                button = Button(self.frame, menu_key, menu_text, RENKLER.TURUNCU, RENKLER.SIYAH, 18, 2,
                                self.handle_click, 0,0, tk.BOTTOM)
            else:
                button = Button(self.frame, menu_key, menu_text, RENKLER.TURUNCU, RENKLER.SIYAH, 18, 2,
                                self.handle_click)
                # window ilk açıldığında anasayfa nın seçili gelmesi (turuncu olarak gelmesi) için:
                if menu_key == 'anaSayfa':
                    SolFrame.secili_button_rengi(button.button)


    def button_renklerini_yonet(self,event):
        # TIKLANAN BUTON:
        # seçili olanın tüm kardeşlerini siyah yap
        for child in event.widget.master.winfo_children():
            child.configure(bg=RENKLER.SIYAH, fg=RENKLER.TURUNCU)
        # seçili oalnı turuncu yap:
        SolFrame.secili_button_rengi(event.widget)

    def secili_button_rengi(button):
        button.configure(bg=RENKLER.TURUNCU, fg=RENKLER.BEYAZ)




