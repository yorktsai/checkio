def check(matrix, x, y, dx, dy):
    v = matrix[x][y]
    for i in range(0, 3):
        x += dx
        y += dy
        if x >= len(matrix) or x < 0:
            return False
            
        if y >= len(matrix[0]) or y < 0:
            return False
            
        if matrix[x][y] != v:
            return False
            
    return True

def checkio(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if check(matrix, i, j, 0, 1):
                return True
                
            if check(matrix, i, j, 1, 1):
                return True
                
            if check(matrix, i, j, 1, 0):
                return True
                
            if check(matrix, i, j, 1, -1):
                return True
    
    #replace this for solution
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

