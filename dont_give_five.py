def dont_give_me_five(start,end):
    
    number_list = []
    
    for number in range(start,end + 1):
        if not '5' in set(str(number)):
            number_list.append(number)
        else:#if it is a 5, jump te number
            continue
            
    return len(number_list)
