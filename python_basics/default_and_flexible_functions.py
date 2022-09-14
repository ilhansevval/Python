# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:28:28 2022

@author: ŞEVVAL
"""

#default and flexible functions

# default function: çember çevresi= 2*pi*r

def cember_cevre(r,pi=3.14): #burada pi sayısının değeri değişmeyeceği için default değer atandı.
    
    """
    cember_cevre
    
    parametre:r,pi
    
    output:çemberin çevresi
    
    """
    
    output = 2*pi*r
    
    return output

cember_cevre(2) #pi sayısı default olarak tanımlandığından fonksiyonda yeni değer yazılmaz.
#cember cevresi 12.56 olarak hesaplandı. 


def daire_alan(r,pi=3.14): 
    
    """
    daire_alan
    
    parametre: int - r, pi
    
    output : daire alanı
    
    """
    
    output = pi*(r**2)
    
    return output

daire_alan(3) #28.26

#flexible function

def hesapla(boy,kilo,*args): #boy ve kilo parametleri kesinlikle olacak, ekstra parametler de eklenebilir.
    
    """
    hesapla
    
    parametre:boy,kilo,args
    
    output:argumanta bağlı olarak değişiklik gösterir.
    """

    print(len(args)) #args uzunluğu verilir.

    output=(boy+kilo)*args[0]
    
    return output


# def hesapla(boy,kilo,yas):
    
#     output=(boy+kilo)*yas
    
#     return output

def x(y):

    y = y + [2]

    print(y)

c = [1,2,3]

x(c) #[1, 2, 3, 2]

print(len(c)) #3


def s(x, y = 2):

    c = 2

    for i in range(y):

        c = c + x

    return c

s(2) #6
s(2,3) #8


yas=22
name="sevval"
soyisim="ilhan"


def func1(yas,name,*args,ayakkabi_no=38): #default parametreler sona yazılır.
    
    print("İsmi: ",name," Yaşı: ",yas," Ayakkabı numarası: ",ayakkabi_no)
    print(type(name))
    
    output = args[0]*yas 
    
    return output

sonuc = func1(yas,name,soyisim)

print(sonuc)

#İsmi:  sevval  Yaşı:  22  Ayakkabı numarası:  38
#<class 'str'>
#ilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhanilhan
#soyismi 22 defa (yaş kadar) yazdırır.