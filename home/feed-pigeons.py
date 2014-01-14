# http://www.checkio.org/mission/feed-pigeons/solve/

def checkio(number):
    round = 1
    pigeons = 1
    while number >= pigeons:
        number -= pigeons
        round += 1
        pigeons += round
        
    return max(pigeons - round, number)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
