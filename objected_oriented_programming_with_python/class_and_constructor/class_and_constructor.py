# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 13:40:37 2022

@author: ŞEVVAL
"""

class Calisan(): #Calisan class'ı

    def __init__(self,isim,soyisim,maas): #Constructor
        self.isim=isim #Constructor'da java'da this kullanılırken python'da self kullanılır.
                       #self Calisan class'ından gelen ismi constructordan gelen isme eşitler.
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@gmail.com"
        #bütün çalışanların ismi,soyismi,maaşı,emaili olacağı bellidir.
        #bu değişkenleri her çalışan için tek tek tanımlamak yerine Constructor yapısı kullanılır.
        
        
    def GiveNameSurname(self):
        return self.isim + " "+self.soyisim
        #Constructordaki self.isim classtan gelen isme eşitlenir.
        #eşitlenen isim methodda çağırılır.
    
    
isci1 = Calisan("ali","acar",100)

print(isci1.isim) #ali

print(isci1.email) #aliacar@gmail.com

print(isci1.maas) #100

print(isci1.GiveNameSurname()) #ali acar