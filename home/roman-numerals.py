# http://www.checkio.org/mission/roman-numerals/

def checkio(data):
    nums = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ]
    
    rt = ""
    for pair in nums:
        num = pair[0]
        ch = pair[1]
        
        if data // num > 0:
            for i in range(0, data // num):
                rt += ch
            data %= num
            
    return rt

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
