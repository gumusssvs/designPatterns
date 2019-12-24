
""" FRONTCONTROLLER """

""" RASIM SAVAS / 1160505047 """
class Anasayfa:
    def goster(self):
        print("Goruntulenen:.. ANASAYFA")


class Kullanici:
    def goster(self):
        print("Goruntulenen:.. KULLANICI SAYFASI")
        
    
class yonlendirici:
    def __init__(self):
        self.anasayfa = Anasayfa()
        self.kullanici = Kullanici()

    def sayfaYonlendir(self,sayfa):
        if sayfa.lower() == "kullanici":
            self.kullanici.goster()
        else:
            self.anasayfa.goster()


class frontController:
    def __init__(self):
        self.yonlendirici = yonlendirici()
        
    def kullaniciGiris(self):
        print("giris yapildi")
        return True
    
    def sayfaSec(self,sayfa):
        print("sayfa cagiriliyor:..",sayfa)

    def istekAl(self,sayfa):
        self.sayfaSec(sayfa=sayfa)

        if self.kullaniciGiris():
            self.yonlendirici.sayfaYonlendir(sayfa=sayfa)

frontController = frontController()
frontController.istekAl(sayfa="kullanici")
frontController.istekAl(sayfa="anasayfa")




























