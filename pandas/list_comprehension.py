# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 00:14:25 2022

@author: ŞEVVAL
"""

#list comprehension

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

mean_salary = dataframe.SALARY.mean() #salary sütununun ortalaması verilir. (225.0)

import numpy as np

mean_salary_np = np.mean(dataframe.SALARY) #mean methoduyla numpy'da da sütunların ortalaması hesaplanabilir.

dataframe["Salary_Level"] = [ "low" if mean_salary > each else "high" for each in dataframe.SALARY]
#maaşı ortalamadan yüksek olanlar high, düşük olanlar low olarak sınıflandırıldı
#bunlar için yeni bir feature oluşturuldu

dataframe.columns = [ each.lower() for each in dataframe.columns]
#lower methodu stringleri küçük harfe çevirir.
#burada for each ile tüm columnlar dönülür ve küçük harfe çevrilir.

dataframe.columns = [ each.split()[0] + "_" + each.split()[1] if (len(each.split())>1) else each for each in dataframe.columns]
#eğer column isimlerinde boşluk varsa onlar _ ile birleştirilir, yoksa devam edilir.