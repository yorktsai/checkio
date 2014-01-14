# http://www.checkio.org/mission/x-o-referee/

def checkio(game_result):
    size = len(game_result)

    for i in range(0, size):
        for j in range(0, size):
            if game_result[i][j] == ".":
                continue
                
            if i == 0 and j == 0:
                matched = True
                for k in range(1, size):
                    if game_result[k][k] != game_result[i][j]:
                        matched = False
                        break
                if matched:
                    return game_result[i][j]
                    
            if i == 0:
                matched = True
                for k in range(1, size):
                    if game_result[k][j] != game_result[i][j]:
                        matched = False
                        break
                if matched:
                    return game_result[i][j]
                    
            if j == 0:
                matched = True
                for k in range(1, size):
                    if game_result[i][k] != game_result[i][j]:
                        matched = False
                        break
                if matched:
                    return game_result[i][j]
                    
            if i == 0 and j == size - 1:
                matched = True
                for k in range(1, size):
                    if game_result[i+k][j-k] != game_result[i][j]:
                        matched = False
                        break
                if matched:
                    return game_result[i][j]

    return "D"

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
