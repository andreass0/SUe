# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:26 2020

@author: Andreas
"""
# import numpy as np
def writeTxt(fileName, inputArray):
    file = open(fileName, 'w+')
    for i in range(len(inputArray)):
         file.write(str(inputArray[i])+'\n')
    file.close()
    return file


# array = np.array([1,2,3,4])
# writeTxt('tOP.txt', array)
