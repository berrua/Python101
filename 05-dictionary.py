#Dictionary
#kapsayicidir, sirasizdir ve degistirilebilir
#anahtar ve karsiliklari bir arada tutulur (referanslidir)
#indexleme yapilamaz

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}
sozluk
len(sozluk)

sozluk = {"REG" : 10,
          "LOJ" : 20,
          "CART" : 30}
sozluk

sozluk = {"REG" : ["RMS",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}
sozluk

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}
sozluk[0]

sozluk["REG"]
sozluk["LOJ"]
sozluk["CART"]

sozluk = {"REG" : ["RMS",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}

sozluk["REG"]
sozluk["LOJ"]
sozluk["CART"]

sozluk = {"REG" : {"RMS":10,
                   "MSE":20,
                   "SSE":30},
          
          "LOJ" : {"RMS":10,
                   "MSE":20,
                   "SSE":30},
          
          "CART" : {"RMS":10,
                    "MSE":20,
                    "SSE":30},}
sozluk
sozluk["REG"]["SSE"] #ic ice yapi

sozluk = {"REG" : ["RMS",10],
          "LOJ" : ["MSE",20],
          "CART" : ["SSE",30]}
sozluk

sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}
sozluk["GBM"] = "Gradient Boostig Mac" #ekleme
sozluk

sozluk["REG"] = "Coklu Dogrusal Reg" #guncelleme
sozluk
 
sozluk[1] = "Yapay Sinir Aglari" #ekleme
sozluk

l = [1]
l

sozluk[l] = "yeni bir sey" #sabit veri yapisi olmadigi icin hata verdi
#key degerleri sabit olmali

t = ("tuple",)
sozluk[t] = "yeni bir sey"
sozluk