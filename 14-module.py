#Modul (Kutuphane, Paket) Olusturmak
#belirli amaclari yerine getirmek icin birarada bulunan fonksiyonlar grubu

def yeni_maas(x):
    print(x*20/100 + x)

maaslar = [1000,2000,3000,5000]

#test
import HesapModulu
HesapModulu.yeni_maas(1000)
HesapModulu.yeni_maas(2000)

import HesapModulu as hm
hm.yeni_maas(1000)

from HesapModulu import yeni_maas
yeni_maas(4000)

import HesapModulu as hm
hm.maaslar
