# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 14:14:42 2020

@author: a.sarkany
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import multi_dot
# from funcSchichtmatrix import schichtmatrix
import math
from funcBauteilmatrix import bauteilmatrix
from funcCapacity import capacity
# from funcUwertBT import uBT
import classes as cl
from funcReadTxt import readTxt
from funcWriteTxt import writeTxt
from funcGeneralWriteTxt import generalWriteTxt
from funcStrahlungFenster import strahlungFenster
from funcStrahlungBauteil import strahlungBauteil
#from funcInterpol import interpol



"---------------Eingangswerte---------------"

'Simulationsparameter'

zeitschritt = 10 #Zeitschritt in Sekunden
zeit = 0    #Beginnzeit in Sekunden
stunde = 0  #Beginnzeit in Stunden
durchlauf = 1 #Beginn mit 1. Durchlauf
simDauer = 86400   #Simulationsdauer in Sekunden
i = 0
# b = (int(simDauer / zeitschritt), 1)
sizeArray = int(simDauer / zeitschritt)
tOPArray = np.zeros(sizeArray) #Arrays zum Plotten initialisieren
tOPStunde = []  #Stundenausgabe der operativen Temperatur zur Validierung

zeitArray = np.zeros(sizeArray) #Arrays zum Plotten initialisieren
bTiArray = np.zeros(sizeArray)
# tOPArray = list() #Arrays zum Plotten initialisieren
# zeitArray = list() #Arrays zum Plotten initialisieren
genauigkeit = 1e-3   #Simulationsgenauigkeit
abbruch = False     #Initialisierung der Abbruchvariable für die Simulation
maxDurchlaeufe = 1000 #maximale Anzahl der erlaubten Durchläufe bis Konvergenz eintritt
index = list()   #Index für allgemeine Ausgabe

'Randbedingungen'
tE = np.array([21.31, 20.18, 19.27, 18.53, 17.97, 17.62, 17.66, 19.07, 21.41, 23.94, 26.23, 28.08, 29.48, 30.47, 31.1, 31.45, 31.54, 31.3, 30.6, 29.42, 27.86, 26.09, 24.31, 22.69, 21.31])
#tE = np.array([30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30])

#tE = -10 #Außentemperatur in Grad Celsius
#tSky = tE - 11
tBoden = 10
tInt = 30 #interne Starttemperatur in Grad Celsius
tInnenflaechen = tInt
tC = tInt
tR = tInt
tOP = tInt
tBTi = tInt
tBTe = tInt
H = 172     #Seehöhe des Standortes in m


cA = 1.0068 * 1000 #spezifische Wärmekapazität Luft J/(kg*K)
rhoA = 1.1894 #Dichte Luft in kg/m³

"Wärmeübergangswiderstände"
RsiHor = 0.13    #horizontal
RsiUp = 0.1        #aufwärts
RsiDown = 0.17    #abwärts
fKonvHor = 1-5/(1/RsiHor)   #konvektive Anteile des Wärmestroms in die entsprechenden Richtungen
fKonvUp = 1-5/(1/RsiUp)
fKonvDown = 1-5/(1/RsiDown)

"Konvektionswärmeübergangskoeffzienten an der Innenfläche"
hChor = 2.5
hCup = 5
hCdown = 0.7 
hRad = 5.5

"Fenster"
idealLueften = True
scheduleFeLueftung = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1])
scheduleFeLueftung = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
scheduleFeLueftung = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
scheduleFeSonnenschutz = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
scheduleFeSonnenschutz = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#scheduleFeSonnenschutz = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

Fe01 = cl.Fenster('1', 'Fe01', 1.23, 1.48, 0, 1.1, 2.5, 0.65, 0.16, 180, 0)
# iS = np.array([0, 0, 0, 0, 0, 0, 0, 10, 50, 250, 400, 550, 575, 550, 400, 250, 50, 10, 0, 0, 0, 0, 0, 0, 0]) #später aus Verschattungstool
 
"Strahlung"
eX = np.array([0, 0, 0, 0, 0, 0, -0.442, -0.265, -0.088, 0.079, 0.224, 0.336, 0.409, 0.436, 0.417, 0.353, 0.247, 0.108, -0.056, -0.232, -0.410, 0, 0, 0, 0])
eY = np.array([0, 0, 0, 0, 0, 0, 0.892, 0.929, 0.903, 0.816, 0.673, 0.484, 0.262, 0.023, -0.219, -0.445, -0.641, -0.793, -0.892, -0.929, -0.903, 0, 0, 0, 0])
eZ = np.array([0, 0, 0, 0, 0, 0, 0.097, 0.257, 0.42, 0.573, 0.705, 0.808, 0.874, 0.9, 0.882, 0.823, 0.726, 0.599, 0.449, 0.288, 0.126, 0, 0, 0, 0])
fSol = 0.1
S = 1322.4 #Normalstrahlungsintensität in W/m²
#strahlungGlobal = [0, 0.00, 0.00, 0.00, 0.00, 4.96, 41.02, 94.55, 146.96, 244.50, 345.02, 368.75, 325.61, 240.80, 300.67, 310.74, 261.11, 172.91, 87.63, 40.52, 4.96, 0.00, 0.00, 0.00, 0.00]

