# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:53:29 2020

@author: a.sarkany
"""

"Funktion zur Berechnung der Bauteilmatrix"

import numpy as np
from numpy.linalg import multi_dot

def bauteilmatrix(rSi, rSe, rAir, *args):
    
    zAir = np.array([[1, -rAir], [0, 1]])
    zSi = np.array([[1, -rSi], [0, 1]])
    zSe = np.array([[1, -rSe], [0, 1]])
    zB = 1
    z = np.array([[1, 0], [0, 1]])
    for num in args:
        # print(num)
        z = multi_dot([z, num])
        # print(z)
    
    zB = multi_dot([zSe, z, zSi])
    

    # return zSi
    # return zSe
    return zB

# zB = bauteilmatrix(0.1, 0.2, 0.0, np.array([[1, 2], [2, 1]]), np.array([[1, 3], [3, 1]]))

