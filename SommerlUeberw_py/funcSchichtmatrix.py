# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:34:59 2020

@author: a.sarkany
"""

"Funktion zur Berechnung der Schichtmatrix"

import numpy as np
import cmath as c

def schichtmatrix(lambDa, T, rho, c, d):
    delta = np.sqrt((lambDa * T)/(np.pi * rho * c))
    xi = d / delta
    #i = complex(0, 1)
    #z11 = z22 = np.cosh(xi) * np.cos(xi) + (np.sinh(xi) * np.sin(xi)) * i
    #z12 = -delta / ( 2 * lambDa) * (np.sinh(xi) * np.cos(xi) + np.cosh(xi) * np.sin(xi) + (np.cosh(xi) * np.sin(xi) - np.sinh(xi) * np.cos(xi)) * i)
    #z21 = -lambDa / delta * (np.sinh(xi) * np.cos(xi) - np.cosh(xi) * np.sin(xi) + (np.sinh(xi) * np.cos(xi) + np.cosh(xi) * np.sin(xi)) * i)
    z11 = z22 = complex(np.cosh(xi) * np.cos(xi), np.sinh(xi) * np.sin(xi))
    z12 = -delta / ( 2 * lambDa) * complex(np.sinh(xi) * np.cos(xi) + np.cosh(xi) * np.sin(xi), np.cosh(xi) * np.sin(xi) - np.sinh(xi) * np.cos(xi))
    z21 = -lambDa / delta * complex(np.sinh(xi) * np.cos(xi) - np.cosh(xi) * np.sin(xi), np.sinh(xi) * np.cos(xi) + np.cosh(xi) * np.sin(xi))
    zS = np.array([[z11, z12], [z21, z22]])
    return zS


#zS = schichtmatrix(2.5, 86400, 2400, 1000, 0.14)
#print(zS)

    