"Raumgeometrie"
l = 4   #Abmessungen in Meter
b = 4
h = 2.5
volRaum = l * b * h
BF = l*b
H = 172 #Seehöhe des Standortes in m

'Wände'
w1 = cl.Bauteil('120', 'w1', b, h, 0.09, 3, 0, 0, 0.5)      #Wand 1 mit Aufbau 2 und keinem Fenster
w2 = cl.Bauteil('220', 'w2', l, h, 0.09, 3, 90, 0, 0.5)
w3 = cl.Bauteil('311', 'w3', b, h, 0.305, 1, 180, 0, 0.5)     #Wand 3 mit Aufbau 1 und dem Fenster Fe01 (iD = 1)
w4 = cl.Bauteil('420', 'w4', l, h, 0.09, 3, 270, 0, 0.5)

'Boden'
b1 = cl.Bauteil('530', 'b1', l, b, 0.307, 3, 0, 90, 0.5)

'Dach'
d1 = cl.Bauteil('640', 'd1', l, b, 0.307, 3, 0, 90, 0.5)


"Aufbauten"
AW01 = cl.Aufbau('1', 'AW01', 2)
IW01 = cl.Aufbau('2', 'IW01', 2)
FB01 = cl.Aufbau('3', 'FB01', 0)
AD01 = cl.Aufbau('4', 'AD01', 1)

'Schichten'
#Stahlbeton14cm = cl.Schicht('1', 'Stahlbeton14cm', 2400, 1000, 2.5, 0.14)
#epsF = cl.Schicht('1', 'epsF', 15, 1500, 0.04, 0.16)
#Systemputz = cl.Schicht('1', 'Systemputz', 1600, 1000, 0.8, 0.005)

Systemputz = cl.Schicht('1', 'Systemputz', 1600, 1000, 0.8, 0.005)
epsF = cl.Schicht('1', 'epsF', 15, 1500, 0.04, 0.16)
Stahlbeton14cm = cl.Schicht('1', 'Stahlbeton14cm', 2400, 1000, 2.5, 0.14)

 
GKF = cl.Schicht('2', 'GKF', 900, 1050, 0.21, 0.0125)
TWKF = cl.Schicht('2', 'TWKF', 50, 1030, 0.037, 0.075)
GKF = cl.Schicht('2', 'GKF', 900, 1050, 0.21, 0.0125)

#Parkett = cl.Schicht('3', 'Parkett', 600, 2500, 0.15, 0.0125)
#Ausgleich = cl.Schicht('3', 'Ausgleich', 50, 1800, 0.04, 0.005)
#Zementestrich = cl.Schicht('3', 'Zementestrich', 1800, 1080, 1.11, 0.05)
#TSD = cl.Schicht('3', 'TSD', 150, 800, 0.045, 0.03)
#psBeton = cl.Schicht('3', 'psBeton', 120, 1350, 0.06, 0.05)
#Stahlbeton16cm = cl.Schicht('3', 'Stahlbeton16cm', 2400, 1000, 2.5, 0.16)

Stahlbeton16cm = cl.Schicht('3', 'Stahlbeton16cm', 2400, 1000, 2.5, 0.16)
psBeton = cl.Schicht('3', 'psBeton', 120, 1350, 0.06, 0.05)
TSD = cl.Schicht('3', 'TSD', 150, 800, 0.045, 0.03)
Zementestrich = cl.Schicht('3', 'Zementestrich', 1800, 1080, 1.11, 0.05)
Ausgleich = cl.Schicht('3', 'Ausgleich', 50, 1800, 0.04, 0.005)
Parkett = cl.Schicht('3', 'Parkett', 600, 2500, 0.15, 0.012)

#Stahlbeton16cm = cl.Schicht('4', 'Stahlbeton16cm', 2400, 1000, 2.5, 0.16)
#psBeton = cl.Schicht('4', 'psBeton', 120, 1350, 0.06, 0.05)
#TSD = cl.Schicht('4', 'TSD', 150, 800, 0.045, 0.03)
#Zementestrich = cl.Schicht('4', 'Zementestrich', 1800, 1080, 1.11, 0.05)
#Ausgleich = cl.Schicht('4', 'Ausgleich', 50, 1800, 0.04, 0.005)
#Parkett = cl.Schicht('4', 'Parkett', 600, 2500, 0.15, 0.0125)

