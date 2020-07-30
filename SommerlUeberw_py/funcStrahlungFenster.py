
import math
import numpy as np
import classes as cl

#Funktion zur Berechnung der globalen Strahlung pro Stunde für Fenster
def strahlungFenster(listFe, eX, eY, eZ, H):
    for stunde in range(25):
        T = 4.5     #Linke'sche Trübungsfaktor T = 4,5 lt. B8110-3 (Stand 2020)
        S = 1322.4  #Normalstrahlungsintensität in W/m²
        M_stunde = 93807.6/(10000 - H) * eZ[stunde] + 0.912018 # Maß für die zur Stunde durchstrahlte Luftmasse.
        I_stunde = S * np.exp(T/M_stunde)
        for i in range(len(listFe)):
            listFe[i].nX = -np.cos(listFe[i].Neigung * math.pi/180) * np.cos(listFe[i].Azimut * math.pi/180)
            listFe[i].nY = np.cos(listFe[i].Neigung * math.pi/180) * np.sin(listFe[i].Azimut * math.pi/180)
            listFe[i].nZ = np.sin(listFe[i].Neigung * math.pi/180)
            listFe[i].cosW_stunde = eX[stunde] * listFe[i].nX + eY[stunde] * listFe[i].nY + eZ[stunde] * listFe[i].nZ
            listFe[i].red_strahlungDirekt_akt = 1 - math.pow((1 - listFe[i].cosW_stunde), listFe[i].eps)
            listFe[i].red_strahlungDiffus_akt = (listFe[i].eps * (listFe[i].eps + 3)) / ((listFe[i].eps + 1) * (listFe[i].eps + 2))
            # print(listFe[i].cosW_stunde)
            # print(red_strahlungDirekt_akt)
            # print(red_strahlungDiffus_akt)
            if listFe[i].cosW_stunde > 0: 
                listFe[i].strahlungDirekt_akt = I_stunde * listFe[i].cosW_stunde * listFe[i].red_strahlungDirekt_akt
        
            else:
                listFe[i].strahlungDirekt_akt = 0
            kappa = 0.333   #Reitz'scher Trübungsfaktor laut 8110-3
            listFe[i].strahlungHimmel_akt = (kappa * (S - I_stunde) * eZ[stunde] * (1 + listFe[i].nZ) / 2)
            if listFe[i].strahlungHimmel_akt < 0:        #Fehler für negative Einträge vorerst abfangen
                listFe[i].strahlungHimmel_akt = 0
            listFe[i].strahlungReflex_akt = 0.2 * (I_stunde + kappa * (S - I_stunde)) * eZ[stunde] * ((1 - listFe[i].nZ) / 2)
            listFe[i].strahlungDiffus_akt = (listFe[i].strahlungHimmel_akt + listFe[i].strahlungReflex_akt) * listFe[i].red_strahlungDiffus_akt
            listFe[i].strahlungGlobal_akt = listFe[i].strahlungDirekt_akt + listFe[i].strahlungDiffus_akt

            #bis auf diese Ausgaben könnten alle anderen Variablen nur temporär in der Funktion existieren.
            listFe[i].strahlungDirekt_stunde.append(listFe[i].strahlungDirekt_akt)
            listFe[i].strahlungHimmel_stunde.append(listFe[i].strahlungHimmel_akt)
            listFe[i].strahlungReflex_stunde.append(listFe[i].strahlungReflex_akt)
            listFe[i].strahlungDiffus_stunde.append(listFe[i].strahlungDiffus_akt)
            listFe[i].strahlungGlobal_stunde.append(listFe[i].strahlungGlobal_akt)


#eX = np.array([0, 0, 0, 0, 0, 0, -0.442, -0.265, -0.088, 0.079, 0.224, 0.336, 0.409, 0.436, 0.417, 0.353, 0.247, 0.108, -0.056, -0.232, -0.410, 0, 0, 0, 0])
#eY = np.array([0, 0, 0, 0, 0, 0, 0.892, 0.929, 0.903, 0.816, 0.673, 0.484, 0.262, 0.023, -0.219, -0.445, -0.641, -0.793, -0.892, -0.929, -0.903, 0, 0, 0, 0])
#eZ = np.array([0, 0, 0, 0, 0, 0, 0.097, 0.257, 0.42, 0.573, 0.705, 0.808, 0.874, 0.9, 0.882, 0.823, 0.726, 0.599, 0.449, 0.288, 0.126, 0, 0, 0, 0])

#Fe01 = cl.Fenster('1', 'Fe01', 1.23, 1.48, 0, 1.1, 2.5, 0.65, 0.16, 180, 0)
#H = 172

#strahlungFenster(cl.Fenster.listFe, eX, eY, eZ, H)