#STRING
#string'in 5. harfini my_letter isimli bir degiskene atayiniz
my_string = "James Hetfield"
my_letter = my_string[4]

#string'in 5. ve 8. karakteri arasindaki tum harfleri yazdiriniz (5, 8 dahil)
my_new_string = "QuentinTarantino"
my_new_string[4:8]

#string'i tersten yazdiriniz
my_last_string = "afyonkarahisarlılaştıramadıklarımızdanmısınız"
my_last_string[::-1]

#INT & FLOAT
#asagidaki islemin sonucu hangi veri tipinde olacaktir
3 + 10.2 + 50
number = 3 + 10.2 + 50
type(number)

#asagidaki islemin sonucu kactir
5 + 8 * 12

#LIST & DICTIONARY & SET
#bu listeyi 3 farkli yoldan olusturunuz: [1,2,"a"]
my_list_1 = [1,2,"a"]

my_list_2 = []
my_list_2.append(1)
my_list_2.append(2)
my_list_2.append("a")
my_list_2

my_list_3 = list()
my_list_3.append(1)
my_list_3.append(2)
my_list_3.append("a")
my_list_3

#asagidaki "a"'yi tek satirda aliniz
my_list = [1,4,[2,3,"a"]]
my_list[2][2]

#asagidaki "b"'yi tek satirda aliniz
my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}
my_dictionary["kk"][1]["kkkk"]

#asagidaki liste set'e cevirilince hangi degerler icinde kalacaktir
my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45]
my_new_set = set(my_list_to_be_set)
my_new_set #[11,12,21,22,32,33,45]

#BOOLEAN
#asagidaki ifadenin sonucu ne olacaktir
x = 40 * 5 + 3
y = 208 - 2 * 4
x > y
True

#asagidaki ifadenin sonucu ne olacaktir
a = 40 * (4 - 2)
b = 80 - 2 * -5
a > b
False