Parkett = cl.Schicht('4', 'Parkett', 600, 2500, 0.15, 0.012)
Ausgleich = cl.Schicht('4', 'Ausgleich', 50, 1800, 0.04, 0.005)
Zementestrich = cl.Schicht('4', 'Zementestrich', 1800, 1080, 1.11, 0.05)
TSD = cl.Schicht('4', 'TSD', 150, 800, 0.045, 0.03)
psBeton = cl.Schicht('4', 'psBeton', 120, 1350, 0.06, 0.05)
Stahlbeton16cm = cl.Schicht('4', 'Stahlbeton16cm', 2400, 1000, 2.5, 0.16)

# "Lüftung"
# n50 = 0.5 # in 1/h
# "Fenster/Sonnenschutz"
# a = (1, 24)
# iS = np.zeros(a) #aus Verschattungstool
# gWert = 0.5
# gw = 0.9 * 0.98 * gWert
# fSol = 0.1
# fF = 0.3    #Verschattungsfaktor vereinfacht mit 0.3 angenommen
# fS = 1 #beim Kühlfall vereinfacht mit 1 angenommen
# aTrans = aFenster * (1 - fF) * fS * gw

# "Innere Lasten"
# qiLGeraete = 6 * 200     #innere Lasten in Watt
# qiLPersonen = 6 * 100
# qiLHeizKuehl = 500

pGeraetehBF = np.array([1.76, 1.67, 1.8, 1.8, 2.61, 5.76, 5.09, 8.06, 6.84, 6.3, 5.67, 4.1, 3.47, 3.33, 5.36, 6.3, 7.7, 6.71, 6.26, 5.36, 4.32, 3.11, 2.7, 1.98, 1.76])
pPersonenhBF = np.array([3.76, 3.76, 3.76, 3.76, 3.76, 3.76, 3.76, 0.94, 0.94, 0.94, 0.94, 0.94, 0.94, 2.82, 2.82, 2.82, 2.82, 3.76, 3.76, 3.76, 3.76, 3.76, 3.76, 3.76, 3.76])
vLueftunghNatBF = np.array([1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 0.353, 0.353, 0.353, 0.353, 0.353, 0.353, 1.058, 1.058, 1.058, 1.058, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411])
vLueftunghMechBF = np.array([1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411, 1.411])

"Eingabe ob Lüftung vorhanden"
ventNat = 1     #1 wenn natürliche Lüftung vorhanden, 0 wenn nicht.
ventMech = 0    #1 wenn mechanische Lüftung vorhanden, 0 wenn nicht.
fGer = 0.4  #geräteabhängiger Gewichtungsfaktor mit 0.4 festgelegt lt. Entwurf 8110-3 2020
fPer = 0.4  #personenabhängiger Gewichtungsfaktor mit 0.4 festgelegt lt. Entwurf 8110-3

"Recorder"
recTop = list()
recqBT = list()
rectBTi1 = list()
rectBTi2 = list()
rectBTi3 = list()
rectBTi4 = list()
rectBTe1 = list()
rectBTe2 = list()
rectBTe3 = list()
rectBTe4 = list()
recStrahlung = list()


"Assemblierung"  
            
'Aufbauten'
for i in range(len(cl.Aufbau.listAufbau)):
    for k in range(len(cl.Schicht.listSchicht)):
        if cl.Schicht.listSchicht[k].iD == cl.Aufbau.listAufbau[i].iD:
            cl.Aufbau.listAufbau[i].Schichten.append(cl.Schicht.listSchicht[k])
'Berechnung der Schichtmatrizen'
for k in range(len(cl.Aufbau.listAufbau)):
    for i in range(len(cl.Aufbau.listAufbau[k].Schichten)):
        # print(cl.Aufbau.listAufbau[k].zS)
        # print(cl.Aufbau.listAufbau[k].Schichten[i].zSi)
        # print('\n')
        
        cl.Aufbau.listAufbau[k].zS = multi_dot([cl.Aufbau.listAufbau[k].zS, cl.Aufbau.listAufbau[k].Schichten[i].zSi]) 
        # print(cl.Aufbau.listAufbau[k].zS)
        # print('\n')
        
