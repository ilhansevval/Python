# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:03:38 2022

@author: ŞEVVAL
"""

class Square(object):
    
    edge = 5 #meter
    
    area=0
    
    def Area(self): #behaviour
                    #self ile classa ait attributelara erişim sağlanır.
        self.area = self.edge*self.edge #5*5
        #area da classın bir attribute'u olduğu için self yazılır.
        print("area: ",self.area)
    
s1 = Square()

print(s1)

print(s1.edge)

print(s1.Area())

print(s1.Area) #memoryde yarattığı yeri döndürür.

s1.edge = 7

print(s1.Area()) #class içerisinde tanımlanmış attribute değeri değiştirildi.