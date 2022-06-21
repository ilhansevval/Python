# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 22:57:06 2022

@author: ŞEVVAL
"""

class Website(object):
    "parent"
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    
    def loginInfo(self):
        print(self.name+" "+self.surname)
        

class Website1(Website):
        "child"
        def __init__(self,name,surname,ids):
            Website.__init__(self,name,surname) #super methoduyla parent classtan direkt alınan constructor
                                                #yeniden tanımlanabilir.
            self.ids=ids
            
        def login(self):
            print(self.name+" "+self.surname+" "+self.ids)
            #name ve surname parent classtan geldi.
            #ids Website1 classında oluşturuldu.
            
class Website2(Website):
    "child"
    def __init__(self,name,surname,email):
        Website.__init__(self,name,surname)
        self.email=email
    
    def login(self):
        print(self.name+" "+self.surname+" "+self.email)
            
person1 = Website("nazli","acar")

person2 = Website1("sevval", "ilhan", "123")

person3 = Website2("utku", "acar", "email")

print(person2.login()) #sevval ilhan 123 -> child classtan gelen method

print(person2.loginInfo()) #sevval ilhan -> parent classtan gelen method

print(person3.login()) #utku acar email -> child classtan gelen method

print(person3.loginInfo()) #utku acar -> parent classtan gelen method