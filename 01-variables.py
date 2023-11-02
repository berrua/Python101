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

string = "hello world"
string[2] #2. indisteki karakter 
string[:2] #ilk 2 karakter 
string[::] #tamami
string[::3] #3'er atla
string[2:5] #2'den basla, 5'te dur
string[2:5:2] #2'den basla, 5'te dur, 2'şer atla'
string[::-1] #tersten yazma 

#metodlar (fonksiyonlar)
a = "hello" #atama

b = 9
c = 8

b * c

len(a) #boyutunu yazar
len("hello world")

a.capitalize() #ilk harfi buyuk harfe cevirir
a.upper() #stringi buyuk harfe cevirir
a.lower() #stringi kucuk harfe cevirir

a.islower() #kucuk harf mi diye kontrol eder
d = a.upper()
d.islower()
d.isupper() #buyuk harf mi diye kontrol eder

a.replace("e","a") #e'leri a ile degistirir

a.split() #kelimeleri ayirir

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