#u-Wert des Aufbaus ohne Übergangskoeffizienten
for i in range(len(cl.Aufbau.listAufbau)):
    for k in range(len(cl.Schicht.listSchicht)):
        if cl.Schicht.listSchicht[k].iD == cl.Aufbau.listAufbau[i].iD:
            cl.Aufbau.listAufbau[i].uBT += cl.Schicht.listSchicht[k].rSchicht
    cl.Aufbau.listAufbau[i].uBT = 1 / cl.Aufbau.listAufbau[i].uBT
    
'Bauteile'
#adding the layers to the building part
for i in range(len(cl.Bauteil.listBT)):
    for k in range(len(cl.Aufbau.listAufbau)):
        if cl.Aufbau.listAufbau[k].iD == cl.Bauteil.listBT[i].iD[1]:
            cl.Bauteil.listBT[i].Aufbau = cl.Aufbau.listAufbau[k]   
            
#adding windows to the building part            
for i in range(len(cl.Bauteil.listBT)):
    for k in range(len(cl.Fenster.listFe)):
        if cl.Fenster.listFe[k].iD == cl.Bauteil.listBT[i].iD[2]:
            cl.Bauteil.listBT[i].Fenster.append(cl.Fenster.listFe[k])
            cl.Bauteil.listBT[i].a = cl.Bauteil.listBT[i].a - cl.Fenster.listFe[k].A

#Summe Flächen
aBTges = 0    #initialisieren für Summenschleife
for i in range(len(cl.Bauteil.listBT)):
    aBTges = aBTges + cl.Bauteil.listBT[i].a

'Anfangstemperaturen zuweisen'
for i in range(len(cl.Bauteil.listBT)):
    cl.Bauteil.listBT[i].tBTe = tInt
    cl.Bauteil.listBT[i].tBTi = tInt
    
# # checking if the loop has worked
# for i in range(len(cl.Bauteil.listBT)):
#     for k in range(len(cl.Schicht.listSchicht)):
#         if k < len(cl.Bauteil.listBT[i].Aufbau.Schichten):
#             print(cl.Bauteil.listBT[i].Aufbau.Schichten[k].name)
#     print('Temperatur Oberfläche aussen = ' + str(cl.Bauteil.listBT[i].tBTe))
#     print('Temperatur Oberfläche innen = ' + str(cl.Bauteil.listBT[i].tBTi))
#     print('\n')
    
"--------------Solare Einträge---------------"

strahlungFenster(cl.Fenster.listFe, eX, eY, eZ, H)
strahlungBauteil(cl.Bauteil.listBT, eX, eY, eZ, H)



while zeit < simDauer and abbruch != True:
    
