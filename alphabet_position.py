def alphabet_position(text):
    result = []
    
    for letter in text:
        if letter.isalpha():
            result.append(str(ord(letter.lower()) -96))
            
    return " ".join(result)
