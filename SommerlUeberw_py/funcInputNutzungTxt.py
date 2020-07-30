#funcReadInputTxt
#Function to read input Parameters for the simulations

import json

def readInputNutzung(fileName, parameterName):
    file = open(fileName)
    fileLines = file.readlines()

    for i in range(len(fileLines)):
        if str(fileLines[i]) == str(parameterName):
            a = json.loads(fileLines[i+1])
            print(a)
    return a
        #for k in range(len(fileLines[i])):
        #    if fileLines[i][k] == '[':
        #        while True:
        #            k += 1
        #            if fileLines[i][k] == ']':
        #                break
        #            a.append(fileLines[i][k])
    #return a
            #elif fileLines[i][k] == ']':
            #    print(fileLines[i][k])
            #    break

#print(len(fileLines[0]))

#fileName = 'Input.txt'
#scheduleFeLueftung = 'scheduleFeLueftung\n'
#a = readInput(fileName, 'scheduleFeLueftung\n')

#end = True