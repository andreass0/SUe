#funcInputGeoTxt
#Function to read  input windows and create objects for the simulation

import classes as cl

def readInputFenster(fileName):
    file = open(fileName)
    fileLines = file.readlines()
    checkStart = 'FENSTER\n'
    checkEnd = 'ENDE\n'
    #counter = 0
    Fenster = {}  #dictionary für die Fenster

    for i in range(len(fileLines)):
        if str(fileLines[i]) == str(checkStart):
            i += 3
            while str(fileLines[i]) != str(checkEnd):
                a = fileLines[i]
                try:
                    int(a[0])
                    str(a[0])
                except:
                    i += 1
                a = fileLines[i].split(", ")
                a[len(a) - 1] = a[len(a) - 1].replace('\n', '')
                Fenster[a[1]] = cl.Fenster(a[0], a[1], float(a[2]), float(a[3]), float(a[4]), float(a[5]), float(a[6]), float(a[7]), float(a[8]), float(a[9]), float(a[10]), float(a[11]))
                #counter += 1
                i += 1
    return Fenster


#print(len(fileLines[0]))

#Fenster = {}

#fileName = 'InputGeo.txt'

###a = readInputSchichten(fileName)
#Fenster = readInputFenster(fileName)
#end = True