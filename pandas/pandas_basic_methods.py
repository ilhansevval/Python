# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 00:21:35 2022

@author: ŞEVVAL
"""

#pandas basic methods

import pandas as pd

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

print(dataframe.columns) #column isimleri verilir.
#Index(['NAME', 'AGE', 'SALARY'], dtype='object')
#column isimlerine göre filtreleme ya da değişiklik yapılmak istendiğinde bakılır.

print(dataframe.info()) 
#dataframe'in pandas dataframe'i olduğunu gösterir.
#içerisinde 6 sample var (0'dan 5'e kadar)
#toplamda 3 datacolumn olduğunu gösterir.
#columnların missing data olmayan veri sayısını ve bu verilerin türünü gösterir.
#pandasta string datatype object olarak adlandırılır.
#memory kullanımını da gösterir.

print(dataframe.dtypes) #bu methodla columnların sadece datatype'ı hakkında bilgi verilir.

print(dataframe.describe()) 
#describe methodu sadece sayısal değer barındıran columnları alır.
#count ile her bir columnun kaç tane satır olduğu gösterilir.
#mean ile columnların ortalaması verilir.
#sütunlardaki min ve max değerleri gösterilir.