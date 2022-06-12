# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 15:04:33 2022

@author: ŞEVVAL
"""

#conditionals
#if else statement

1 == 1 #True

1 == 2 #False

1 != 1 #False

True == True #True

True == False #False

1>0 and 4<5 #True

1>0 or 4<3 #True (tek durumun doğru olması yeterli)

var1=10
var2=20

if (var1 > var2):
    
    print("var 1 büyüktür var 2'den")
    
elif (var1 == var2):
    print("var1 eşittir var2")
    
else :
    
    print("var1 küçüktür var2'den")
    

liste =[1,2,3,4,5]

if 6 in liste:
    
    print("6 listenin içindedir.")
    
else:
    print("6 listenin içinde değildir.")
    

value = 3

if value in liste:
    
    print("value değeri {} listenin içindedir.".format(value))
    
else:
    print("value değeri {} listenin içinde değildir.".format(value))
    

dictionary = {"sevval":22, "utku":6, "nazli":3}

keys = dictionary.keys() #dictionary'nin keyleri keys variable'ına eşitlendi.

if "sevval" in keys: #sevval keylerin içindeyse evet, değilse hayır yazılır.
    
    print("evet")

else:
    print("hayır")
    


# 1650. yıl = 17. yüzyıl
# 109.yıl = 2.yüzyıl
# input = integer (yıllar)
# output = integer (yüzyıl)
# MÖ ve 2005'ten sonrası yok
# input = year -->  1 <= year <= 2005

def year2Century (year):
    
    """
    from year to century 
    """
    
    str_year = str(year) #yıl stringe çevrildi, str_year variable'ının içinde depolandı.
    
    if (len(str_year)<3): #1. yüzyıl yılları 1-99 arasındadır.
        
        return 1
    
    elif(len(str_year)==3): #yıllar 100-999 arası seçilmiştir.
        
        if(str_year[1:3] == "00"):#eğer son iki hanesi 00 ise -->>> 100,200
        
            return int(str_year[0]) #bu problemde yüzyıl artırılmıyor.
        
        else:
            
            return int(str_year[0])+1 #101,251,343 olduğunda yüzyıl 1 artırılır.
    
    else: #1700, 1750
    
        if (str_year[2:4] == "00"): #1700 ise ilk iki rakam döndürülür.
            
            return int(str_year[:2])
        
        else:   #1701, 1945
        
            return int(str_year[:2])+1
            

year2Century(2000) #20
year2Century(1999) #20