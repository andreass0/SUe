# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:36:30 2020

@author: Andreas
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 17:33:02 2020

@author: a.sarkany
"""


"Funktion um .txt Dateien einzulesen"
'nur die erste Spalte der .txt-Datei wird gelesen.'

def readTxt(fileName):  #input file name as string into function
    file = open(fileName)
    fileLines = file.readlines()
    content = [float(line.split()[0]) for line in fileLines]    #the coloumn 0 will be extracted
    return content

# iS = readTxt('SonneneinstrahlungSekunden.txt')
