lines = open("D1_Input.txt").readlines()
elvesDict = {}
elfNumber = 1
calories = 0
highestScore = 0
theElf = 0
topThree = 0



for line in lines:
    if line != "\n":
        calories += int(line)
    else:
        elvesDict.update({elfNumber: calories})
        elfNumber += 1
        calories = 0
        
for elf in elvesDict:
    if elvesDict[elf] > highestScore:
        highestScore = elvesDict[elf]
        theElf = elf    
        
ordereddict = dict(sorted(elvesDict.items(), key=lambda item: item[1]))
dictLength = len(ordereddict)
topThreeValues = list(ordereddict.values())[-3:]
print('Top three values are: ' + str(topThreeValues))
for value in topThreeValues:
    topThree += value
print('Sum of top three values: ' + str(topThree))
print('The highest calories score: '+ str(highestScore))
print("The elf with the highest score: " + str(theElf))
        

    
