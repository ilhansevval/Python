# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:12:13 2022

@author: ŞEVVAL
"""

#convert and copy array

import numpy as np

liste = [1,2,3,4]

array = np.array([5,6,7,8])
#array tanımlamak için array'in içine liste yazılır.

array = np.array(liste)

liste2 = list(array) #arrayden listeye geçilir.

a = np.array([1,2,3])

b=a

c=a

b[0]=5 #bu örnekte a,b,c arraylerinin hepsinin 0. indeksi değişir.
#bunun sebebi np.array memory'de bir değer olarak değil bir alan olarak depolanır.
#a,b,c için memory aynı alan ayrıldığından bir tanesi değiştirilince hepsi değişir.

d = a.copy() #copy methoduyla memory yeni bir alan tahsis edilir.
#böylelikle birinin bir indeksi değişince diğerleri bundan etkilenmez.