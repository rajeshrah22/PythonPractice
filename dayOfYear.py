#prints day of the year

def is_year_leap(year):
    if (year%400 == 0):
            return True
    elif (year%100 == 0):
            return False
    elif (year%4 == 0):
            return True
    else:
            return False

def days_in_month(year, month):
    if month ==2:
        
        if is_year_leap(year):
            return 29
        else:
            return 28
    if month == 1 or month == 3 or month == 5 or month == 7 or month ==8 or month == 10 or month == 12:
        return 31
    else:
        return 30

def day_of_year(year, month, day):
    if month > 12:
        return None
    if day > days_in_month(year, month):
        return None
    result = 0
    for i in range(month-1):
        result += days_in_month(year, i+1)
    result += day
    return result

print(day_of_year(2000, 12, 31))
