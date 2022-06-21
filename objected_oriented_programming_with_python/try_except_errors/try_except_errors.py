# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:05:51 2022

@author: ŞEVVAL
"""

#exceptions

a = 10

b = "2"

liste = [1,2,3,4]

print(sum(liste))

print(a+b) #integer bir sayı ile string bir değer toplandığından hata verir.

print(a+int(b)) #b değeri integera çevrilirse hata çözülür.


print(k) #k adında bir değişken tanımlanmadığından yazdırılamaz.

c=10 

zero=0

e=c/zero #bir sayının sıfıra bölümü tanımsızdır.

if(zero==0):
    e=0
    
else:
    e=c/zero
    
try:
    e=c/zero
except ZeroDivisionError:
    e=0
    
#index error

list1 = [1,2,3,4]
list1[15] #listenin 15. elemanına erişemez, bu yüzden index error verir.

#module not found
import numpyy #modülün ismi yanlış yazıldığından module not found hatası verir.

#file not found error

import pandas as pd

pd.read_csv("asd") #csv formatında bir dosya import edilmek istenmiştir.
                   #asd diye bir dosya olmadığından file not found error verir.
                   
#type error

"2" + 2 #bir string ile bir integer toplanamayacağından type error verir.

#value error

int("asd") #integera çevrilecek bir değer girilmediğinden value error verir.

try:
    1/0
except:
    print("else")
else:
    print("else")
finally:
    print("done") #finally methodu hatanın olup olmadığına bakmaz, her koşulda çalışır.