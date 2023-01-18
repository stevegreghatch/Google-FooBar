def solution(xs):
    # build and sort list of negatives and positives
    negatives = []
    positives = []
    for i in range(len(xs)):
        if xs[i] > 0:
            positives.append(xs[i])
        elif xs[i] < 0:
            negatives.append(abs(xs[i]))
    negatives.sort(reverse=True)
    positives.sort(reverse=True)
    
    # create outcome for each possibility
    numbersToMultiply = []
    outcome = 1
    
    # if each list has a number
    if len(negatives) > 0 and len(positives) > 0:
        # if odd number of negatives
        if len(negatives) % 2 != 0:
            # if more than one negative
            if len(negatives) > 1:
                # multiply all with exception of smallest negative
                for i in range(len(negatives)-1):
                    numbersToMultiply.append(negatives[i])
                for i in range(len(positives)):
                    numbersToMultiply.append(positives[i])
                for i in range(len(numbersToMultiply)):
                    outcome *= numbersToMultiply[i]
            # if only one negative
            else:
                # multiply all
                for i in range(len(negatives)):
                    numbersToMultiply.append(negatives[i])
                for i in range(len(positives)):
                    numbersToMultiply.append(positives[i])
                for i in range(len(numbersToMultiply)):
                    outcome *= numbersToMultiply[i]
        # if even number of negatives
        elif len(negatives) % 2 == 0:
            # multiply all
            for i in range(len(negatives)):
                numbersToMultiply.append(negatives[i])
            for i in range(len(positives)):
                numbersToMultiply.append(positives[i])
            for i in range(len(numbersToMultiply)):
                outcome *= numbersToMultiply[i]
    # if no negatives
    elif len(negatives) == 0:
        # if there is a positive number
        if len(positives) > 0:
            # multiply all positive numbers
            for i in range(len(positives)):
                numbersToMultiply.append(positives[i])
            for i in range(len(numbersToMultiply)):
                outcome *= numbersToMultiply[i]
        # if no positive numbers
        else:
            outcome = 0
    # if no positive numbers
    elif len(positives) == 0:
        # if there is a negative number
        if len(negatives) > 0:
            # if odd number of negatives
            if len(negatives) % 2 != 0:
                # if more than one negative
                if len(negatives) > 1:
                    # multiply all with exception of smallest negative
                    for i in range(len(negatives)-1):
                        numbersToMultiply.append(negatives[i])
                    for i in range(len(numbersToMultiply)):
                        outcome *= numbersToMultiply[i]
                # if original list contains a 0
                elif 0 in xs:
                    outcome = 0
                # if no 0 in original list
                else:
                    # use lowest negative number
                    outcome = negatives[len(negatives)-1] * -1
            # if even number of negatives
            if len(negatives) % 2 == 0:
                # multiply all
                for i in range(len(negatives)):
                    numbersToMultiply.append(negatives[i])
                for i in range(len(numbersToMultiply)):
                    outcome *= numbersToMultiply[i]
    
    stringToReturn = str(outcome)
    # print(stringToReturn)
    return stringToReturn
