def generate_range(start, stop, step):
    
    sol = []
    
    while start<=stop:
        sol.append(start)
        start += step
        
    return sol
