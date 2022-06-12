# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:07:53 2022

@author: ŞEVVAL
"""

#string

s="bugün günlerden pazartesi"

variable_type = type(s) 

# type bir functiondır.
# Bu functionın içine variable adı verildiğinde bu variable'ın türünü gösterir.
# str sonucunu döndürür. str de stringin kısaltmasıdır.
# integer bir variable için int döndürür.

print(s) #yazdırmak için print fonksiyonu kullanılır.

var1="ankara"
var2="istanbul"
var3=var1+var2 # 'ankaraistanbul' sonucunu yazdırır.

var4="100"
var5="200"
var6=var4+var5 #sayılar string olarak tanımlandığından 300 değil '100200' sonucunu yazdırır.

uzunluk= len(var6) #variable uzunluğu len methoduyla gösterilir.

var6[0] #var6 variable'ının 0. indeksi gösterilir.