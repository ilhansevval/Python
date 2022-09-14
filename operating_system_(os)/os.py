# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:51:34 2022

@author: ilhan
"""

#os

#operating system kütüphanesi, klasörlerde dolaşmayı sağlayıp, resimleri içeriye yükler ya da kaydeder.

import os

print(os.name) 
#bilgisayarın işletim sisteminin ne olduğuna bakılır.
#nt -> windows

current_directory = os.getcwd()
print(current_directory)

#getcwd methodu ile hangi klasörde bulunduğunun bilgisi alınır.
#C:\Users\ilhan

#new folder
folder_name = "new folder"
os.mkdir(folder_name)
#new folder adında bir klasör oluşturuldu.

new_folder_name = "new_folder_2"
os.rename(folder_name, new_folder_name)
#new folder klasör adı new_folder_2 olarak değiştirildi.

#change directory
os.chdir(current_directory+"\\"+new_folder_name)
print(os.getcwd()) #C:\Users\ilhan\new_folder_2
#new_folder_2 klasörünün içerisine girileceği için '\\' kullanılır.

os.chdir(current_directory)
print(os.getcwd())

files = os.listdir()
#listdir methodu ile bulunan konumdaki klasörler listelenir.

for f in files:
    if f.endswith(".ipynb"):
        print(f) #data.ipynb
#tüm dosyalar değil de sonu ipynb ile biten dosyalar yazdırılır.


#remove directory
os.rmdir(new_folder_name)

for i in os.walk(current_directory):
    print(i)
    
#current directoryde bulunan klasörlerde dolaşarak yazdırılır.

os.path.exists("Desktop")
#böyle bir klasör bulunduğu için True sonucu yazdırılır.