# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:23:38 2022

@author: ŞEVVAL
"""

#list
#her bir integer,string değeri için bir variable oluşturmak yerine bir list oluşturulur.
#list string,integer,float gibi bir datatype'dır.

var1=10
var2=20
var3=30

list_int=[1,2,3,4,5,6] #her bir variable listenin içine yerleştirilir.
type(list_int) #type listenin içindeki değer değil listenin kendisidir. list gözükür.

list_str=["pazartesi","salı","carsamba"] #liste string değerler de alabilir.
type(list_str)

value = list_int[0] 
print(value) #listenin 0. indeksi 1 olduğundan 1 yazdırılır.

value1 = list_int[-1] 
print(value1) #listede çok eleman olduğunda ve kaç eleman olduğu sayılmıyorsa sonuncu eleman bu şekilde yazdırılır.

list_divide= list_int[0:3] #listenin ilk 3 elemanı yazdırılır. 0'dan 3'e kadar
print(list_divide)

#listenin de kendi built_in_functionları vardır.
dir(list_int) #liste ile kullanılabilecek methodlar yazdırılır.

help(list.append) #append methodunun ne işe yaradığını gösterir.

list_int.append(7) #7'yi listenin sonuna ekler.

list_int.remove(7) #7 listeden çıkartılır.

list_int.reverse(7) #listeyi ters çevirir.

list_yeni=[3,5,2,6,1,4]
list_yeni.sort()

string_int_list=["sevval","ilhan",15,1,2000] #liste string ve integer değer birlikte alabilir.