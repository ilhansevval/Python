# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 14:44:10 2022

@author: ŞEVVAL
"""

#pandas_review

#csv dosyalarında veriler virgüller ile ayrılmıştır.
#csv comma separated values demektir.

#matplotlib kütüphanesi görselleştirme için kullanılır.


import pandas as pd

df = pd.read_csv("C:/Users/ŞEVVAL/Desktop/machine_learning/python_for_artificial_intelligence/visualization_with_matplotlib/data/iris.csv")
#iris.csv datası dataframe'e çevrilip içindekiler öğrenilir.

#iris bir çiçek ve bu çiçeğin versicolor, setosa, virginica olmak üzere 3 farklı türü var.
#bu datadaki özellikler anlaşılmaya çalışılacaktır.

print(df.columns)
#Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm','Species'],
      #dtype='object') -> bunlar featurelardır.
      
#dataframe'de 150 sample vardır.
#bu samplelar arasından kaç farklı tür olduğu anlaşılacaktır.
print(df.Species.unique()) #unique methoduyla kaç farklı tür olduğu bulunacaktır.

print(df.info()) 
#dataframe 150 sample'dan oluşur.
#id sütunu integer, species sütunu string, uzunluk sütunları float değer içerir.

print(df.describe()) #string olmayan sayısal değerleri karşılaştırmaya yarar.

setosa = df[ df.Species == "Iris-setosa"] 
#setosa türünün ayrıldığı bir dataframe oluşturuldu.

versicolor = df[ df.Species == "Iris-versicolor"] 
#versicolor türünün ayrıldığı bir dataframe oluşturuldu.

print(setosa.describe())
print(versicolor.describe())
#iki farklı türün uzunlukları ayrı ayrı karşılaştırıldı.