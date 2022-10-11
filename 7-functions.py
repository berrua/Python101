#Fonksiyonlar

print("a", "b", sep = "_", end = ",")
print

len("a")

#fonksiyon tanimlama

def kare_al(x):
    print("Girilen sayinin karesi: " + str(x**2))

kare_al(3)

#fonksiyon icine not ekleme

def kare_al(x):
    print("Girilen sayi: " + str(x) +
          ", Karesi: " + str(x**2))

kare_al(3)

#iki argumanli fonksiyon tanimlama

def carpma_yap(x, y):
    print(x*y)
    
carpma_yap(2,3)

#on tanimli argumanlar

def carpma_yap(x, y=1):
    print(x*y)
    
carpma_yap(2)


def carpma_yap(x, y=1):
    print(x*y)
    
carpma_yap(y = 2, x = 3)

#ornek

def direkt_hesap(isi, nem, sarj):
    print((isi + nem) / sarj)
    
direkt_hesap(30, 40, 70)

#return ifadesi, fonksiyonlarin ciktisini girdi olarak kullanmayi saglar

def direkt_hesap(isi, nem, sarj):
    return (isi + nem) / sarj

cikti = direkt_hesap(26, 49, 65)
cikti
print(cikti)
direkt_hesap(26, 49, 65)*7
