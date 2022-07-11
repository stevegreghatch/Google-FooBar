import itertools

def solution(l):
    
    l = list(sorted(l, reverse=True))

    possibleCombinations = []

    for i in range(len(l)):
        # start by appending single digit
        numberToAppend = str(l[i])
        possibleCombinations.append(numberToAppend)
        
        # create a list of possible combinations over each iteration
        # first with 2 digits, then 3 digits etc. up to total list length
        createdList = list(itertools.combinations(l, i+1))
        
        for j in range(len(createdList)):
            # create string of number from each combination
            numberToAppend = ''
            for k in range(len(createdList[j])):
                numberToAppend += str(createdList[j][k])
            # filter out combinations already seen
            if numberToAppend not in possibleCombinations:
                possibleCombinations.append(numberToAppend)

    numbersDivisibleBy3 = []

    for i in range(len(possibleCombinations)):
        # convert each string number to int
        numberToCheck = int(possibleCombinations[i])
        # check if number is divisble by 3
        if numberToCheck % 3 == 0:
            numbersDivisibleBy3.append(numberToCheck)
            
    numberToReturn = 0;
    
    # return value if a number is divisible by 3
    if numbersDivisibleBy3 != []:
        numberToReturn = max(numbersDivisibleBy3)
    
    print(numberToReturn)
    return numberToReturn
