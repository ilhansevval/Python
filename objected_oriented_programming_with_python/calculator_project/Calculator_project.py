# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:45:14 2022

@author: ŞEVVAL
"""

class Calculator(object):
    "calculator"
    #init methodu(constructor)
    def __init__(self,a,b):
        "initialize values"
        
        #attributes
        self.value1 = a
        self.value2 = b
        
    
    def Add(self):
        "addition a+b = result -> return result"
        result= self.value1 + self.value2 
        return result
    
    def Sub(self):
        "substraction a-b = result -> return result"
        result= self.value1 - self.value2 
        return result
    
    def Multiply(self):
        "multiplication a*b = result -> return result"
        result= self.value1 * self.value2 
        return result
    
    def Div(self):
        "division a/b = result -> return result"
        result= self.value1 / self.value2 
        return result


print("Choose addition(1), substraction(2), multiplication(3), division(4)")
selection = input("select 1,2,3,4: ") #consoledan input almak için gerekli olan method inputtur.
                                   #alınan input selectiona eşitlenir.
                                   
v1 = int(input("First value: "))   #klavyeden girilen değer string olduğu için integera çevirdi.
v2 = int(input("Second value: "))
    
c1 = Calculator(v1,v2)

if selection == "1":

    add_result = c1.Add()
    print ("Addition: {} ".format(add_result))
    
elif selection == "2":

    substraction_result = c1.Sub()
    print ("Substraction: {} ".format(substraction_result))

elif selection == "3":

    multiply_result = c1.Multiply()
    print ("Multiply: {} ".format(multiply_result))  
    
elif selection == "4":

    division_result = c1.Div()
    print ("Division: {} ".format(division_result))
    
else:
    print("----Wrong Selection----")