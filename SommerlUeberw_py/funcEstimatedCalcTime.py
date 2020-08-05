# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:26 2020

@author: Andreas
"""

import time

#Function to calculate the estimated simulation time and save it in a txt for further usage
def calcTime(startTime, simGenauigkeitIst, simGenauigkeitSoll, durchlauf):
    timeTxt = open('time.txt', 'w')
    calcTime = time.perf_counter() - startTime
    calcTime = round(calcTime, 1)
    simGenauigkeitIst = round(simGenauigkeitIst, 7)
    timeTxt.write('Die Simulationsdauer von Durchlauf ' + str(durchlauf) + ' betrug ' + str(calcTime) + ' Sekunden.\n')
    timeTxt.write('Die Simulationsgenauigkeit von Durchlauf ' + str(durchlauf) + ' beträgt ' + str(simGenauigkeitIst)+'.\n')
    deltaSim = (simGenauigkeitIst - simGenauigkeitSoll)/simGenauigkeitSoll
    if deltaSim <= 0:
        deltaSim = 0
    else:
        deltaSim = abs(deltaSim)
    #timeTxt.write('Die Abweichung von der vorgegebenen Simulationsgenauigkeit beträgt ' + str(deltaSim * 100)+' %.\n')
    estimCalcTime = calcTime * deltaSim
    estimCalcTime = round(estimCalcTime, 1)
    timeTxt.write('Die vorraussichtliche Rechendauer beträgt ' + str(estimCalcTime) + ' Sekunden.\n')
    timeTxt.close()

for i in range(2):
    startTime = time.perf_counter()
    simGenauigkeitIst = 0.002
    simGenauigkeitSoll = 0.001
    calcTime(startTime, simGenauigkeitIst, simGenauigkeitSoll, 1)
    print(i)