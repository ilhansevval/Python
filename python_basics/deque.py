# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:13:43 2022

@author: ilhan
"""

#deque

#deque yapısı listelere oldukça benzemektedir.
#ancak liste tanımlanırken boyut belirtmeye gerek yoktu.
#deque ile listenin boyutu tanımlanıp, circler bir liste oluşturmaya imkan sağlamaktadır.

from collections import deque

dq = deque(maxlen = 3)
#deque'nun içi boştur, maximum 3 eleman eklenebilir.

dq.append(1)
print(dq)
#append methodu ile 1 elemanı eklenmiştir. deque([1], maxlen=3) 

dq.append(2)
dq.append(3)
dq.append(4)
print(dq)
#maksimum uzunluğu 3 olduğu en sona 4 eklenir, ancak 1 atılır.
#deque([2, 3, 4], maxlen=3)

dq.appendleft(5)
print(dq)
#appendleft methodu ile deque'nun başına eklenir.
#deque([5, 2, 3], maxlen=3)

dq.clear()
print(dq)
#clear methodu ile deque'nun içerisi temizlenir.
#deque([], maxlen=3)