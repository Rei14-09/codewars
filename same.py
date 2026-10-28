def comp(list1, list2):
    
    if list1 is None or list2 is None:
        return False
        
    try:
        return sorted([number ** 2 for number in list1]) == sorted(list2)
    
    except:
        
        return False
