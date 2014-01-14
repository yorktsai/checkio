# http://www.checkio.org/mission/speechmodule/

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    parts = []

    hundred = number // 100
    if hundred > 0:
        parts.append(FIRST_TEN[hundred])
        parts.append(HUNDRED)
        
    ten = number % 100
    if ten >= 10 and ten <= 19:
        parts.append(SECOND_TEN[ten - 10])
        
        return " ".join(parts)
        
    ten_part = ten // 10
    if ten_part > 1:
        parts.append(OTHER_TENS[ten_part - 2])
        
    ten_part_2 = ten % 10
    if ten_part_2 > 0:
        parts.append(FIRST_TEN[ten_part_2])
        
    return " ".join(parts)

#Some hints
#Don't forget strip whitespaces at the end of string


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"

