#Veri yapilari

#Listeler
#[]
#list()
#degistirilebilir, kapsayicidir, siralidir

notlar = [90,80,70,60]
type(notlar)

liste = ["a",19.3,90]

liste_genis = ["a",19.3,90, notlar]
len(liste_genis)

#Liste ici tip sorgulama

type(liste_genis[0])
type(liste_genis[1])
type(liste_genis[2])
type(liste_genis[3])

tum_liste = [liste, liste_genis]
#del tum_liste

#Eleman islemleri

notlar = [90,80,70,60]
notlar[1]
notlar[5]
notlar[:2]
notlar[2:]

yeni_liste = ["a", 10,[20,30,40,50]]
yeni_liste[2][1] #30

#Eleman silme

liste = ["ali","veli","ayse","berna"]
liste[1] = "ahmet"
liste

liste[0:3] = "mete","ahmet","sena"
liste

liste + ["kemal"]
liste

#del liste[2]
liste

#Liste metodlari

liste2 = ["ali","veli","berat"]

dir(liste2) #metodlari listeler

liste2.append("murat") #yeniden atama yapmadan kalici ekleme metodu
liste2

liste2.remove("murat") #silme metodu
liste2

liste2.insert(0,"ayse") #indexe gore eleman ekleme
liste2

liste2[2] = "burak" #degistirme
liste2

liste2.insert(5,"betul")
liste2

len(liste2)

liste2.insert(len(liste2),"beren") #liste sonuna eleman ekleme
liste2

liste2.pop(0) #indexe gore eleman cikarma
liste2

liste2.count("ali") #eleman sayisi verir
liste2

liste2.count("eda")
liste2

liste_yedek = liste2.copy() #liste kopyalama
liste_yedek

liste2.extend(["a","b",10]) #liste birlestirme
liste2

liste2.index("ali") #elemanin indexini verir

liste2.reverse() #liste elemanlari sirasini tersine cevirir
liste2

liste3 = [10,40,55,2]
liste3.sort() #listeyi kucukten buyuge siralar
liste3

liste3.clear() #liste temizleme
liste3

liste4 = [1,2,3,4]
liste4.pop() #son elemani cikar
liste4.reverse() #tersine cevirir