# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:41:29 2022

@author: ŞEVVAL
"""

#dictionary

#küçük bir database gibidir.
#multiple return yapılmak istendiğinde hepsinin belli isimleri adı altında dictionary kullanmak yararlı olur.

dictionary = {"sevval":22, "utku":6, "nazli":3}
#küçük bir database oluşturuldu.

type(dictionary) #dict

dictionary["sevval"] #Şevval'in yaşını verir(22).

type(dictionary["sevval"]) #dictionary'deki Şevval'in yaşının type'ı integerdır.

#sevval, nazlı, utku = keys
#22, 6, 3 = value

dictionary.keys() #dictionary'de tanımlı keyler verilir
#dict_keys(['sevval', 'utku', 'nazli'])

dictionary.values() #dictionary'de tanımlı valuelar verilir.
#dict_values([22, 6, 3])

def deneme():
    
    dictionary = {"sevval":22, "utku":6, "nazli":3}
    
    return dictionary

dic = deneme() #dic adında bir dictionary fonksiyon içerisinde oluşturuldu.

dic["sevval"] #sevval adlı key'in value'sunu verir(22).