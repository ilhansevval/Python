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
    
    parametre:
    
    return:
    
    """
    output=((var1+var2)*50)/100.0*var1/var2
    
    return output

func(1,2) #var1=1 var2=2 atanır ve denklemdeki işlem yapılır. Sonuç 0.75 