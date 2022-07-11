# attempt 1 --- using itertools

import itertools

def solution(l):
    
    l = list(sorted(array1, reverse=True))

    possibleCombinations = []

    for i in range(len(l)):
        numberToAppend = str(l[i])
        possibleCombinations.append(numberToAppend)
        if i > 1:
            createdList = list(itertools.permutations(l, i+1))
            for j in range(len(createdList)):
                numberToAppend = ''
                for k in range(len(createdList[j])):
                    numberToAppend += str(createdList[j][k])
                if numberToAppend not in possibleCombinations:
                    possibleCombinations.append(numberToAppend)

    numbersDivisibleBy3 = []

    for i in range(len(possibleCombinations)):
        numberToCheck = int(possibleCombinations[i])
        if numberToCheck % 3 == 0:
            numbersDivisibleBy3.append(numberToCheck)
        
    print(max(numbersDivisibleBy3))
    # return max(numbersDivisibleBy3)

    
# attempt 2 without imports
    
