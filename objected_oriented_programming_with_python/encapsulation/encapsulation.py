# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:24:12 2022

@author: ŞEVVAL
"""

#encapsulation method ya da variablelara erişimi kısıtlamak demektir.
#herhangi bir nesnenin methodlarını, verilerini ve değişkenlerini diğer nesnelerden saklayarak
#ve bunlara erişimi sınırlandırarak yanlış kullanımdan koruma konseptidir.

class BankAccount(object):
    
    def __init__(self,name, money, address):
        
        self.name=name #public variable
        self.__money=money #javada değişken private money diye tanımlanırken pythonda __money şeklinde tanımlanır.
        self.address=address
        
    def getMoney(self): #get methodu ile classın içerisine erişim sağlanır.
            return self.__money
        
    def setMoney(self,amount): #set methodu ile classın içerisindeki değer değiştirilir.
            self.__money = amount
            
    def __increase(self): #methodlar da '__' ile private yapılabilir.
        self.__money = self.__money + 500
        
person1 = BankAccount("Sevval", 100, "Istanbul")
person2 = BankAccount("Utku", 150, "Balıkesir")

print(person1.getMoney()) #money attribute'u private olduğu için get methodu ile erişim sağlanır.

person2.setMoney(200)  #set methodu ile money değeri değiştirildi.
print(person2.getMoney())

person1.__increase()  #increase methodu private olduğu için erişim sağlayamaz
print(person1.getMoney())