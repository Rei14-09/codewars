def freq_seq(s, sep):
    
    resultado = []
    
    for caracter in s:
        tirada = str(s.count(caracter))
        resultado.append(tirada)
        
    return  sep.join(resultado)
