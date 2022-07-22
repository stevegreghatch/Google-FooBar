# n1 = '15'
# n1S = 5
# n2 = '4'
# n2S = 2

# n = '11'

def solution(n):
    possibleNumbersTotal = []
    possibleNumbers = []
    n = int(n)
    possibleNumbers.append(n)

    def function(n):
        # print('original: ' + str(n))
        while n != 1:
            if n % 2 == 0:
                n = int(n/2)
                possibleNumbers.append(n)
                # print('divided: ' + str(n))
            else:
                options = []
                options.append(n+1)
                options.append(n-1)
                # print('options: ' + str(options))
                for i in range(len(options)):
                    if i == 0:
                        possibleNumbers.append(n+1)
                    elif i == 1:
                        possibleNumbers.append(n-1)

                    function(options[i])
                    
                    if possibleNumbers not in possibleNumbersTotal:
                        # print('possibleNumbers: ' + str(possibleNumbers))
                        possibleNumbersTotal.append(possibleNumbers.copy())
                        numbersToCarryOver = []
                        for j in range(len(possibleNumbers)):
                            if j < possibleNumbers.index(options[i]):
                                numbersToCarryOver.append(possibleNumbers[j])
                        # print('numbersToCarryOver: ' + str(numbersToCarryOver))
                        possibleNumbers.clear()
                        for j in range(len(numbersToCarryOver)):
                            possibleNumbers.append(numbersToCarryOver[j])
                        # print('moved to next number')
                    else:
                        return
    
    function(n)
    
    if possibleNumbersTotal != []:
        print('possibleNumbersTotal: ' + str(possibleNumbersTotal))
        possibleCounts = []
        for i in range(len(possibleNumbersTotal)):
            possibleCounts.append(len(possibleNumbersTotal[i]))
        numberToReturn = min(possibleCounts) - 1
    else:
        numberToReturn = len(possibleNumbers) - 1
        
    print('numberToReturn: ' + str(numberToReturn))
    return numberToReturn

solution(n)
