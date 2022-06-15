# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 04:00:47 2022

@author: ŞEVVAL
"""

#transforming data

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

dataframe["list_comp"] = [ each*2 for each in dataframe.AGE] 
#list_comp adında yeni bir sütun oluşturulup, age sütunundakilerin 2 katı bu sütuna yazılır.

#apply()

def multiply(age):
    return age*2

dataframe["apply_method"] = dataframe.AGE.apply(multiply)

#     NAME  AGE  SALARY  apply_method  list_comp
#0  Sevval   22     100            44         44
#1   Nazli    3     150             6          6
#2    Utku    5     200            10         10
#3     Ali    3     250             6          6
#4    Ayse   88     300           176        176
#5   Fatma   99     350           198        198