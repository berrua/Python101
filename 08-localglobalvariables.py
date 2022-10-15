#Local - Global Variables

#global
x = 10
y = 20

#local, fonksiyonlarin etki alanindaki degiskenler
def carpma_yap(x = 4,y = 5): #degisiklik olmadi
    return x*y

carpma_yap(2, 3)

#Local Etki Alanindan Global Etki Alanini Degistirmek

x = [] #global etki alani

def eleman_ekle(y):
    x.append(y) #local etki alani
    print(str(y) + " ifadesi eklendi")
    
eleman_ekle("ali")
eleman_ekle("veli")
x

#once local alanda x'i arayacak
#bulamayinca globale cikip oradaki x icin islem yapacak
