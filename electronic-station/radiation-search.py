def checkio(matrix):
    # init
    used = []
    for i in range(0, len(matrix)):
        used.append([])
        for j in range(0, len(matrix[0])):
            used[i].append(0)
    
    max_count = 1
    max_num = matrix[0][0]
    
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            if 1 == used[x][y]:
                continue
                
            used[x][y] = 1
            
            stack = []
            stack.append([x, y])
            parent = [x, y]
            count = 0
            
            while len(stack) > 0:
                loc = stack.pop()
                i = loc[0]
                j = loc[1]
                count += 1
                if i-1 >= 0 and matrix[i-1][j] == matrix[i][j] and 0 == used[i-1][j]:
                    used[i-1][j] = 1
                    stack.append([i-1, j])
                    
                if i+1 < len(matrix) and matrix[i+1][j] == matrix[i][j] and 0 == used[i+1][j]:
                    used[i+1][j] = 1
                    stack.append([i+1, j])
                    
                if j-1 >= 0 and matrix[i][j-1] == matrix[i][j] and 0 == used[i][j-1]:
                    used[i][j-1] = 1
                    stack.append([i, j-1])
                    
                if j+1 < len(matrix[0]) and matrix[i][j+1] == matrix[i][j] and 0 == used[i][j+1]:
                    used[i][j+1] = 1
                    stack.append([i, j+1])
                    
            if count > max_count:
                max_count = count
                max_num = matrix[parent[0]][parent[1]]
                
    #replace this for solution
    return [max_count, max_num]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'
