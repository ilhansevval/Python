# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 03:31:28 2022

@author: ŞEVVAL
"""

#concatenating data

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

mean_salary = dataframe.SALARY.mean()

dataframe["Salary_Level"] = [ "low" if mean_salary > each else "high" for each in dataframe.SALARY]

dataframe.drop(["Salary_Level"],axis=1) #Salary_Level sütunu dataframeden kaldırıldı.
#axis=1 demek yukarıdan aşağı yani sütun drop et demektir.
#axis=0 demek soldan sağa yani satır drop et demektir.

#inplace=1 demek kaldırılan sütun ya da satırı dataframe'de güncelle demektir.
#eğer inplace=1 yapılmazsa yapılan değişiklik dataframe'e kaydedilmeyecektir.

dataframe.drop(["Salary_Level"],axis=1, inplace=True)

dataframe = dataframe.drop(["Salary_Level"],axis=1) #inplace=True'nun yaptığını yapar.

#concatenating birleştirmek demektir. numpy'daki hstack, vstack mantığıyla çalışır.
#iki dataframe'i birleştirir.

data1 = dataframe.head()
data2 = dataframe.tail()

#vertical

data_vertical_concat = pd.concat([data1,data2],axis=0)
#iki dataframe yukarıdan aşağı olacak şekilde birleştirildi.

#horizontal

salary = dataframe.SALARY

age = dataframe.AGE

data_horizontal_concat = pd.concat([salary,age],axis=1)