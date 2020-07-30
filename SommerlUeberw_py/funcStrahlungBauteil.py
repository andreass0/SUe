
import math
import numpy as np
import classes as cl

#Funktion zur Berechnung der globalen Strahlung pro Stunde für Fenster
def strahlungBauteil(listBT, eX, eY, eZ, H):
    for stunde in range(25):
        T = 4.5     #Linke'sche Trübungsfaktor T = 4,5 lt. B8110-3 (Stand 2020)
        S = 1322.4  #Normalstrahlungsintensität in W/m²
        M_stunde = 93807.6/(10000 - H) * eZ[stunde] + 0.912018 # Maß für die zur Stunde durchstrahlte Luftmasse.
        I_stunde = S * np.exp(T/M_stunde)
        for i in range(len(listBT)):
            listBT[i].nX = -np.cos(listBT[i].Neigung * math.pi/180) * np.cos(listBT[i].Azimut * math.pi/180)
            listBT[i].nY = np.cos(listBT[i].Neigung * math.pi/180) * np.sin(listBT[i].Azimut * math.pi/180)
            listBT[i].nZ = np.sin(listBT[i].Neigung * math.pi/180)
            listBT[i].cosW_stunde = eX[stunde] * listBT[i].nX + eY[stunde] * listBT[i].nY + eZ[stunde] * listBT[i].nZ
            #listBT[i].red_strahlungDirekt_akt = 1 - math.pow((1 - listBT[i].cosW_stunde), listBT[i].eps)
            #listBT[i].red_strahlungDiffus_akt = (listBT[i].eps * (listBT[i].eps + 3)) / ((listBT[i].eps + 1) * (listBT[i].eps + 2))
            # print(listBT[i].cosW_stunde)
            # print(red_strahlungDirekt_akt)
            # print(red_strahlungDiffus_akt)
            if listBT[i].cosW_stunde > 0: 
                listBT[i].strahlungDirekt_akt = I_stunde * listBT[i].cosW_stunde
        
            else:
                listBT[i].strahlungDirekt_akt = 0
            kappa = 0.333   #Reitz'scher Trübungsfaktor laut 8110-3
            listBT[i].strahlungHimmel_akt = (kappa * (S - I_stunde) * eZ[stunde] * (1 + listBT[i].nZ) / 2)
            if listBT[i].strahlungHimmel_akt < 0:        #Fehler für negative Einträge vorerst abfangen
                listBT[i].strahlungHimmel_akt = 0
            listBT[i].strahlungReflex_akt = 0.2 * (I_stunde + kappa * (S - I_stunde)) * eZ[stunde] * ((1 - listBT[i].nZ) / 2)
            listBT[i].strahlungDiffus_akt = listBT[i].strahlungHimmel_akt + listBT[i].strahlungReflex_akt
            listBT[i].strahlungGlobal_akt = listBT[i].strahlungDirekt_akt + listBT[i].strahlungDiffus_akt

            #bis auf diese Ausgaben könnten alle anderen Variablen nur temporär in der Funktion existieren.
            listBT[i].strahlungDirekt_stunde.append(listBT[i].strahlungDirekt_akt)
            listBT[i].strahlungHimmel_stunde.append(listBT[i].strahlungHimmel_akt)
            listBT[i].strahlungReflex_stunde.append(listBT[i].strahlungReflex_akt)
            listBT[i].strahlungDiffus_stunde.append(listBT[i].strahlungDiffus_akt)
            listBT[i].strahlungGlobal_stunde.append(listBT[i].strahlungGlobal_akt)


#eX = np.array([0, 0, 0, 0, 0, 0, -0.442, -0.265, -0.088, 0.079, 0.224, 0.336, 0.409, 0.436, 0.417, 0.353, 0.247, 0.108, -0.056, -0.232, -0.410, 0, 0, 0, 0])
#eY = np.array([0, 0, 0, 0, 0, 0, 0.892, 0.929, 0.903, 0.816, 0.673, 0.484, 0.262, 0.023, -0.219, -0.445, -0.641, -0.793, -0.892, -0.929, -0.903, 0, 0, 0, 0])
#eZ = np.array([0, 0, 0, 0, 0, 0, 0.097, 0.257, 0.42, 0.573, 0.705, 0.808, 0.874, 0.9, 0.882, 0.823, 0.726, 0.599, 0.449, 0.288, 0.126, 0, 0, 0, 0])

#Fe01 = cl.Fenster('1', 'Fe01', 1.23, 1.48, 0, 1.1, 2.5, 0.65, 0.16, 180, 0)
#H = 172

#strahlungFenster(cl.Fenster.listBT, eX, eY, eZ, H)