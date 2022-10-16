#Map Fonksiyonu

liste = [1,2,3,4,5]

for i in liste:
    print(i+ 10)
    
#her elemanin uzerine 10 ekler
list(map(lambda x: x + 10, liste))
#lambda, verilen bir vektor icinde belirli bir fonksiyonu calistirma imkani verir

#Filter Fonksiyonu

liste = [1,2,3,4,5,6,7,8,9,10]
#saglayan kosullari geri dondurur
list(filter(lambda x: x % 2 == 0, liste)) #mod alma

#Reduce Fonksiyonu

from functools import reduce #kutuphane cagirimi

liste = [1,2,3,4]
reduce(lambda a,b: a + b, liste)