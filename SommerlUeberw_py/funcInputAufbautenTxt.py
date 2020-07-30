#funcInputAufbautenTxt
#Function to read input parts and create objects for the simulation

def readInputAufbauten(fileName, parameterName):
    file = open(fileName)
    fileLines = file.readlines()

    for i in range(len(fileLines)):
        if str(fileLines[i]) == str(parameterName):
            a = fileLines[i+1].split(", ")
            a[len(a) - 1] = a[len(a) - 1].replace('\n', '')
    return a


#print(len(fileLines[0]))

#fileName = 'InputAufbauten.txt'
#a = readInputAufbauten(fileName, 'aufbauW1\n')
#end = True