# #     # print(i)
# #     # print(zeit)
    'Berechnung der Außentemperatur zum jeweiligen Zeitschritt'

    tE_akt = tE[stunde-1] + (tE[stunde] - tE[stunde-1]) / 3600 * (zeit - (stunde - 1) * 3600)
    tSky_akt = tE_akt - 11

    "--------------Wärmeströme---------------"
    
    for i in range(len(cl.Bauteil.listBT)):
        aci = 0     #Wärmeübergangskoeffizient konvektiv innen, Platzhalter; wird später zugewiesen
        ari = 5.13   #Wärmeübergangskoeffizient radiativ lt. Entwurf 8110-3 2020
        ae = 25     #äußerer Wärmeübergangskoeffizient Konvektion + Strahlung in W/m²K
        if cl.Bauteil.listBT[i].Aufbau.orientation == 2:
            aci = 2.5   #Wärmübergangskoeffizient für horizontalen Wärmestrom bei einem vertikalen Bauteil
            cl.Bauteil.listBT[i].Aufbau.rSi = 0.13
        elif cl.Bauteil.listBT[i].Aufbau.orientation == 1:
            if cl.Bauteil.listBT[i].tBTi > cl.Bauteil.listBT[i].tBTe:
                aci = 5     #Wärmeübergangskoeffizient für Wärmestrom nach "oben"
                cl.Bauteil.listBT[i].Aufbau.rSi = 0.10
            else:
                aci = 0.7   #Wärmeübergangskoeffizient für Wärmestrom nach "unten"
                cl.Bauteil.listBT[i].Aufbau.rSi = 0.17
        elif cl.Bauteil.listBT[i].Aufbau.orientation == 0:
            if cl.Bauteil.listBT[i].tBTi < cl.Bauteil.listBT[i].tBTe:
                aci = 5     #Wärmeübergangskoeffizient für Wärmestrom nach "oben"
                cl.Bauteil.listBT[i].Aufbau.rSi = 0.10
            else:
                aci = 0.7   #Wärmeübergangskoeffizient für Wärmestrom nach "unten"
                cl.Bauteil.listBT[i].Aufbau.rSi = 0.17
        if cl.Bauteil.listBT[i].Lage == 3:
            cl.Bauteil.listBT[i].Aufbau.rSe = cl.Bauteil.listBT[i].Aufbau.rSi

        cl.Bauteil.listBT[i].qBTic = aci * cl.Bauteil.listBT[i].a * (tC - cl.Bauteil.listBT[i].tBTi)
        cl.Bauteil.listBT[i].qBTir = ari * cl.Bauteil.listBT[i].a * (tR - cl.Bauteil.listBT[i].tBTi)
        if cl.Bauteil.listBT[i].Lage == 1:
            cl.Bauteil.listBT[i].qBTe = ae * cl.Bauteil.listBT[i].a * (tE_akt - cl.Bauteil.listBT[i].tBTe)
        elif cl.Bauteil.listBT[i].Lage == 2:
            cl.Bauteil.listBT[i].qBTe = ae * cl.Bauteil.listBT[i].a * (10 - cl.Bauteil.listBT[i].tBTe)  #Annahme einer konstanten Temperatur des Erdkörpers von 10 Grad Celsius
        elif cl.Bauteil.listBT[i].Lage == 3:
            cl.Bauteil.listBT[i].qBTe = aci * cl.Bauteil.listBT[i].a * (tC - cl.Bauteil.listBT[i].tBTe) + ari * cl.Bauteil.listBT[i].a * (tR - cl.Bauteil.listBT[i].tBTe)
        # cl.Bauteil.listBT[i].qBTleit = cl.Bauteil.listBT[i].U
        # for k in range(len(cl.Bauteil.listBT[i].Aufbau.zSi)):
        #     print(k)
        cl.Bauteil.listBT[i].Aufbau.zB = bauteilmatrix(cl.Bauteil.listBT[i].Aufbau.rSi, cl.Bauteil.listBT[i].Aufbau.rSe, cl.Bauteil.listBT[i].Aufbau.rAir, cl.Bauteil.listBT[i].Aufbau.zS)
        #print(cl.Bauteil.listBT[i].Aufbau.zB)
        (cl.Bauteil.listBT[i].cI, cl.Bauteil.listBT[i].cE) = capacity(cl.Bauteil.listBT[i].Aufbau.zB[0, 0], cl.Bauteil.listBT[i].Aufbau.zB[0, 1], cl.Bauteil.listBT[i].Aufbau.zB[1,1], simDauer, cl.Bauteil.listBT[i].a)
        cl.Bauteil.listBT[i].qBTleit = cl.Bauteil.listBT[i].Aufbau.uBT * cl.Bauteil.listBT[i].a * (cl.Bauteil.listBT[i].tBTi - cl.Bauteil.listBT[i].tBTe)
        # checking if the loop has worked
    # for i in range(len(cl.Bauteil.listBT)):
    #     for k in range(len(cl.Schicht.listSchicht)):
    #         if k < len(cl.Bauteil.listBT[i].Aufbau.Schichten):
    #             print(cl.Bauteil.listBT[i].Aufbau.Schichten[k].name)
    #     print('Temperatur Oberfläche innen = ' + str(cl.Bauteil.listBT[i].tBTi))
    #     print('Temperatur Oberfläche aussen = ' + str(cl.Bauteil.listBT[i].tBTe))
    #     print('Kapazität innen = ' + str(cl.Bauteil.listBT[i].cI))
    #     print('Kapazität aussen = ' + str(cl.Bauteil.listBT[i].cE))
    #     print('\n')  
        
    'Lüftungsströme'
    
    'Fenster'
    cRef = 100 # Austauschkoeffizient in m^(1/2)/(h*K^(1/2))
    for i in range(len(cl.Fenster.listFe)):
        cl.Fenster.listFe[i].verwendung = scheduleFeLueftung[stunde]
        'geschlossen'
        if cl.Fenster.listFe[i].verwendung == 0:
            cl.Fenster.listFe[i].vFe = 0
        'geöffnet'
        if idealLueften == True:
            if cl.Fenster.listFe[i].verwendung == 1 and tE_akt < tOP:
                cl.Fenster.listFe[i].vFe = 0.7 * cRef * cl.Fenster.listFe[i].A * np.sqrt(cl.Fenster.listFe[i].h) * np.sqrt(np.abs(tC - tE_akt))
        if idealLueften == False:
            if cl.Fenster.listFe[i].verwendung == 1:
                cl.Fenster.listFe[i].vFe = 0.7 * cRef * cl.Fenster.listFe[i].A * np.sqrt(cl.Fenster.listFe[i].h) * np.sqrt(np.abs(tC - tE_akt))
        'gekippt'
        if idealLueften == True:
            if cl.Fenster.listFe[i].verwendung == 2 and tE_akt < tOP:
                cl.Fenster.listFe[i].vFe = 0.7 * cRef * 0.1 * np.sqrt(cl.Fenster.listFe[i].h) * np.sqrt(np.abs(tC - tE_akt))  #0.1 Abschätzung der Fläche lt. TopPhi
        if idealLueften == False:
            if cl.Fenster.listFe[i].verwendung == 2:
                cl.Fenster.listFe[i].vFe = 0.7 * cRef * 0.1 * np.sqrt(cl.Fenster.listFe[i].h) * np.sqrt(np.abs(tC - tE_akt))
    'Lüftungsschacht'
    #to be added
    
    "Volumenströme"
    
    'Volumenströme zu Folge mechanischer/natürlicher Lüftung'
    if ventNat == 1:
        vNat = vLueftunghNatBF[stunde] * BF * 1 / 3600 * zeitschritt
    else:
        vNat = 0
        
    if ventMech == 1:
        vMech = vLueftunghMechBF[stunde] * BF * 1 / 3600 * zeitschritt
    else:
        vMech = 0
        
    'Aufsummieren der Volumenströme der Fenster'
    vCges = 0
    for i in range(len(cl.Fenster.listFe)):
        vCges += cl.Fenster.listFe[i].vFe
        
    'Gesamter Wärmestrom infolge Lüftung'
    qVent = 0.34 * (vCges + vNat + vMech) * (tE_akt - tC)
    
    'Wärmeströme durch das Fenster'
    #vorerst nur vertikale Fensterflächen
    sF = 0.5    #Sichtfaktor zum Himmel kann für vertikale Flächen mit 0.5 und für horizontale Flächen mit 1.0 angenommen werden. aus bph kalender 2015.
    aci = 2.5   #konvektiver Wärmeübergangskoeffizient für vertikale Flächen. 
    for i in range(len(cl.Fenster.listFe)):
        cl.Fenster.listFe[i].tFEi = tC + ari / (ari + aci) * (tR - tC)
        cl.Fenster.listFe[i].tFEe = tE_akt + (cl.Fenster.listFe[i].eps / ae) * (sF * tSky_akt + (1 - sF) * tE_akt - tE_akt)
        cl.Fenster.listFe[i].tFE = cl.Fenster.listFe[i].tFEi - (cl.Fenster.listFe[i].tFEi - cl.Fenster.listFe[i].tFEe) * cl.Fenster.listFe[i].uFE * (1 / (aci + ari))
    qFE = 0
    for i in range(len(cl.Fenster.listFe)):
        qFE +=  cl.Fenster.listFe[i].A * aci * (cl.Fenster.listFe[i].tFE - tC)
    # print(qFE) 
    'Solare Einträge'

    '- Fenster'
    
    qSol = 0
    for i in range(len(cl.Fenster.listFe)):
        cl.Fenster.listFe[i].strahlungGlobal_akt = cl.Fenster.listFe[i].strahlungGlobal_stunde[stunde-1] + (cl.Fenster.listFe[i].strahlungGlobal_stunde[stunde] - 
                    cl.Fenster.listFe[i].strahlungGlobal_stunde[stunde-1]) / 3600 * (zeit - (stunde - 1) * 3600)
        if scheduleFeSonnenschutz[stunde] == 1:
            qSol += cl.Fenster.listFe[i].strahlungGlobal_akt   * cl.Fenster.listFe[i].aTransSchutz
        else:
            qSol += cl.Fenster.listFe[i].strahlungGlobal_akt * cl.Fenster.listFe[i].aTrans
        # print(scheduleFeSonnenschutz[stunde])
        #print(qSol)

    '- Bauteile'
    #bei Bauteilaußentemperatur berücksichtigt
    
    'Aufsummieren der konvektiven Wärmeströme innen durch die Bauteile'
    qBT = 0
    for i in range(len(cl.Bauteil.listBT)):
        qBT += cl.Bauteil.listBT[i].qBTic
    qBT = (-1) * qBT
    # print(qBT)
    'Wärmeströme durch Innere Lasten'
    qiLGeraete = pGeraetehBF[stunde] * BF * 1 / 3600 * zeitschritt
    qiLPersonen = pPersonenhBF[stunde] * BF * 1 / 3600 * zeitschritt
    qiLc = qSol * fSol + qiLGeraete * fGer + qiLPersonen * fPer
    qiLr = qSol * (1 - fSol) + qiLGeraete * (1 - fGer) + qiLPersonen * (1 - fPer)
    #qiLc = 0
    #qiLr = 0
    # print(qiLc)
    # print(qiLr)
    
    'Neue Lufttemperatur'
    cE = b1.a * 38 * 1046.7     #Kapazität der Einrichtung in J/K
    
    tC = tC + (qiLc + qBT + qVent +qFE)/cE * zeitschritt  #neue Lufttemperatur
    # print(tC)
    
    'Neue Strahlungstemperatur'
    TA = 0  #initialiesieren für Schleife von tBT * aBT
    for i in range(len(cl.Bauteil.listBT)):
        TA += cl.Bauteil.listBT[i].tBTi * cl.Bauteil.listBT[i].a
    
    tR = (TA + (qiLr / ari)) / aBTges
    # print(tR)
    'Neue Temperatur Innenseite Bauteiloberfläche'
    for i in range(len(cl.Bauteil.listBT)):
        cl.Bauteil.listBT[i].tBTi = cl.Bauteil.listBT[i].tBTi + (cl.Bauteil.listBT[i].qBTic + cl.Bauteil.listBT[i].qBTir - cl.Bauteil.listBT[i].qBTleit) / cl.Bauteil.listBT[i].cI * zeitschritt    #sollte das nicht minus qBT,leit sein?
    
    'Neue Temperatur Außenseite Bauteiloberfläche'
    for i in range(len(cl.Bauteil.listBT)):
        if cl.Bauteil.listBT[i].Lage == 1:
            cl.Bauteil.listBT[i].strahlungGlobal_akt = cl.Bauteil.listBT[i].strahlungGlobal_stunde[stunde-1] + (cl.Bauteil.listBT[i].strahlungGlobal_stunde[stunde] - 
                        cl.Bauteil.listBT[i].strahlungGlobal_stunde[stunde-1]) / 3600 * (zeit - (stunde - 1) * 3600)
            cl.Bauteil.listBT[i].tBTe = cl.Bauteil.listBT[i].tBTe + (cl.Bauteil.listBT[i].qBTe + 
                     cl.Bauteil.listBT[i].qBTleit + cl.Bauteil.listBT[i].strahlungGlobal_akt * cl.Bauteil.listBT[i].AbsGrad * cl.Bauteil.listBT[i].a) / cl.Bauteil.listBT[i].cE * zeitschritt   #solarer Eintrag auf Flächen wenn Außenfläche
        else:
            cl.Bauteil.listBT[i].tBTe = cl.Bauteil.listBT[i].tBTe + (cl.Bauteil.listBT[i].qBTe + cl.Bauteil.listBT[i].qBTleit) / cl.Bauteil.listBT[i].cE * zeitschritt
    
    'Neue operative Temperatur'
    tOP = 0.5 * (tC + tR)
    
    'Ausgabe'
    recTop.append(tOP)
    recqBT.append(qBT)
    rectBTi1.append(cl.Bauteil.listBT[0].tBTi)
    rectBTi2.append(cl.Bauteil.listBT[1].tBTi)
    rectBTi3.append(cl.Bauteil.listBT[2].tBTi)
    rectBTi4.append(cl.Bauteil.listBT[3].tBTi)
    rectBTe1.append(cl.Bauteil.listBT[0].tBTe)
    rectBTe2.append(cl.Bauteil.listBT[1].tBTe)
    rectBTe3.append(cl.Bauteil.listBT[2].tBTe)
    rectBTe4.append(cl.Bauteil.listBT[3].tBTe)
    recStrahlung.append(cl.Fenster.listFe[0].strahlungGlobal_akt)
    
    "Schleifensteuerung"
    
    arrayPosition = int(zeit / zeitschritt)
    tOPArray[arrayPosition] = tOP
    bTiArray[arrayPosition] = cl.Bauteil.listBT[2].tBTi
    
    #Stundenausgabe zur Validierung hardcoded
    temp_tOP = 0

    if stunde == 0 and zeit / 3600 == stunde:
        temp_tOP += tOPArray[0]
        tOPStunde.append(temp_tOP)

    if stunde >= 1 and zeit / 3600 == stunde:
        rangeFromThisValue = stunde - 1 #if stunde >= 1 else 0
        rangeToThisValue = stunde
        for i in range(int(rangeFromThisValue * sizeArray/(simDauer/3600)), int(rangeToThisValue * sizeArray/(simDauer/3600))):   #sizeArray = simDauer / zeitschritt
            temp_tOP += tOPArray[i] / (sizeArray/(simDauer/3600))
        tOPStunde.append(temp_tOP)
        #print(tOPStunde)
    
    zeitArray[arrayPosition] = zeit
    # tOPArray.append(tOP)
    # zeitArray.append(zeit)
    print(zeit)
    print(tOP)
    print(stunde)
    print(cl.Bauteil.listBT[2].tBTi)
    print(cl.Bauteil.listBT[2].tBTe)
    
    zeit = zeit + zeitschritt
    if len(index) == 0:
        index.append(0)
    else:
        index.append(index[len(index) - 1] + 1)

    
    for n in range(25):
        if zeit/3600 == n:
            stunde = stunde + 1
            
    # if stunde == 2:
    #    abbruch = True
       
    if zeit == simDauer:
        simGenauigkeit = abs(tOPArray[0] - tOPArray[sizeArray-1]) / tOPArray[0]
        #print(simGenauigkeit)
        if simGenauigkeit <= genauigkeit:
            abbruch = True
        elif durchlauf == maxDurchlaeufe:
            #print(durchlauf)
            abbruch = True
        else:
            zeit = 0
            stunde = 0
            i = 0
            tOPStunde = []
            durchlauf += 1
            #print(durchlauf)
            # abbruch = True
            
