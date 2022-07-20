from collections import deque

# map1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
# map1Solution = 7
# map2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# map2Solution = 11

# map = map1

def solution(map):

    # 4 possible directions
    possibleDirections = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # breadth-first search function
    def bfs(row, col, map):
        rows = len(map)
        cols = len(map[0])
        pathValues = []
        # populate pathValues array with 'None' values
        for i in range(rows):
            pathValues.append([None] * cols)
        # input '1' at start and end location
        pathValues[row][col] = 1
        # initialize queue
        queue = deque()
        # append start and end location to queue
        queue.append((row, col))

        # queue tracks optimal path
        while queue:
            row, col = queue.popleft()
            # populate number of moves from start to end and end to start
            for pDrow, pDcol in possibleDirections:
                newRow, newCol = (row + pDrow, col + pDcol)
                # if move is with bounds and array at location is currenlty unpopulated
                if 0 <= newRow < rows and 0 <= newCol < cols and pathValues[newRow][newCol] is None:
                    # increase value at new location
                    pathValues[newRow][newCol] = pathValues[row][col] + 1
                    # if new location is not a wall
                    if map[newRow][newCol] != 1:
                        # append to queue
                        queue.append((newRow, newCol))
        return pathValues

    # continuation of main function
    rows = len(map)
    cols = len(map[0])
    startToEnd = bfs(0, 0, map)
    endToStart = bfs(rows - 1, cols - 1, map)
    # height and width ranges from 2 to 20 --- highest max = 20 * 20 + 1
    pathLength = 20 * 20 + 1
    for i in range(rows):
        for j in range(cols):
            # get matching location
            if startToEnd[i][j] and endToStart[i][j]:
                # get path length
                pathLength = min(pathLength, startToEnd[i][j] + endToStart[i][j] - 1)
                # return if match
                if pathLength == rows + cols - 1:
                    return pathLength
    # return lowest path
    return pathLength

# solution(map)
