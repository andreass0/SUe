#funcInputGeoTxt
#Function to read geometric input parameters for the simulation

def readInputGeo(fileName, parameterName):
    file = open(fileName)
    fileLines = file.readlines()

    for i in range(len(fileLines)):
        if str(fileLines[i]) == str(parameterName):
            a = fileLines[i+1].split(", ")
            a[len(a) - 1] = a[len(a) - 1].replace('\n', '')
    return a


#print(len(fileLines[0]))

#fileName = 'GeoInput.txt'
#a = readGeoInput(fileName, 'w1\n')[1]

#end = True