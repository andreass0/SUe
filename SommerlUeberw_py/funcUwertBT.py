# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:12:57 2020

@author: Andreas
"""

import numpy as np

"Funktion zur Berechnung des U-Wertes des Bauteils ohne Übergangskoeffizienten"

def uBT(*args):
    uBT = 0
    # i = 0
    # while i <= len(args):
    #     uBT += (args[i]/args[i+1])
    #     i += 1
    #     print(uBT)
    for i in args:
        uBT += args
        print(uBT)
        
    uBT = 1/uBT
    
    return uBT

# a = [1,2,3,4]
# uBT = uBT(a)
# uBT = uBT(0.14, 2.5, 0.16, 0.04, 0.005, 0.8)
print(uBT)


