# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 02:13:14 2022

@author: ŞEVVAL
"""

#lambda function
#Amaç daha hızlı bir şekilde fonksiyon yazabilmektir.

def hesapla(x):
    
    output= x*x
    
    return output

sonuc = hesapla(3)

sonuc2 = lambda x: x*x 

print(sonuc2(3)) 

#iki fonksiyonda da x'in karesi hesaplanır. lambda ile daha kısa bir yazım olur.

y = 3

z = lambda x:x*y

z(3) #9