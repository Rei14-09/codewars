def first_dup(prase):
    
    for letter in prase:
        if prase.count(letter) > 1:
            return f'{letter}'
    return None
