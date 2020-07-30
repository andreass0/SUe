# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:33:02 2020

@author: a.sarkany
"""

import numpy as np

"Funktion zur Berechnung der Wärmekapazität eines Bauteiles"

def capacity(z11, z12, z22, T, A):
    y11 = z11 / z12
    y22 = z22 / z12
    cI = A * (T * abs(z11-1)) / (2 * np.pi * abs(z12))
    cE = A * (T * abs(z22-1)) / (2 * np.pi * abs(z12))
    return cI, cE

# (cI, cE) = capacity(8, 2, 3, 4, 5)

# print(cI)
# print(cE)

