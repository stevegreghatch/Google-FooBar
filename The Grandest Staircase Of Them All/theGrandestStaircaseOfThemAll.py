def solution(n):
    # construct matrix of n+1 number of n+1 '0' lists
    totalCombinations = []
    for i in range(n+1):
        innerList = []
        for j in range(n+1):
            innerList.append(0)
        totalCombinations.append(innerList)
      
    # set first example in matrix  
    totalCombinations[0][0] = 1
    
    # populate totalCombinations matrix
    for i in range(1, n + 1):
	    for j in range(0, n + 1):
	        totalCombinations[i][j] = totalCombinations[i - 1][j]
	        if j >= i:
	            totalCombinations[i][j] += totalCombinations[i - 1][j - i]
	            
	# get appliciable number from matrix to return            
    return totalCombinations[n][n] - 1
