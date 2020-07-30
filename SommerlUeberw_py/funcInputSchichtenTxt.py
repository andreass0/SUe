#funcInputSchichtenTxt
#Function read the input layers and create the objects for the simulation

import classes as cl

def readInputSchichten(fileName):
    file = open(fileName)
    fileLines = file.readlines()
    checkStart = 'AUSSEN\n'
    checkEnd = 'INNEN\n'
    #counter = 0
    Schichten = {}  #dictionary für die Schichten

    for i in range(len(fileLines)):
        if str(fileLines[i]) == str(checkStart):
            i += 2
            while str(fileLines[i]) != str(checkEnd):
                a = fileLines[i]
                try:
                    int(a[0])
                    str(a[0])
                except:
                    i += 1
                a = fileLines[i].split(", ")
                a[len(a) - 1] = a[len(a) - 1].replace('\n', '')
                Schichten[a[1]] = cl.Schicht(a[0], a[1], float(a[2]), float(a[3]), float(a[4]), float(a[5]))
                #counter += 1
                i += 1
    return Schichten


#print(len(fileLines[0]))

#SchichtenDict = {}

#fileName = 'InputAufbauten.txt'

##a = readInputSchichten(fileName)
#SchichtenDict = readInputSchichten(fileName)
#end = True