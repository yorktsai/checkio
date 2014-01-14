def s(vec, index, total):
    if index >= len(vec):
        return total
        
    return s(vec, index+1, total+vec[index])

def checkio(data):
    return s(data, 0, 0)

