#Decision Control Structures

#True-False Sorgulari

sinir = 5000
sinir == 4000 #false
sinir == 5000 #true

#If Yapisi

sinir = 50000
gelir = 40000

if gelir < sinir:
    print("Gelir sinirdan kucuk.")

if gelir > sinir:
    print("Gelir sinirdan buyuk.")
    
#Else Yapisi

sinir = 50000
gelir = 60000

if gelir < sinir:
    print("Gelir sinirdan kucuk.")
else:
    print("Gelir sinirdan buyuk.")
    
sinir = 50000
gelir = 50000
    
if gelir == sinir:
    print("Gelir sinira esit.")
else:
    print("Gelir sinira esit degil.")
    
#Elif Yapisi

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir2 > sinir:
    print("Tebrikler.")
elif gelir2 < sinir:
    print("Uyari!")
else:
    print("Devam.")
    
#Mini Uygulama

sinir = 40000
magaza_adi = input("Magaza adini giriniz: ")
gelir = int(input("Gelirinizi giriniz: "))
    
if gelir > sinir:
    print("Tebrikler " + magaza_adi + "! promosyon kazandiniz!")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir: " + str(gelir))
else:
    print("Devam..")