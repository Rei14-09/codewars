def well(x):
    
    if 'good' not in x:
        return 'Fail!'
    elif x.count('good') < 3:
        return 'Publish!'
    else:
        return 'I smell a series!