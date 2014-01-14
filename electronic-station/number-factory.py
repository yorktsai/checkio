# http://www.checkio.org/mission/number-factory/

def checkio(data):
    nums = []
    while data > 9:
        found = False
        for i in range(9, 1, -1):
            if data % i == 0:
                found = True
                nums.append(i)
                data = data // i
                break

        if found is False:
            return 0

    nums.append(data)

    rt = ""
    for num in sorted(nums):
        rt += str(num)

    return int(rt)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(5) == 5, "5th example"

