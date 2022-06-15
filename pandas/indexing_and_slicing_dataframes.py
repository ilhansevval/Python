# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 00:44:32 2022

@author: ŞEVVAL
"""

#indexing and slicing dataframes

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

print(dataframe["NAME"]) #sadece name sütunu alındı.
#0    Sevval
#1     Nazli
#2      Utku
#3       Ali
#4      Ayse
#5     Fatma
#Name: NAME, dtype: object

print(dataframe.NAME) #NAME sütununu almak için farklı bir yöntem.

dataframe["yeni_feature"] = [-1,-2,-3,-4,-5,-6]
#yeni_feature adında dataframe'e yeni bir column eklendi.
#feature adı tanımlarken boşluk bırakılmamalı

print(dataframe.yeni_feature)

print(dataframe.loc[:,"AGE"]) #AGE sütununun tüm satırları seçilir.

print(dataframe.loc[:3,"AGE"]) #ilk 4 satır verilir.
#pandasta başlangıç da bitiş de inclusivedir.

print(dataframe.loc[:3,"NAME":"SALARY"]) #NAME, AGE, SALARY sütunlarının ilk 4 satırı yazıldı.

print(dataframe.loc[::-1,:]) #tüm sütunların tüm satırlarını tersten yazdırır.

print(dataframe.loc[:,:"AGE"]) #ilk sütundaki başlayıp AGE sütunu da inclusive olmak üzere tüm satırları yazdırır.

#iloc integer location demektir, sütunun indexini yazmak gerekir.
#loc location demektir, obje alabilir.

print(dataframe.iloc[:,2]) #salary sütununun tüm satırları alınır.