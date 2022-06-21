# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Animal: #parent
    
    def toString():
        print("animal")
        
class Monkey(Animal): #child

    def toString():
        print("monkey")
        
a1 = Animal()
a1.toString()

m1 = Monkey() 
m1.toString() #hem parent classta hem de child classta toString methodu var.
              #monkey classı burada override methodunu çağırır.
              #javadaki gibi @override yazmaya gerek yoktur.
              
class Rectangle(): #parent
    
	def __init__(self,length,breadth):
		self.length = length
		self.breadth = breadth
        
	def getArea(self):
		print(self.length*self.breadth," is area of rectangle")
        
class Square(Rectangle): #child
    
	def __init__(self,side):
		self.side = side
		Rectangle.__init__(self,side,side)
        
	def getArea(self):
		print(self.side*self.side," is area of square")
        
s = Square(4)

r = Rectangle(2,4)

s.getArea() #square classı içindeki getArea methodu çalışır.

r.getArea() #rectangle classı içindeki getArea methodu çalışır.