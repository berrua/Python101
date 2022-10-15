#Loops

#For dongusu

ogrenci = ["ali", "veli", "ayse", "nazli"]
ogrenci[0]
ogrenci[1]
ogrenci[2]
ogrenci[3]

for i in ogrenci:
    print(i)
    
#ornek

maaslar = [1000,2000,3000,4000,5000]
maaslar[0]
maaslar[1]
maaslar[2]
maaslar[3]
maaslar[4]

for i in maaslar:
    print(i*2)
    
for maas in maaslar:
    print(maas)
    
#Donguler ve Fonksiyonlar

def kare_al(x):
    print(x**2)
kare_al(2)

maaslar = [1000,2000,3000,4000,5000]
for i in maaslar:
    print(i)
    
#maaslara %20 zam
maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]

#fonksiyon yazilacak
def yeni_maas(x):
    print(x*20/100 + x)
yeni_maas(1000)
yeni_maas(2000)

#dongu yazilacak
for i in maaslar:
    yeni_maas(i)

#If, For ve Fonksiyonlar Mini Uygulama

maaslar = [1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100 + x)
    
def maas_alt(x):
    print(x*20/100 + x)

for i in maaslar:
    if i >= 3000:
        maas_ust(i)
    else:
        maas_alt(i)

#Break - Continue

maaslar = [8000,5000,2000,1000,3000,7000,1000]

dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000: #3000 degerinde durur
        print("Durdu.")
        break
    print(i)

for i in maaslar:
    if i == 3000: #3000 degerini atla
        continue
    print(i)

#While dongusu
#sart saglandigi surece

sayi = 10
while sayi < 20:
    sayi += 1
    print(sayi)