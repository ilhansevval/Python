# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:51:30 2022

@author: ŞEVVAL
"""

class Animal(object):
    #classa her bir hayvan tanımlandığında name ve age attributelarını elle değiştirmek mantıklı değildir.
    #bunun için tüm hayvanların özelliklerinin ortak olarak sahip olduğu bir constructor yaratılır.
    
    def __init__(self,name,age): #pythonda constructor oluştururken javadan farklı olarak init methodu kullanılır.
                    #init initialize demektir.
                    #init methodu ile attributelar tanımlanır.
        self.name = name
        
        self.age = age
    
    
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
animal1 = Animal("dog",2) #name ve age constructordan geldiği için obje oluştururken değerler içerisine yazılır.

print(animal1.age)

print(animal1.getAge) #bir method olduğundan değerin gözükmesi için parantez kullanılması gerekir.
                      #kullanılmazsa memory'de kapladığı alanı yazdırır.
                      
animal2 = Animal("bird",3)

animal3 = Animal("dog",4)

print("name: ",animal3.getName())