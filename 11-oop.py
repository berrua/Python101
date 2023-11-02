#Classes

#sinif tanimlama
class VeriBilimci():
    print("Bu bir siniftir")
    
#Sinif Ozellikleri

class Gelistirici():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []
    
#siniflarin ozelliklerine erismek
Gelistirici.bolum
Gelistirici().sql

#siniflarin ozelliklerini degistirmek
Gelistirici.sql = 'Hayir'
Gelistirici().sql

#sinif orneklendirilmesi (instantion)
ali = Gelistirici()
ali.sql
ali.deneyim_yili
ali.bolum

#ozellik ekleme
ali.bildigi_diller.append("Python") #yapilan degisiklik, tum sinif icin gecerli oldu
ali.bildigi_diller

veli = Gelistirici()
veli.sql
veli.bildigi_diller

#Ornek Ozellikleri
class Gelistirici():
    bolum = ''
    sql = ''
    deneyim_yili = 0
    bildigi_diller = ["Java","Python"]
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
#self, ornekleri temsil eden temsilci

ali = Gelistirici()
veli = Gelistirici()

ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli.bildigi_diller.append("Java")
veli.bildigi_diller

Gelistirici.bildigi_diller

ali.bolum = "istatistik"
ali.bolum

veli.bolum = "endustri"
veli.bolum

Gelistirici.bolum

#Ornek Metodlari

class Gelistirici(): #sinif tanimlama
    calisanlar = [] #nesne olusturuldu
    def __init__(self):
        self.bildigi_diller = [] #ornek ozelligi tanimlama
        self.bolum = ''
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil) #guncelleme fonksiyonu yazildi

ali = Gelistirici()
ali.bildigi_diller
ali.bolum

veli = Gelistirici()
veli.bildigi_diller
veli.bolum

dir(Gelistirici) 

ali.dil_ekle("Java")
veli.dil_ekle("Python")

ali.bildigi_diller
veli.bildigi_diller

#Miras Yapilari (inheritance)
#bir class'in ozellikleri diger class'in ozelliklerini iceriyorsa,
#bu ozellikler miras olrak kullanilir

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class Develop(Employees): #employees ozellikleri miras alindi
    def __init__(self):
        self.Programming = ""

class Marketing(Employees):
    def __init__(self):
        self.Storytelling = ""

gelistirici1 = Develop()
gelistirici1.FirstName #kontrol

mark1 = Marketing()
mark1.FirstName #kontrol

#extra

class Employees_yeni():
    def __init__(self, FirstName,LastName,Address): #fonksiyonel yapida tanimlama
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address

ali = Employees_yeni("Ali", "Yilmaz", "Turkey")
ali.Address
