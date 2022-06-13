# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:43:47 2022

@author: ŞEVVAL
"""

#shape manipulation

import numpy as np

array = np.array([[1,2,3],[4,5,6],[7,8,9]]) #3*3'lük array oluşturuldu.

#flatten 
#arrayler tek boyutlu hale getirilir.
#deep learning conventional neural network'te bu yöntem sıklıkla kullanılır.

a = array.ravel() #ravel methoduyla tek boyutlu hale getirilir.

array2 = a.reshape(3,3) #tekrardan 3*3'lük array haline getirildi.

array_transpose = array2.T #array'in transpose'u alınır.
                           #array([[1, 4, 7],
                                  #[2, 5, 8],
                                  #[3, 6, 9]])
                
array3 = np.array([[1,2],[3,4],[5,6]])

array3.resize((2,3)) #resize ile yapılan boyut değişimleri kalıcıdır, aynı array'in içine kaydeder.
#reshape ile yapılan değişimler kalıcı değildir. yapılan değişim başka bir değişkene kaydedilmelidir.