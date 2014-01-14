# http://www.checkio.org/mission/sentence-with-extra-spaces/

#Your optional code here
#You can import some modules or create additional functions

import re

def checkio(line):
    #Your code goes here
    #This is the main function.
    #It's must return the result for auto-testing, so don't remove it!

    line = re.sub("-+", "-", line)

    #replace this with your solution
    return line

#Some hints
#you can use split and join methods from string.
#If you used replace() -- don't forget about three or four dashes
#Maybe regexp

#These "asserts" using only for self-checking and not necessary for auto-testing    
if __name__ == '__main__':
    assert checkio('I---like--python') == "I-like-python", 'Example'

