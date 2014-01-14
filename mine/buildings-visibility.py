def get_visible_parts(b1, b2):
    if b2[4] < b1[4]:
        return [b1]
        
    if b2[3] > b1[1]:
        return [b1]
        
    if b2[0] > b1[2]:
        return [b1]
        
    if b2[2] < b2[0]:
        return [b1]
        
    if b2[0] <= b1[0] and b2[2] >= b1[2]:
        return []

    if b2[0] <= b1[0] and b2[2] < b1[2]:
        return [[max(b1[0], b2[2]), b1[1], b1[2], b1[3], b1[4]]]

    if b2[0] > b1[0] and b2[2] >= b1[2]:
        return [[b1[0], b1[1], min(b1[2], b2[0]), b1[3], b1[4]]]
        
    if b2[0] > b1[0] and b2[2] < b1[2]:
        return [[b1[0], b1[1], b2[0], b1[3], b1[4]],
                [b2[2], b1[1], b1[2], b1[3], b1[4]],]
                
    return []

def checkio(buildings):
    count = 0
    for i in range(0, len(buildings)):
        visibles = [buildings[i]]
        for j in range(0, len(buildings)):
            if i == j:
                continue
                
            new_visibles = []
            for part in visibles:
                visible_parts = get_visible_parts(part, buildings[j])
                for vp in visible_parts:
                    new_visibles.append(vp)
                    
            visibles = new_visibles
            if len(visibles) == 0:
                break;
                
        if len(visibles) > 0:
            count += 1
        
    return count


if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
