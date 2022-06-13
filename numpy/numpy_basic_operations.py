# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:27:04 2022

@author: ŞEVVAL
"""

#numpy basic operations

import numpy as np

a= np.array([1,2,3])
b= np.array([4,5,6]) #toplama çıkarma gibi işlemlerde boyutlarının aynı olması önemlidir.

print(a+b) #[5 7 9]
print(a-b) #[-3 -3 -3]
print(a**2) #[1 4 9]

print(np.sin(a)) #a arrayinin sinüsü alınır.
                 #[0.84147098 0.90929743 0.14112001]
                 
print(a<2) #[ True False False] -> a arrayinde 2'den küçük olanlar

c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,2,3],[4,5,6]])

#element wise product
print(c*d) #[[ 1  4  9]
           #[16 25 36]]

#matrix product
a.dot(b.T) #b'nin transpose'u alınır(3*2), o şekilde matris çarpımı yapılır.
           #32

#exponential           
print(np.exp(a)) #[ 2.71828183  7.3890561  20.08553692]

e = np.random.random((5,5)) #5*5'lik 0-1 arasında random sayılardan oluşan array

e.sum() #array'in içindeki tüm değerler toplanır. 
        #11.422940221938168
        
e.max() #array'in içindeki maksimum değer bulunur.   
        #0.9861521950041183

e.min() #array'in içindeki minimum değer bulunur.   
        # 0.013287513110473048

e.sum(axis=0) #sütunları toplar.
#array([1.69428664, 2.02912223, 2.42214449, 2.29643208, 2.98095479])

e.sum(axis=1) #satırları toplar.    
#array([1.54293376, 3.05523577, 2.46029224, 2.08433014, 2.28014833])

np.sqrt(e) #arraydeki her değerin karekökü alınır.
np.square(e) #arraydeki her değerin karesi alınır.

np.add(e,e) #(e+e) işlemini add methoduyla yapar.