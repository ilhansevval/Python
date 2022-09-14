# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#variables

#python temelinde 3 çeşit component var.Bunlar
# 1)variable
# 2)function
# 3)object

#variable pythonda bir kodu organize etmek ve belli değerler tanımlamak için kullanılan kalıplardır.
#variable ismi rakamla başlayamaz.
#variable tanımlanırken ilk harfin küçük harfle başlaması tavsiye edilir.

var1 = 10 #integer
var2 = 15

#burada variablelar tanımlandı.

#strinler karakter dizileridir.
gun="pazartesi" #string

var3=10.0 #double(float)

#4 işlem özellikleri

pi_sayisi = 3.14
katsayi = 2

toplam = pi_sayisi + katsayi #5.140000000000001
fark   = pi_sayisi - katsayi #1.1400000000000001
carpma = pi_sayisi * katsayi #6.28
bolme  = pi_sayisi / katsayi #1.17

#print değişkenleri, veri tiplerini yazdırmak için kullanılır.

print("Toplam: ",toplam) #Toplam:  5.140000000000001
print("Toplam {} ve Fark {}".format(toplam,fark)) #Toplam 5.140000000000001 ve Fark 1.1400000000000001
print("Çarpma %.1f , Bolme %.4f" % (carpma,bolme)) #Çarpma 6.3 , Bolme 1.5700

#değişkenler arası dönüşümler

carpma_int = int(carpma)
print(carpma_int) #6

katsayi_float = float(katsayi)
print(katsayi_float) #2.0