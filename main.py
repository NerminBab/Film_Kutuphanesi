"""
Film kütüphanesi
sayfalar:
ana sayfa
film listesi
film detayı

"""
# sayfa ve widget adlı 2 paket oluşturduk.

from widget import Window, SolFrame, SagFrame


if __name__ == '__main__':


    # ana pencere yarat
    pencere = Window("film kütüphanesi")


    # sol frame
    sol_frame = SolFrame(pencere.window, 'solFrame')


    # sağ frame
    sag_frame = SagFrame(pencere.window, 'sagFrame')


    # başlat:
    pencere.start_window()


