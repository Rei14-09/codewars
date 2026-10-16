def likes(name_list):
    
    if len(name_list) == 0:
        return 'no one likes this'
    elif len(name_list) == 1:
        return f'{name_list[0]} likes this'
    elif len(name_list) == 2:
        return f'{name_list[0]} and {name_list[1]} like this'
    elif len(name_list) == 3:
        return f'{name_list[0]}, {name_list[1]} and {name_list[2]} like this'
    else:
        return f'{name_list[0]}, {name_list[1]} and {len(name_list)-2} others like this'
