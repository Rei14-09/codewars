def find_it(number_list):
    
    solution = []
    
    for number in number_list:
        if number_list.count(number) % 2 == 0:
            continue
        else:
            if number not in solution:
                solution.append(number)
            else:
                continue
            
    return solution[0]
