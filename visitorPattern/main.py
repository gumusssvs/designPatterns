""" Visitor Pattern """

""" RASIM SAVAS / 1160505047 """

from __future__ import generators
import random

class Cicek(object):
    def kabulEder(self, ziyaretci):
        ziyaretci.ziyaret(self)
    def polenleme(self, polenlendi):
        print(self, polenlendi, " tarafindan polenlendi")
    def yer(self, yiyici):
        print(self, yiyici, " tarafindan yenildi")
    def __str__(self):
        return self.__class__.__name__

class Papatya(Cicek): pass
class Gul(Cicek): pass
class Menekse(Cicek): pass

class Ziyaretci:
    def __str__(self):
        return self.__class__.__name__

class Bocek(Ziyaretci): pass
class Polenleyen(Bocek): pass
class Avci(Bocek): pass

# Ari Hareketleri
class Ari(Polenleyen):
    def ziyaret(self, cicek):
        cicek.polenleme(self)\

# Solucan hareketleri
class Solucan(Avci):
    def ziyaret(self, cicek):
        cicek.yer(self)

def cicekGen(n):
    cicekler = Cicek.__subclasses__()
    for i in range(n):
        yield random.choice(cicekler)()

ari = Ari()
solucan = Solucan()
for cicek in cicekGen(5):
    cicek.kabulEder(ari)
    cicek.kabulEder(solucan)
