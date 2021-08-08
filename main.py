from collections import OrderedDict
import util

fileLoc = input("Hello. Please enter txt file directory: ")    

#Read the file from given directory
try:
    f = open(fileLoc, "r")
except:
    print("Something gone wrong with the file")
    exit(1)

occurenceDict = dict()

#Calculate occurrences of letters
lines = []
for line in f:
    lines.append(line)
    line = line.rstrip('\n')
    for char in line:
        if char != " ":
            if char in occurenceDict.keys():
                occurenceDict[char] += 1
            else:
                occurenceDict[char] = 1

            
f.close()

#Find most occurring letter in the text.
letter, letterCount = util.mostOccurringItemInDict(occurenceDict)
print("Most occurring letter is",letter,"by",letterCount,"occurrences. (Most occurring letter in English is 'E')\n")

#Calculate frequency of each letter and print it on the console.
print("Frequency of each letter in the text")
print(util.calculateFrequencyAndOrder(occurenceDict, frequency=True),"\n")

occurenceWords = dict()

#Count each occurrence of the words
for line in lines:
    line = line.rstrip('\n')
    for word in line.split(" "):
        if word not in occurenceWords.keys():
            occurenceWords[word] = 1
        else:
            occurenceWords[word] += 1

#Find most occurring word in the text.
word, wordCount = util.mostOccurringItemInDict(occurenceWords)
print("Most occurring word is",word,"by",wordCount,"occurrences. (Most occurring word in English is 'THE')\n")

print("Words by length 1,2,3:")
for i in range(1,4):
    print("Length",i,":", util.findWordsByLength(occurenceWords, i))

print('\nFrom here, you will proceed in manual mode.')


decryptionDict = OrderedDict()
util.prettifyLines(lines)

tempLines = lines
while True:
    editMode = False

    print("\n*** ENTER: 0 0 -> EXIT  || ENTER: 1 1 -> EDIT ***")
    text, replacement = input("Please enter letters you want to change one space in between (FMT: letter replacement): ").split(" ")
    
    #Exit the program saving translated text and translation dictionary.
    if text == "0" and replacement == "0":
        f = util.getWriteFile("result.txt")
        f.writelines(tempLines)
        f.close()

        f = util.getWriteFile("decryptiondict.txt")
        
        f.write("***FORMAT: ENCRYPTED VALUE -> DECRYPTED EQUIVALENT***\n")
        for key, val in decryptionDict.items():
            string = key + " -> " + val.upper()+ "\n"
            f.write(string)

        f.close()

        print("Decrypted file has been saved to file named result.txt . Encryption dictionary has been saved to file named resultdict.txt .")
        break
    
    #Bu edit modu cok mantikli bir kodlama olmadi. buna tekrar bak.
    if text == "1" and replacement == "1":
        text, replacement = input("**EDIT MODE** Please enter letters you want to change with one space in between (FMT: letter replacement): ").split(" ")
        
        editMode = True

    if not editMode:   
        if replacement.lower() in decryptionDict.values():
            choice = input("\nYou have entered a replacement for this letter before. Do you want to change it? [y/n]: ").lower()
            if choice == "y":
                replace = input("\nSelected letter:"+ text.upper() +". What do you want new value to be?: ")
                tempLines = util.revert(tempLines, decryptionDict[text.upper()], replace)
                decryptionDict[text.upper()] = replace.lower()
            elif choice == "n":
                pass
            else:
                print("Not a valid choice!")
            
            continue

    prevState = tempLines
    if editMode:
        tempLines = util.replace(tempLines, text.lower(), replacement.lower())    
    else:
        tempLines = util.replace(tempLines, text.upper(), replacement.lower())
    
    print("\nAfter replacement, here is the text file: ")
    print(util.prettifyLines(tempLines))
    choice =input("\nDo you want to revert changes or proceed? [p(roceed)/r(evert)]: ")

    if choice == "p":
        #Add replacement into encryptionDict.
        if editMode:
            for key, val in decryptionDict.items():
                if decryptionDict[key] == text:
                    decryptionDict[key] == replacement.lower()
        else:
            decryptionDict[text.upper()] = replacement.lower()
    else: 
        tempLines = prevState
        print("\nAfter reverting the selection: ")
        print(util.prettifyLines(tempLines))
    
    del prevState