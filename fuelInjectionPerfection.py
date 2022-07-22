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
                    
                    count = len(possibleNumbers)
                    
                    if len(possibleNumbersTotal) > 0:
                        if count >= possibleNumbersTotal[0]:
                            # print('rejecting set:' + str(possibleNumbers))
                            return
                        
                        # print('possibleNumbers: ' + str(possibleNumbers))
                        possibleNumbersTotal.append(count)
                        numbersToCarryOver = []
                        for j in range(possibleNumbers.index(options[i])):
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
        # print('\npossibleNumbersTotal: ' + str(possibleNumbersTotal))
        numberToReturn = possibleNumbersTotal[0] - 1
    else:
        numberToReturn = len(possibleNumbers) - 1
        
    # print('numberToReturn: ' + str(numberToReturn))
    return numberToReturn
