# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:38:20 2022

@author: ŞEVVAL
"""

#indexing and slicing

import numpy as np

#arraylerde saymaya sıfırdan başlanır.

a= np.array([1,2,3,4,5,6,7]) #vektor -> dimension 1

print(a[0]) #arraydeki 1 sayısını verir.

print(a[0:4]) #ilk 4 indeksi yazdırır.

reverse_array = a[::-1] #array'i ters çevirir.

b = np.array([[1,2,3,4,5],[6,7,8,9,10]]) #2 boyutlu array oluşturuldu.

print(b[1,1]) #1.satır 1.sütundaki değer olan 7'yi verir.

print(b[:,1]) #satırların hepsini ve 1. sütunu verir. [2 7]

print(b[1,:]) #1.satırdaki sütunların tamamını verir. [ 6  7  8  9 10]

print(b[1,1:4]) #1.satır 1. 2. 3. sütunları verir. [7 8 9]

print(b[-1,:]) #son satır ve tüm sütunları alır. [ 6  7  8  9 10]

print(b[:,-1]) #son sütun ve tüm satırlari alır. [ 5 10]