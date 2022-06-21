# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:51:14 2022

@author: ŞEVVAL
"""

#integer = 10
#string = "asd"

integer1 = 22

string1 = "sevval"

#Bir şirket olduğunu düşünürsek;
#burada çalışanların yaşı, ev adresi, ismi, soyismi gibi genel bilgiler vardır.

employee1_name = "sevval"
employee1_age = 22
employee1_location = "Istanbul" 

#bir çalışanın bilgileri bu şekilde tutulur.
#Ancak bu şirkette 1000 çalışan olursa hepsi tek tek değişken tanımlanamaz.
#Bu ortak bilgiler oluşturulan classın constructor'ında tutulur.

class Employee(object): #object Employee classının içerisinde oluşan bir nesnedir.
    #attribute = name, surname, age
    #behaviour = yapabildikleri
    pass #boş bir class olduğunda programın hata vermemesi için pass yazılır.
    
employee1 = Employee() #employee1 adlı obje yaratıldı.