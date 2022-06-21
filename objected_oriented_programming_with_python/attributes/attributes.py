# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:19:38 2022

@author: ŞEVVAL
"""

#attribute variable'ların class içerisinde tanımlaması, o classa özgü özelliklerdir.

class Footballer:
    
    age = 30
    football_club = "barcelona"

f1 = Footballer()

print(f1) #<__main__.Footballer object at 0x0000016DE4184E80>  
          #bir object olduğunu ve memoryde kapladığı alanı gösterir.

print(f1.age)

print(f1.football_club) #yaratılan futbolcunun attributeları görüntülenir.

f1.football_club = "real_madrid"

print(f1.football_club) #attribute değiştirildi.