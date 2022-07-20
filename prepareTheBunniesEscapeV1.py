# map1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map1Solution = 7
# map2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map2Solution = 11

# map = map2

def solution(map):
    
    currentLocation = (0,0)
    endLocation = (len(map)-1, len(map[len(map)-1])-1)
    
    count = 1

    for i in range(len(map)):
        if i < len(map)-1:
            # print('currentLocation: ' + str(currentLocation))
            # print('original row: ' + str(map[i]))
            # two possbile moves -- right or down
            validMoves = []
            if (currentLocation[1] + 1) < len(map[i]):
                possibleMove1 = (i, currentLocation[1] + 1)
            else:
                possibleMove1 = (-1, -1)
            if i + 1 < len(map):
                possibleMove2 = (i+1, currentLocation[1])
            else:
                possibleMove2 = (-1, -1)
            if map[possibleMove1[0]] [possibleMove1[1]] == 0 and possibleMove1 != (-1,-1):
                validMoves.append(possibleMove1)
            if map[possibleMove2[0]] [possibleMove2[1]] == 0 and possibleMove2 != (-1,-1):
                validMoves.append(possibleMove2)
            # if i < len(map)-1:
                # print('next row:     ' + str(map[i+1]))
            # print('possibleMove1/move right: ' + str(possibleMove1))
            # print('possibleMove2/move down: ' + str(possibleMove2))
            # print('validMoves: ' + str(validMoves))
            if len(validMoves) == 1:
                # if valid move is on current row
                previousRow = currentLocation[0]
                currentLocation = validMoves[0]
                newRow = currentLocation[0]
                while previousRow == newRow:
                    count += 1
                    # print("current count: " + str(count))
                    # print('\nstaying on same row')
                    # print('currentLocation: ' + str(currentLocation))
                    # print('original row: ' + str(map[i]))
                    # two possbile moves -- right or down
                    validMoves = []
                    if (currentLocation[1] + 1) < len(map[i]):
                        possibleMove1 = (i, currentLocation[1] + 1)
                    else:
                        possibleMove1 = (-1, -1)                    
                    if i + 1 < len(map):
                        possibleMove2 = (i+1, currentLocation[1])
                    else:
                        possibleMove2 = (-1, -1)
                    if map[possibleMove1[0]] [possibleMove1[1]] == 0 and possibleMove1 != (-1,-1):
                        validMoves.append(possibleMove1)
                    if map[possibleMove2[0]] [possibleMove2[1]] == 0 and possibleMove2 != (-1,-1):
                        validMoves.append(possibleMove2)
                    # if i < len(map)-1:
                        # print('next row:     ' + str(map[i+1]))
                    # print('possibleMove1/move right: ' + str(possibleMove1))
                    # print('possibleMove2/move down: ' + str(possibleMove2))
                    # print('validMoves: ' + str(validMoves))
                    if len(validMoves) == 1:
                        # if valid move is on current row
                        previousRow = currentLocation[0]
                        currentLocation = validMoves[0]
                        newRow = currentLocation[0]

            count += 1
            # print("current count: " + str(count))
            # print('\n')
            
            if currentLocation == endLocation:
                numberToReturn = count
                # print("final count: " + str(numberToReturn))
                # return
                return numberToReturn
        
# solution(map)
