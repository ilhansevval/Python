# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:34:35 2022

@author: ŞEVVAL
"""

#while_loop

"""
döngüler bir dizi üzerinde yineleme yapmak için kullanılan yapılardır.

"""

#while loop'ta bir condition vardır.

i=0 

while (i<4):
    
    print(i)
    
    i = i+1 #i=4 olana kadar yazdırır. (0,1,2,3)
#eğer i artırılmazsa 0 hiçbir zaman 4'ten büyük olmayacağı için sonsuz döngüye girer.
    

liste = [1,2,3,4,7,9,5,8,6,0]
    
sinir=len(liste)

each=0

count=0

while (each<sinir):
    
    count=count+liste[each]
    
    each=each+1    
    
    print(count) 
    #burada listenin her elemanı count'a eklenir, eklendikten sonra bir sonraki elemana geçer.
    #böylece toplama yapılmış olur.
    #count'a her sayı eklendiğinde toplam yazılır.