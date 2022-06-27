l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
lSolution = ['0.1', '1.1.1', '1.2', '1.2.1', '1.11', '2', '2.0', '2.0.0']

# split strings by decimal and convert each to int
splitStringsArray = []
for i in range(len(l)):
    stringToLookAt = str(l[i])
    splitString = stringToLookAt.split('.')
    for j in range(len(splitString)):
        splitString[j] = int(splitString[j])
    splitStringsArray.append(splitString)
    
# sort occurances
sortedArray = sorted(splitStringsArray)
    
# convert back to string list and join splits
for i in range(len(sortedArray)):
    listToConvert = sortedArray[i]
    for j in range(len(listToConvert)):
        listToConvert[j] = str(listToConvert[j])
    sortedArray[i] = ".".join(listToConvert)
    
return sortedArray
