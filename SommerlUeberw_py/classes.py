# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:56:25 2020

@author: a.sarkany
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import multi_dot
from funcSchichtmatrix import schichtmatrix
from funcBauteilmatrix import bauteilmatrix
from funcCapacity import capacity

T = 86400

class Bauteil:
    #class variable to count objects created
    counter = 0
    #list for BT
    listBT = []
    def __init__(self, iD, name, länge, breite, dicke, Lage, Azimut, Neigung, AbsGrad):
        self.iD = iD
        self.name = name
        self.länge = länge
        self.breite = breite
        self.dicke = dicke
        self.a = länge * breite
        #self.RB = RB        #Innenbauteil = 0 Außenbauteil = 1
        self.Lage = Lage    #0 = adiabat, 1 = Außenluft, 2 = Erdberührt, 3 = Innenbauteil
        self.Azimut = Azimut #0-360 Grad
        self.Neigung = Neigung #0-180 Grad 0=horizontal 90=vertikal
        self.AbsGrad = AbsGrad
        #if self.RB == 0:
        #    self.Lage = 3
        self.Aufbau = object
        self.Fenster = []
        self.cI = float     #Wärmekapazität an der inneren Seite des Bauteiles in J/K
        self.cE = float     #Wärmekapazität an der äußeren Seite des Bauteiles in J/K
        
        self.tBTi = float   #Temperatur des Bauteils an der Innenoberfläche
        self.tBTe = float   #Temperatur des Bauteils an der Außenpberfläche
        self.qBTic = float
        self.qBTir = float
        self.qBTe = float 
        self.qBTleit = float
        self.uBT = float
        self.nX = float
        self.nY = float
        self.nZ = float
        self.cosW_stunde = float
        self.strahlungDirekt_akt = float
        self.strahlungHimmel_akt = float
        self.strahlungReflex_akt = float
        self.strahlungDiffus_akt = float
        self.strahlungGlobal_akt = float
        self.strahlungDirekt_stunde = []
        self.strahlungHimmel_stunde = []
        self.strahlungReflex_stunde = []
        self.strahlungDiffus_stunde = []
        self.strahlungGlobal_stunde = []
        Bauteil.counter += 1    #counting
        Bauteil.listBT.append(self)
        

class Aufbau:
    #class variable to count objects created
    counter = 0
    #list for BT
    listAufbau = []
    #Schichtmatrix des Aufbaus
    # zS = np.array([[1, 0], [0, 1]])       #Einheitsmatrix als Platzhalter initialisieren
    def __init__(self, iD, name, orientation):
         self.iD = iD
         self.name = name
         self.orientation = orientation         # 0 = horizontalBoden, 1 = horizontalDach, 2 = vertikal
         self.rSi = float        #mögliche Richtungen der Wärmeübergangswiderstände
         self.rSe = 0.04
         self.rAir = 0          #Wärmeübergangswiderstand ruhender Luftschichten vorerst nicht berücksichtigt
         self.Schichten = []
         self.zS = np.array([[1, 0], [0, 1]])       #Einheitsmatrix als Platzhalter initialisieren
         # for i in range(len(self.Schichten)):
         #     self.zS = multi_dot([self.zS, self.Schichten[i]])          
         self.zB = float
         self.uBT = 0  #Wärmeübergangswiderstand ohne Übergangskoeffizienten
         Aufbau.counter += 1    #counting
         Aufbau.listAufbau.append(self)
         # i = 0
         # while i < len(self.Schichten):
         #     #for i in range(len(self.Schichten)):
         #     Aufbau.zS = multi_dot([Aufbau.zS, self.Schichten[i]]) 
         #     i += 1

    
class Schicht:
    #class variable to count objects created
    counter = 0
    #list for BT
    listSchicht = []
    def __init__(self, iD, name, rho, c, lambDa, dicke):
        self.iD = iD    #gibt an zu welchem Bauteil die Schicht gehört
        self.name = name
        self.rho = rho
        self.c = c
        self.lambDa = lambDa
        self.dicke = dicke
        self.zSi = schichtmatrix(self.lambDa, T, self.rho, self.c, self.dicke)
        self.rSchicht = self.dicke / self.lambDa
        Schicht.counter += 1    #counting
        Schicht.listSchicht.append(self)
        
class Fenster:
    #class variable to count objects created
    counter = 0
    #list for BT^
    listFe = []
    def __init__(self, iD, name, b, h, verwendung, uFE, eps, g, fS, fC, Azimut, Neigung):
        self.iD = iD
        self.name = name
        self.b = b  #Breite der Lüftungsöffnung
        self.h = h      #Höhe der Lüftungsöffnung
        self.A = self.b * self.h     #effektive Lüftungsfläche
        self.verwendung = verwendung    #0 = geschlossen, 1 = geöffnet, 2 = gekippt, 3 = Lueftungsschacht
        self.uFE = uFE
        self.eps = eps
        self.Azimut = Azimut
        self.Neigung = Neigung
        self.vFe = float
        self.tFEi = float
        self.tFEe = float
        self.tFE = float
        self.g = g
        self.gw = 0.9 * 0.98 * g
        self.fF= 0.3
        self.fS = fS
        self.fC = fC
        self.aTrans = self.A * (1 - self.fF) * self.fS * self.gw
        self.aTransSchutz = self.A * (1 - self.fF) * self.fS * self.gw * self.fC
        self.nX = float
        self.nY = float
        self.nZ = float
        self.red_strahlungDiffus_stunde = float
        self.red_strahlungDirekt_stunde = float
        self.cosW_stunde = float
        #self.strahlungDirekt_akt = float
        #self.strahlungHimmel_akt = float
        #self.strahlungReflex_akt = float
        #self.strahlungDiffus_akt = float
        #self.strahlungGlobal_akt = float
        self.strahlungDirekt_stunde = []
        self.strahlungHimmel_stunde = []
        self.strahlungReflex_stunde = []
        self.strahlungDiffus_stunde = []
        self.strahlungGlobal_stunde = []
        cRef = 100      #Austauschkoeffizient
        Fenster.counter += 1    #counting
        Fenster.listFe.append(self)
