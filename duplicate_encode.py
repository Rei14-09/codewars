def duplicate_encode(word):
    res = ''
    word=word.upper()
    
    for leter in word:
        if word.count(leter) == 1:
            res += '('
        elif word.count(leter) != 1:
            res += ')'
        

    return res
