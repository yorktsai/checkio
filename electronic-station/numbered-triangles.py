import itertools

def chips_sum(chips):
    for i in range(0, 5):
        if chips[i][2] != chips[i+1][0]:
            return 0

    if chips[5][2] != chips[0][0]:
        return 0

    sum = 0
    for i in range(0, 6):
        sum += chips[i][1]

    return sum

def find(currents, remains):
    if len(remains) == 0:
        return chips_sum(currents)

    max_sum = 0

    for remain_index in range(0, len(remains)):
        part = remains[remain_index]
        for p in itertools.permutations(part):
            if len(currents) > 0 and currents[-1][2] != p[0]:
                continue

            new_currents = currents[:]
            new_currents.append(p)

            new_remains = remains[:]
            new_remains.pop(remain_index)

            max_sum = max(max_sum, find(new_currents, new_remains))

    return max_sum

def checkio(chips):
    return find([], chips)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"

