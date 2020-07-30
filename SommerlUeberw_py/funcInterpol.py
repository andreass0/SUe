# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:18:27 2020 

@author: Andreas
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:26 2020

@author: Andreas
"""

'Funktion zur Interpolation von Stundenwerten eines Tages zu Sekundenwerten'

'Zum Einlesen in SUE.py müssen 25 Zeilen vorhanden sein'

# from funcWriteTxt import writeTxt 
# import numpy as np
# def solInterpol(fileName, inputArray):
#     file = open(fileName, 'w+')
#     for i in range(len(inputArray)):
#          file.write(str(inputArray[i])+'\n')
#     file.close()
#     return file


# array = np.array([1,2,3,4])
# writeTxt('tOP.txt', array)
def interpol(fileName):
    file = open(fileName)
    fileLines = file.readlines()
    content = [float(line.split()[0]) for line in fileLines]
    file.close()
    
    interval = 3600     #sekunden
    index = 0
    step = list()
    sol = list()
    
    while index < len(content) - 1:
        step.append((content[index + 1] - content[index]) / interval)
        # step.append(index)
        # print(step)
        index += 1
        
    n = 0    
    for i in range(len(step)):
        sol.append(content[i])
        if n > 0:
            n += 1
        for k in range(3599):
            sol.append(sol[n] + step[i])
            n += 1
            # print(sol[n])
            # print(n)
    
    return sol


# sol = interpol("SonneneinstahlungStunden.txt")
# solFile = writeTxt('sonneInterpolTest.txt', sol)











# file = open('SonneneinstahlungStunden.txt')
# fileLines = file.readlines()

# content = [float(line.split()[0]) for line in fileLines]

# interval = 3600     #sekunden
# index = 0
# step = list()
# sol = list()

# while index < len(content) - 1:
#     step.append((content[index + 1] - content[index]) / interval)
#     # step.append(index)
#     # print(step)
#     index += 1
    
# n = 0    
# for i in range(len(step)):
#     sol.append(content[i])
#     if n > 0:
#         n += 1
#     for k in range(3599):
#         sol.append(sol[n] + step[i])
#         n += 1
#         # print(sol[n])
#         # print(n)
    
        
