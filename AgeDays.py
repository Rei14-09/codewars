from datetime import date

def age_in_days(year, month, day):
    
    birth = date(year, month, day)
    
    today = date.today()
    
    difference = today - birth
    
    sol = difference.days
    
    return f'You are {sol} days old'