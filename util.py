alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def mostOccurringItemInDict(myDict):
    mostOccurring = None
    timesOccured = 0
    for key,val in myDict.items():
        if val > timesOccured:
            mostOccurring = key
            timesOccured = val
    
    return mostOccurring, timesOccured

def findWordsByLength(myDict, length):
    newDict = dict()
    for key,val in myDict.items():
        if len(str(key)) == length:
            newDict[key] = val

    return newDict

def prettifyLines(lines):
    for line in lines:
        if line != None:
            print(line)

def replace(lines, letter, replacement):
    for index,line in enumerate(lines):
        lines[index] = line.replace(letter, replacement)
    
    return lines

def getWriteFile(fileName):
    try:
        f = open(fileName,"x")
    except:
        f = open(fileName,"w")

    return f

def calculateFrequencyAndOrder(dictionary, frequency=True):
    if frequency:
        #Calculate total num of letters.
        totalOccurence = 0
        for val in dictionary.values():
            totalOccurence += val
    
    #Convert dictionary to list in order to be able to sort values.
    dictAsList = list(dictionary.items())
    if frequency:
        for index, item in enumerate(dictAsList):
            dictAsList[index] = [item[0], round(item[1]/totalOccurence,4)]
    
    #Sort the list.
    for index,item in enumerate(dictAsList):
        maxVal = item[1]
        maxIndex = index
        for otheritemindex in range(index+1, len(dictAsList)):
            if maxVal < dictAsList[otheritemindex][1]:
                maxVal = dictAsList[otheritemindex][1]
                maxIndex = otheritemindex
        
        swap = dictAsList[index]
        dictAsList[index] = dictAsList[maxIndex]
        dictAsList[maxIndex] = swap

    #Create another dictionary and put sorted items inside.       
    resultDict = {}
    for item in dictAsList:
        resultDict[item[0]] = item[1]
    
    return resultDict
    