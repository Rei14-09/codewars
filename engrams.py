def anagrams(word, word_list):
    solution = []
    
    objetivo_ordenado = sorted(word.lower())
    
    for palabra in word_list:
        if sorted(palabra.lower()) == objetivo_ordenado:
            solution.append(palabra)
            
    return solution