print(durchlauf)            
    # zeit = zeit + zeitschritt
'Ausgabedateien des letzten Durchlaufes'
writeTxt('tOP.txt', tOPArray)
writeTxt('tOPStunde.txt', tOPStunde)


'Recorder in Ausgabedatei schreiben'
writeTxt('rectOP.txt', recTop)
writeTxt('recqBT.txt', recqBT)
writeTxt('rectBTi1.txt', rectBTi1)
writeTxt('rectBTi2.txt', rectBTi2)
writeTxt('rectBTi3.txt', rectBTi3) 
writeTxt('rectBTi4.txt', rectBTi4)
writeTxt('recStrahlung.txt', recStrahlung)


"Ploteinstellungen"
#fig = plt.figure(figsize=(6,3))
"Plot Top"   
#plotrecTop = plt.plot(index, recTop, label='Verlauf der operativen Temperatur')
#plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
#plt.ylabel('Top in °C', fontsize='x-large')
#plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
##plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

#"Plot Bauteiloberfläche Innentemperatur Wand 1"   
#plotrecBTi1 = plt.plot(index, rectBTi1, label='Verlauf BTi von Wand 1')
#plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
#plt.ylabel('Top in °C', fontsize='x-large')
#plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
##plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

"Plot Bauteiloberfläche Innentemperatur Wand 2"   
plotrecBTi1 = plt.plot(index, rectBTi2, label='Verlauf BTi von Wand 2')
plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
plt.ylabel('Top in °C', fontsize='x-large')
plt.legend(bbox_to_anchor=(0.5, 0.5), loc='upper left', borderaxespad=0)
#plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

