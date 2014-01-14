# http://www.checkio.org/mission/house-password/

def checkio(data):

    if len(data) < 10:
        return False

    is_digit = False
    is_upper = False
    is_lower = False
    
    for c in data:
        if c.isdigit():
            is_digit = True
        elif c.isupper():
            is_upper = True
        elif c.islower():
            is_lower = True
                
        if is_digit and is_upper and is_lower:
            return True

    #replace this for solution
    return False

#Some hints
#Just check all conditions


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

