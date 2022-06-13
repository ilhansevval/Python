# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:02:45 2022

@author: ŞEVVAL
"""

#stacking arrays
#bir arrayle başka bir arrayi birleştirme yöntemidir.

import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[-1,-2],[-3,-4]])

#vertical (dikey birleştirme)
#array([[1, 2],
#      [3, 4]])
#array([[-1, -2],
#      [-3, -4]])

c = np.vstack((a,b))

#horizontal (yatay birleştirme)
#array([[1, 2],  array([[-1, -2],
#      [3, 4]])        [-3, -4]])

d = np.hstack((a,b))