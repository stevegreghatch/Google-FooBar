def solution(s):
    letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    braille = ['000000', '100000', '110000', '100100', '100110', '100010', '110100', '110110', '110010', '010100', '010110', '101000', '111000', '101100', '101110', '101010', '111100', '111110', '111010', '011100', '011110', '101001', '111001', '010111', '101101', '101111', '101011']
    outputString = ''
    
    inputList = list(s)

    for i in range(len(inputList)):
        if inputList[i].isupper():
            outputString += '000001'
            inputList[i] = inputList[i].lower()
        indexToLookFor = letters.index(inputList[i])
        stringToAdd = braille[indexToLookFor]
        outputString += stringToAdd

    return outputString
