def solution(n):
    possibleNumbersTotal = []
    possibleNumbers = []
    n = int(n)
    possibleNumbers.append(n)

    def function(n):
        while n != 1:
            if n % 2 == 0:
                n = int(n/2)
                possibleNumbers.append(n)
            else:
                options = []
                options.append(n+1)
                options.append(n-1)
                for i in range(len(options)):
                    if i == 0:
                        possibleNumbers.append(n+1)
                    elif i == 1:
                        possibleNumbers.append(n-1)

                    function(options[i])
                    
                    if possibleNumbers not in possibleNumbersTotal:
                        possibleNumbersTotal.append(possibleNumbers.copy())
                        numbersToCarryOver = []
                        for j in range(len(possibleNumbers)):
                            if j < possibleNumbers.index(options[i]):
                                numbersToCarryOver.append(possibleNumbers[j])
                        possibleNumbers.clear()
                        for j in range(len(numbersToCarryOver)):
                            possibleNumbers.append(numbersToCarryOver[j])
                    else:
                        return
    
    function(n)
    
    if possibleNumbersTotal != []:
        possibleCounts = []
        for i in range(len(possibleNumbersTotal)):
            possibleCounts.append(len(possibleNumbersTotal[i]))
        numberToReturn = min(possibleCounts) - 1
    else:
        numberToReturn = len(possibleNumbers) - 1
        
    return numberToReturn
