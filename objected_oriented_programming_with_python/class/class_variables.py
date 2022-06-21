# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 14:11:26 2022

@author: ŞEVVAL
"""

class Calisan(): 

    zam_orani = 1.8 #class variable
    
    counter = 0

    def __init__(self,isim,soyisim,maas): #initial methodu yeni bir obje yaratıldığında çağrılır.
        self.isim=isim 
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@gmail.com"
        
        Calisan.counter = Calisan.counter+1 #classta yeni bir obje yaratıldığında counter 1 artar.
                                      
        
    def ZamYap(self):
        #methodun içindeki self ile constructorın içinde define edilmiş variablelara erişim sağlanır.
        self.maas = self.maas + self.maas*self.zam_orani


calisan1 = Calisan("nazli","acar",100)

print("ilk maas: ",calisan1.maas) #ilk maas:  100

calisan1.ZamYap()

print("yeni maas: ",calisan1.maas) #yeni maas:  280.0

print(calisan1.counter) #classta yaratılan kaçıncı obje olduğu anlaşılır.

calisan2 = Calisan("utku","acar",100)

print(calisan2.counter) #2

print(Calisan.counter) #classta kaç tane obje olduğu anlaşılır.

calisan3 = Calisan("ali","acar",200)
calisan4 = Calisan("sevval","ilhan",300)

#yaratılan objeler bir listenin içerisinde tutulabilir.

liste = [calisan1,calisan2,calisan3,calisan4]

max_maas = -1 

index=-1

for each in liste: #buradaki each bir indekstir.
    if(each.maas > max_maas):
        max_maas=each.maas
        index = each #index burada tutulur.

print(max_maas) #300
print(index.isim) #sevval -> max maas olan kişinin ismini yazdırır.