# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:28:48 2022

@author: ŞEVVAL
"""

#tuple

"""değiştirilemez ve sıralı bir veri tipidir
   (1,2,3)
"""
#listede köşeli parantez vardır, burada normal parantez

t=(1,2,3,4,5,6)
 
t[2] #2.indeks olarak 3 yazdırılır.

t[3:] #2.indeksten sonraki elemanları yazdırır.

dir(t) #oluşturulan tuple'ın methodlarını gösterir.

help(tuple.count) #count methodunun ne işe yaradığını gösterir.
#tuple'ın içindeki bir veriden kaç tane olduğunu hesaplar.

t.count(3) #tuple'ın içinde 3'ten 1 tane vardır.

help(tuple.index) #tuple'ın içindeki seçilen verinin indexini döndürür.

t.index(3) #3'ün indexi 2'dir.

a = "sakin calismaktan vazgecmeyin"

a[1]+a[0]+a[8]+a[1] + " " + a[-11:]

#a[1]+a[0]+a[8]+a[1] bu kısımda harf harf alır, asla kelimesi oluşur.
#a[-11:] bu kısımda sonuncu kelimenin tamamı alınır.
#'asla vazgecmeyin' yazdırılır.

#bir fonksiyonda birden fazla elemanı return ederken tuple kullanılır.

tuple_xyz = (1,2,3) 
#bir resim için; x. ve y. koordinatlarda ve videonun 3.frame'indeki görsel tuple içerisinde return edilir.

#bunu ayrıştırmak için;
x , y, z = tuple_xyz
#sırasıyla 1 -> x, 2 -> y, 3 -> y şeklinde ayrılır.