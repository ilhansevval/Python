# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 16:18:57 2022

@author: ŞEVVAL
"""

#for_loop

"""
döngüler bir dizi üzerinde yineleme yapmak için kullanılan yapılardır.

"""

for each in range (1,11): #1 -> inclusive, 11 -> exclusive
    
    print(each) 

for each in "ankara istanbul":
    
    print(each)
    
#a
#n
#k
#a
#r
#a
 
#i
#s
#t
#a
#n
#b
#u
#l

#stringleri harf harf yazdırır.

for each in "ankara istanbul".split():
    
    print(each) #split methoduyla kelime kelime ayrılır.
    
    
liste= [1,4,6,8,3,5,9,2,43,57]
sum(liste) #liste sum methoduyla kolay yoldan toplanabilir.

count = 0

for each in liste:
    
    count = count + each #count değeri ilk başta 0, listede her eleman tek tek eklenip toplam sonucu bulunur.
    
    print(count) #count sonucu her liste elemanı eklendiğinde yazdırılır.
    
    
liste1=[1,2,3,4,5,6,-500,23,451,67,21,23]  
min(liste1)  #listedeki en küçük eleman min methoduyla bulunur.
             #aynı işlem for döngüsüyle de yapılabilir.
             
minimum=100000

for each in liste1:
    
    if(each<minimum):
        
        minimum=each
        
    else:
        
        continue #else durumunda hiçbir şey yapmadan devam edilir.
        
print(minimum)          