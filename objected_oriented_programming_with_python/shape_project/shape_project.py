# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 02:23:50 2022

@author: ŞEVVAL
"""

from abc import ABC, abstractmethod

#inheritance
class shape(ABC):
    """
    Shape = parent class / abstract class
    """
    #abstract method
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    #override and polymorphism
    def toString(self):
        pass

class square(shape):
    "child class"
    def __init__(self,edge): #constructor
        self.__edge = edge #encapsulation -> private attribute
        
    def area(self):
        result = self.__edge**2
        print("square area: ",result)
        
    def perimeter(self):
        result = self.__edge*4
        print("square perimeter: ",result)
        
    #override and polymorphism
    def toString(self):
        print("square edge",self.__edge)
        
        
class circle(shape):
    "child class"
    
    #constant variable
    PI = 3.14
    
    def __init__(self,radius): #constructor
        self.__radius = radius #encapsulation
        
    def area(self):
        result = self.PI*self.__radius**2 #pi*r^2
        print("circle area: ",result)
        
    def perimeter(self):
        result = 2*self.PI*self.__radius*4  #2*pi*r
        print("circle perimeter: ",result)
    
    #override and polymorphism
    def toString(self):
        print("circle radius",self.__radius)
        
c = circle(5)
print(c.area()) #circle area:  78.5
print(c.perimeter()) #circle perimeter:  125.60000000000001
print(c.toString()) #circle radius 5

s = square (4)
print(s.area()) #square area:  16
print(s.perimeter()) #square perimeter:  16
print(s.toString()) #square edge 4