# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 23:39:50 2022

@author: ŞEVVAL
"""

#filtering

#burada amaç boolean seriler yaratmaktır.
#boolean True ya da False demektir.
#int = 10 -> integer bu şekilde tanımlanır.
#str = "aaa" -> string bu şekilde tanımlanır.
#bool = True -> boolean bu şekilde tanımlanır. 

#belli başlı kurallar dataframe'in içerisinde verinin filtrelemesi yapılır.

import pandas as pd #pandas import edilip içerisindeki methodlar pd kısaltmasıyla kullanılır.

dictionary = {"NAME":["Sevval","Nazli","Utku","Ali","Ayse","Fatma"],
              "AGE":[22,3,5,3,88,99],
              "SALARY":[100,150,200,250,300,350]} #dictionary oluşturuldu.

dataframe = pd.DataFrame(dictionary) #dictionary dataframe'e dönüştürüldü.
#     NAME  AGE  SALARY
#0  Sevval   22     100
#1   Nazli    3     150
#2    Utku    5     200
#3     Ali    3     250
#4    Ayse   88     300
#5   Fatma   99     350

filtre1 = dataframe.SALARY > 200 #maaşı 200 liradan büyük olanları verir, sonuçlar true/false olarak yazılır.
#0    False
#1    False
#2    False
#3     True
#4     True
#5     True
#Name: SALARY, dtype: bool

type(filtre1) #pandas.core.series.Series
#pandas serie elde edilmiştir.
#numpy'da tek düz bloğa vector denirken pandasta serie denir.

filtrelenmis_data = dataframe[filtre1] #maaşı 200'den büyük olanlarla bir dataframe oluşturuldu.

filtre2= dataframe.AGE > 20 #yaşı 20'den küçük olanlarla boolean series oluşturuldu.

dataframe[filtre1 & filtre2] #filtre1 ve filtre2 birleştirildi.
#yaşı 20'den büyük olup maaşı 200'den fazla olanlar alındı.

#    NAME  AGE  SALARY
#4   Ayse   88     300
#5  Fatma   99     350

dataframe[dataframe.AGE > 60] #yaşı 60'dan büyük olanlar dataframe şeklinde verilir.