"Plot Bauteiloberfläche Innentemperatur Wand 3"   
plotrecBTi1 = plt.plot(index, rectBTi3, label='Verlauf BTi von Wand 3')
plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
plt.ylabel('Top in °C', fontsize='x-large')
plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
#plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

"Plot Bauteiloberfläche Innentemperatur Wand 4"   
plotrecBTi1 = plt.plot(index, rectBTi4, label='Verlauf BTi von Wand 4')
plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
plt.ylabel('Top in °C', fontsize='x-large')
plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
#plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

#"Plot Bauteiloberfläche Außentemperaturen Wand 1"   
#plotrecBTe1 = plt.plot(index, rectBTe1, label='Verlauf BTe von Wand 1')
#plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
#plt.ylabel('Top in °C', fontsize='x-large')
#plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
##plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

"Plot Bauteiloberfläche Außentemperaturen Wand 2"   
plotrecBTe1 = plt.plot(index, rectBTe2, label='Verlauf BTe von Wand 2')
plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
plt.ylabel('Top in °C', fontsize='x-large')
plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
#plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

"Plot Bauteiloberfläche Außentemperaturen Wand 3"   
plotrecBTe1 = plt.plot(index, rectBTe3, label='Verlauf BTe von Wand 3')
plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
plt.ylabel('Top in °C', fontsize='x-large')
plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
#plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

"Plot Bauteiloberfläche Außentemperaturen Wand 4"   
plotrecBTe1 = plt.plot(index, rectBTe4, label='Verlauf BTe von Wand 4')
plt.xlabel('Zeit in 10 Sekunden', fontsize='x-large')
plt.ylabel('Top in °C', fontsize='x-large')
plt.legend(bbox_to_anchor=(0.5, 0.5), loc='best', borderaxespad=0)
#plt.legend(bbox_to_anchor=(1.02, 1), borderaxespad=0)

plt.show()
plt.savefig('plot.pdf')