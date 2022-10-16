#Functional Programming

#fonksiyonlar dilin bastacidir
#birinci sinif nesnelerdir
#yan etkisiz fonksiyonlar, (stateless, girdi-cikti)
#yuksek seviye fonksiyonlar
#vektorel operasyonlar

#Yan Etkisiz Fonksiyonlar (pure functions)

#ornek1, bagimsizlik
A = 5
def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3, 4)

#ornek2, olumcul

#OOP
class LineCounter: #dosya acma ve satir sayma
    def __init__(self, filename): #ornek ozellik tanimlama
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)

lc = LineCounter('deneme.txt')

print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())

#FP
def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
lines_count

#Isimsiz Fonksiyonlar

def old_sum(a,b):
    return a + b
old_sum(4,5)

new_sum = lambda a,b : a + b
new_sum(4,5)

sirasiz_liste = [('b',3),('a',8),('c',1)]
sirasiz_liste

#atama yapmadan siralama
sorted(sirasiz_liste, key = lambda x: x[1])

#Vektorel Operasyonlar (vectorel operations)

#OOP
#a ve b listesinde ayni indisteki elemanlari birbiriyle carp
a = [1,2,3,4]
b = [2,3,4,5]

ab = []
for i in range(0, len(a)):
    ab.append(a[i]*b[i])
ab

#FP
import numpy as np 
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b