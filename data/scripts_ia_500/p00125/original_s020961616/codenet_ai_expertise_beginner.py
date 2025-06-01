def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

def days_in_month(year, month):
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 31

def days_from_start_of_year(y, m, d):
    total = 0
    for month in range(1, m):
        total += days_in_month(y, month)
    total += d
    return total

def days_between_dates(y1, m1, d1, y2, m2, d2):
    if y1 == y2:
        return days_from_start_of_year(y2, m2, d2) - days_from_start_of_year(y1, m1, d1)
    
    days = 0
    days += (days_in_year(y1) - days_from_start_of_year(y1, m1, d1))
    for year in range(y1 + 1, y2):
        days += days_in_year(year)
    days += days_from_start_of_year(y2, m2, d2)
    return days

def days_in_year(year):
    if is_leap_year(year):
        return 366
    return 365

while True:
    try:
        y1, m1, d1, y2, m2, d2 = map(int, raw_input().split())
    except:
        break
    if y1 < 0 or m1 < 0 or d1 < 0 or y2 < 0 or m2 < 0 or d2 < 0:
        break
    print days_between_dates(y1, m1, d1, y2, m2, d2)