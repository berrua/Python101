#Hatalar - Istisnalar (exceptions)

#ZeroDivisionError Hatasi
a = 10
b = 0

a / b

try: #calistirmayi dene
    print(a/b)
except ZeroDivisionError: #hatayi istisna olarak gor
    print("Paydada 0 olamaz")
    
#Type Hatasi
a = 10
b = "2"

a + b

try: #calistirmayi dene
    print(a/b)
except TypeError: #hatayi istisna olarak gor
    print("Sayi ve string toplanamaz")
    
    