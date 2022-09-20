#type tip bilgisi verir
type(9)
type(9.9)
type("hello")

"hello"
'hello'

123 
type(123)
"123"
type("123")

"a" + "b"
"a" "b"
"a " + "b"
"a" + "-b"
"a" * 3
"a " * 3

#metodlar (fonksiyonlar)
a = "hello" #atama

b = 9
c = 8

b * c

len(a) #boyutunu yazar
len("hello")

a.upper() #stringi buyuk harfe cevirir
a.lower() #stringi kucuk harfe cevirir

a.islower() #kucuk harf mi diye kontrol eder
d = a.upper()
d.islower()
d.isupper() #buyuk harf mi diye kontrol eder

a.replace("e","a") #e'leri a ile degistirir

a
a.replace("o", "u")

a = " hello "
a.strip() #istenmeyen karakterleri kirpar
a = "*hello*"
a.strip()
a = "* hello *"
a.strip()
a = "* hello *"
a.strip("*")
a = "hellok"
a.strip("k")

