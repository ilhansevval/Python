# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:05:30 2022

@author: ŞEVVAL
"""

#user defined functions

var1=100
var2=99

output=((var1+var2)*50)/100.0*var1/var2

#fonksiyon parametresi var1 var2'dir
def func(var1,var2): #yazılan output denklemi fonksiyona çevrilir.
    
    """
    
    func
    
    parametre: int - var1, int - var2
    
    return: int - output
    
    """
    output=((var1+var2)*50)/100.0*var1/var2
    
    return output

func(1,2) #var1=1 var2=2 atanır ve denklemdeki işlem yapılır. Sonuç 0.75 

#boş fonksiyon

def bos():
    pass

#eğer parametre fonksiyonun içerisinde global olarak tanımlanırsa fonksiyonun dışında da kullanılabilir.
katsayi = 5

def katsayi_carpim():
    global katsayi
    print(katsayi*katsayi)
    
katsayi_carpim()
print(katsayi)