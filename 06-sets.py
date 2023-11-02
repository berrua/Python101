#Set
#sirasizdir, degerleri essizdir, degistirilebilir ve farkli tipleri barindirir
#hiz icin tercih edilir

s = set() #set olusturur
s

l = [1,"a","ali",123]
s = set(l)
s

t = ("a","ali")
s = set(t)
s

ali = "kod_yaz"
type(ali)

s = set(ali)
s

l = ["kod", "yaz"]
l

s = set(l)
s

len(s)

l[0]
s[0] #indexlenemez

l = ["kod","yaz"]
s = set(l)
s

dir(s)

s.add("bugun") #ekleme
s

s.add("bugun") #tekrar eklemeye izin vermez
s

s.remove("bugun") #cikarma, hata verir
s

s.discard("bugun") #cikarma, hata vermez
s

#Klasik Kume İslemleri
# =============================================================================
# difference() iki kumedeki farkli eleman
# intersection() iki kumenin kesisimi, ortaklari
# union() iki kumenin birlesimi
# symmetric_difference() ikisinde ortak olmayan eleman
# =============================================================================

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1

set1.intersection(set2)
set2.intersection(set1)

set1 & set2

set1.union(set2)
set2.union(set1)

set1.intersection_update(set2) #kesisim elemanlari set1in elemani oldu
set1

#Sorgu Islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#iki kumenin kesisiminin bos olup olmadigini sorgulama
#true bos
#false bos degil

set1.isdisjoint(set2)

#bir kumenin butun elemanlarinin baska bir kume icinde olup olmadigini sorgular
#set1 set2nin alt kumesi midir?

set1.issubset(set2)

#bir kumenin diger bir kumeyi kapsayip kapsamadigini sorgular

set1.issuperset(set2)