# http://www.checkio.org/mission/brackets/

def checkio(expr):
    stack = []
    for c in expr:
        if c in set(["{", "[", "("]):
            stack.append(c)
            
        if c == "}":
            if len(stack) <= 0 or stack[-1] != "{":
                return False
            stack.pop()
            
        if c == "]":
            if len(stack) <= 0 or stack[-1] != "[":
                return False
            stack.pop()
            
        if c == ")":
            if len(stack) <= 0 or stack[-1] != "(":
                return False
            stack.pop()
    
    if len(stack) > 0:
        return False
    
    #replace this for solution
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"

