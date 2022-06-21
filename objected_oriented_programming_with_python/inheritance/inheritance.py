# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:04:16 2022

@author: ŞEVVAL
"""

#inheritance(miras) daha önceden oluşturulmuş bir classın özelliklerini ya da methodlarını kullanarak
#yeni bir class yaratma işlemidir.

#inheritance'ta iki farklı class yapısı vardır. -> parent ve child
#child class parent classın attributelarını ya methodlarını kullanabilen bir alt classtır.


#parent class
class Animal(object):
    
    def __init__(self):
        print("animal created")
        
    def toString(self):
        print(Animal)
        
    def walk(self):
        print("animal is walking")
        
class Monkey(Animal): #Animal classından türetildiği için classın içine Animal yazılır.
                      #javada miras alma class Monkey extends Animal şeklinde yapılırken
                      #pythonda miras alınan class bu şekilde yazılır.
    def __init__(self):
        super().__init__() #parent classının constructorı child classa aktarılır.
        print("monkey created")
        
    def toString(self):
        print("monkey")
        
    def climb(self):
        print("monkey is climbing")
        
class Bird(Animal):
    
    def __init__(self):
        super().__init__() #parent classının constructorı child classa aktarılır.
        print("bird created")
        
    def toString(self):
        print("bird")
        
    def fly(self):
        print("bird is flying")
    
        
m1 = Monkey() #animal created -> animal classından miras alındığı için bu print çalıştı.
              #monkey created
m1.toString() #monkey

m1.walk() #walk methodu animal classından miras alınır. animal is walking yazar.

m1.climb()


b1 = Bird() #animal created -> animal classından miras alır.
            #bird created

b1.walk()  #animal is walking -> walk methodu animal classından miras alındı.

b1.fly()  #bird is flying