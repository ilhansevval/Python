# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 23:34:40 2022

@author: ŞEVVAL
"""

#introduction to pandas

#numpy kütüphanesi arraylerle yapılan matematiksel işlemlerde, depolamada kullanılır.
#pandas kütüphanesi dataframe olarak tabir edilen yapılan için oluşturulmuş kütüphanedir.
#pandas dataframeleri kullanmak için hızlı ve etkili bir kütüphanedir.
#dataframeler datayı içinde depoladığımız yapılardır.
#pandas kütüphanesi ile dosyalar arası geçiş kolaylaşır.
#csv ve text dosyaları üzerinde işlem yapılıp, sonuçlar tekrardan kaydedilebilir.
#datanın içinde missing valuelar olabilir, pandas ile bunlara çözüm üretilir.
#numpy'da yapılan reshape gibi methodlar pandasda datayı çok daha etkili bir şekilde kullanmayı sağlar.
#pandas ile slicing ve indexing yapılabilir. (25 yaşından büyük bireyleri seç gibi)
#time series data -> zaman depended {Ankara'dan İstanbul'a gelen arabanın hız değişimi}
#en önemlisi pandas optimize edilmiş hızlı bir kütüphanedir.

import pandas as pd #pandas import edilip içerisindeki methodlar pd kısaltmasıyla kullanılır.

dictionary = {"NAME":["Sevval","Nazli","Utku","Ali","Ayse","Fatma"],
              "AGE":[22,3,5,3,88,99],
              "SALARY":[100,150,200,250,300,350]} #dictionary oluşturuldu.
#keys: NAME, AGE, SALARY
#values: Sevval,Nazli,Utku,Ali,Ayse,Fatma,22,3,5,3,88,99,100,150,200,250,300,350

#{'NAME': ['Sevval', 'Nazli', 'Utku', 'Ali', 'Ayse', 'Fatma'],
# 'AGE': [22, 3, 5, 3, 88, 99],
# 'SALARY': [100, 150, 200, 250, 300, 350]}

dataframe = pd.DataFrame(dictionary) #dictionary dataframe'e dönüştürüldü.
#     NAME  AGE  SALARY
#0  Sevval   22     100
#1   Nazli    3     150
#2    Utku    5     200
#3     Ali    3     250
#4    Ayse   88     300
#5   Fatma   99     350

head = dataframe.head() #dataframe'in içindeki ilk 5 satır verilir.
#data dışarıdan yüklendiğinde içeriğinde ne olduğunu görmek için head methodu kullanılır.
#head methodu bir ön inceleme yapılmasını sağlar.

tail = dataframe.tail() #dataframe'deki son 5 satırı verir.

head = dataframe.head(6) #ilk 6 satır
#head methodunun içi boş kalırsa ilk 5 satır verilir, içerisine değer yazarak bunu değiştirebiliriz.