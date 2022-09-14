# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 17:57:25 2022

@author: ilhan
"""

#yield


"""
-iterasyon -> yineleme
-generator -> değerleri bellekte saklamaz, yeri gelince anında üretir.
-yield -> fonksiyon return olarak generator döndürecekse, return yerine yield keyword'ü ile yapar.

"""

liste = [1,2,3,4]
for i in liste:
    print(i)
    
#iterasyonlarda listenin içerisindeki elemanlar memory'de tutulur.
#eğer veri çok fazla ise bellekte çok fazla yer kaplandığı anlamına gelir.

generator = (x for x in range(1,4)) #bir liste oluşturulup, her bir değer x olarak dışarı aktarılır.

for i in generator:
    print(i)
#ilk iterasyonda 1 oluşturulur.
#diğer iterasyonda 1 unutulup 2 oluşturulur.
#son iterasyonda da 2 unutulup 3 oluşturulur.
#böylelikle memory dolmamış olur.

def createGenerator():
    liste = range (1,4) #1-> inclusive, 4-> exclusive
    for i in liste:
        yield i
        
generator2 = createGenerator()
print(generator2) #hafızadaki adresi görülür.

for i in generator2:
    print(i) #1,2,3 yazdırılır.
    
#görüntü işlemede resimleri bir anda yaratıp tek bir liste içerisinde depolamak yerine, 
#generator ile yaratılıp memory'den avantaj  sağlanır.
#liste içerisine yaratılırsa, resim sayısı arttığı zaman bellek yeterli olmayacaktır.