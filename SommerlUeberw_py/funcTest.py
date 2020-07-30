# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:48:52 2020

@author: a.sarkany
"""

import numpy as np

from funcSchichtmatrix import schichtmatrix
from funcBauteilmatrix import bauteilmatrix
from funcCapacity import capacity
class Bauteil:
    def __init__(self, name, rho, c, lambDa, dicke, orientation):
        self.name = name
        self.rho = rho
        self.c = c
        self.lambDa = lambDa
        self.orientation = orientation
        self.dicke = dicke
        # self.delta = 
        
BT1 = Bauteil('Stahbeton', 2500, 880, 2.3, 0.2, 1)
BT2 = Bauteil('WDVS', 50, 1450, 0.4, 0.2, 1)

T = 86400

zSchicht = schichtmatrix(BT1.lambDa, T, BT1.rho, BT1.c, BT1.dicke)
zSchicht1 = schichtmatrix(BT2.lambDa, T, BT2.rho, BT2.c, BT1.dicke)


zBT = bauteilmatrix(0.13, 0.04, 1, zSchicht, zSchicht1)
# print(zBT)

print(zBT)

c = capacity(zBT[0][0], zBT[0][1], zBT[1][1], T, 20)

# print(c)
