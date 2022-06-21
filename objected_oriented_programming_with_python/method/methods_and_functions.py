# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 17:24:52 2022

@author: ŞEVVAL
"""

class Employee():
    
    age=22
    
    salary=1000 # $
    
    def ageSalaryRatio(self): #method
        print(self.age / self.salary)
        
def ageSalaryRatio(age,salary): #function
    print(age / salary)
    
#method self adında bir parametreye sahiptir. 
#bu parametreyle classın içinden değerleri alır.
#methodlar class içerisinde tanımlanır, functionlar class dışında tanımlanır.
#fonksiyonun class ile bir ilgisi yoktur.

    
employee1 = Employee() 

print(employee1.ageSalaryRatio())  #0.022 classın içerisindeki method kullanılır.

print(ageSalaryRatio(30, 2000))    #fonksiyonun değerleri bir yerden gelmeyeceği için içine yazılır.



def findArea(pi,r):
    area=pi*r**2
    print(area)
    return area #findArea fonksiyonunun sonucunda çıkan değer döndürülür.

pi = 3.14

r = 5

result1 = findArea(pi,r) #3,14 ve 5 olarak tanımlanan değerlerdir, fonksiyonun içerisindeki parametreler değildir.

result2 = findArea(pi,10)

print(result1+result2) #(78.5+314.0)=392.5