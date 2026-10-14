def to_camel_case(text):
    new_text = ''
    mayuscula = False

    for letra in text:
        if letra.isalpha():
            if mayuscula:
                new_text += letra.upper()
                mayuscula = False
            else:
                new_text += letra
        else:
            mayuscula = True

    return new_text
