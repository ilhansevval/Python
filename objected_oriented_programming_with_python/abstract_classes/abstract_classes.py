# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:31:33 2022

@author: ŞEVVAL
"""

#abstract classlar child classlar için şablon görevi görürler.
#kullanılacak ortak fonksiyonları kendi içlerinde tutarlar.

from abc import ABC, abstractmethod

class Animal (ABC):
    
    @abstractmethod #parent class
    def walk(self):
        pass
    @abstractmethod
    def run(self):
        pass
    
class Bird(Animal):  #child class
    def __init__(self):
        print("bird")
        
    def walk(self):
        print("walk")
    
    def run(self):
        print("run")

#abstract classlar instantiated edilemez.yani;
#a = Animal() -> abstract class için yazılamaz, animal classından obje yaratılamaz.

#abstract classta kullanılan method child classta kullanılmak zorundadır.

b1 = Bird() #bird yazdırır.