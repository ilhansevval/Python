# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#numpy

#numpy bir kütüphanedir. İçerisinde farklı methodlar barındırır.
#Bu kütüphane import edilerek içerisindeki methodlar kullanılır.
#İstatiksel işlemler yapmak için kullanılır.

#importing
import numpy as np #numpy kütüphanesi import edilip kısayol olarak np kullanılır.

array = np.array([1,2,3]) #numpy'ın array methodu çağrılıp array oluşturulur.
                          #1*3 vector oluşturuldu
#numpy vektör ya da matris oluşturarak matematiksel işlemleri hızlı bir şekilde yapar.

array2= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(array2.shape) #array'ın shape'ine bakılır. 
                    #(15,) -> 15'e 1'lik bir vektör
                    
a = array2.reshape(3,5) 
#oluşturulan vektör 3 satır 5 sütunluk matrise dönüştürüldü.

print("shape: ",a.shape) #(3, 5)

print("dimension: ",a.ndim) #oluşturulan matrisin boyutuna bakılır.
                            #dimension:  2

print("data type: ",a.dtype.name) #data type:  int32
#array'in içindeki verilerin datatype'larını öğrenmek için (float,string,integer) bu method kullanılır

print("size: ",a.size) #reshape'ten önceki boyutu verilir.
                       #size:  15
                       
print("type",type(a))  #type <class 'numpy.ndarray'>

array3= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #reshape yapmadan da boyutu değiştirilebilir.

print(array3) #array([[ 1,  2,  3,  4],
                     #[ 5,  6,  7,  8],
                     #[ 9, 10, 11, 12]])

print(array3.shape) #(3, 4)

zeros= np.zeros((3,4)) #3 satır 4 sütunluk sıfırlardan oluşan array yaratılır.
#bu matris ile memoryde yer ayırtılır, güncelleme yapılmak istendiğinde güncellenir.
#append gibi fonksiyonlar memory'iyi yorar ve programı yavaşlatır.
#o yüzden bu method tercih edilir.

zeros[0,0]=5
print(zeros)

np.ones((3,4)) #1'lerden oluşan 3*4'lük bir matris yaratır.

np.empty((4,5)) #boş bir array oluşturulur.

np.arange(10,50,5) #10 ve 50 arasındaki sayılar 5'er 5'er yazdırılır.
#array([10, 15, 20, 25, 30, 35, 40, 45])

a= np.linspace(0,10,20) #0 ile 10 arasında 20 tane sayı yazdırılır.
#array([ 0.        ,  0.52631579,  1.05263158,  1.57894737,  2.10526316,
#       2.63157895,  3.15789474,  3.68421053,  4.21052632,  4.73684211,
#       5.26315789,  5.78947368,  6.31578947,  6.84210526,  7.36842105,
#       7.89473684,  8.42105263,  8.94736842,  9.47368421, 10.        ])