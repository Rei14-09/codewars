def twins(age, distance, velocity):
    
    import math
    
    t = 2*distance/velocity
    
    velocity = math.pow(velocity,2)
    al= math.pow(1-velocity,1/2)
    
    ños1 = age + t
    años2 = al*t + age
    
    
    return round(años2,2),round(ños1,2)
