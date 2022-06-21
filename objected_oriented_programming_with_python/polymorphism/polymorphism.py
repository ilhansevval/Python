# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 01:47:48 2022

@author: ŞEVVAL
"""

#polymorphism parent classtan child classa aktarılan ancak child classta farklı şekilde kullanılan methodlardır.
#Polymorphism ile programın güncellenmesi kolaylaşır.

class Employee():
    
    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100 * raise_rate
        print("Employee: ",result)
    
class compEng(Employee):
    
    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100 * raise_rate
        print("Computer Engineer: ",result)
    
class mechEng(Employee):
    
    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print("Mechatronics Engineer: ",result)

employee1 = Employee()

ceng = compEng()

mecheng = mechEng()

Employeelist = [ceng,mecheng]

for employee in Employeelist: #for each döngüsüyle objeler teker teker yazdırılır.
    employee.raisee()  #Computer Engineer:  120.0
                       #Mechatronics Engineer:  130.0