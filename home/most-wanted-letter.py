# http://www.checkio.org/mission/most-wanted-letter/

from collections import OrderedDict

def checkio(text):

    counter = {}
    for c in text:
        if not c.isalpha():
            continue
        
        if not c in counter:
            counter[c] = 0
            
        counter[c] += 1
        
    result = sorted(counter.items(), key=lambda t: t[1], reverse=True)
    
    max = result[0][1]
    letter = result[0][0]
    
    for iteritem in result:
        if iteritem[1] < max:
            break
            
        if iteritem[0].lower() < letter:
            letter = iteritem[0]
    
    return letter

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."

