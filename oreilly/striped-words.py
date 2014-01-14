import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()
    tokens = re.split("[^A-Z0-9]+", text)
    
    count = 0
    for token in tokens:
        if len(token) <= 1 or not token.isalpha():
            continue

        is_valid = True
        for i in range(0, len(token)-1):
            if VOWELS.find(token[i]) != -1 and VOWELS.find(token[i+1]) != -1:
                is_valid = False
                break

            if CONSONANTS.find(token[i]) != -1 and CONSONANTS.find(token[i+1]) != -1:
                is_valid = False
                break

        if is_valid:
            count += 1

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

