def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    return 0

def date_to_days(y, m, d):
    days = 0
    for year in range(1, y):
        if is_leap_year(year):
            days += 366
        else:
            days += 365
    for month in range(1, m):
        days += days_in_month(y, month)
    days += d
    return days

while True:
    input_line = input()
    y1, m1, d1, y2, m2, d2 = map(int, input_line.split())
    if y1 < 0 or m1 < 0 or d1 < 0 or y2 < 0 or m2 < 0 or d2 < 0:
        break
    days1 = date_to_days(y1, m1, d1)
    days2 = date_to_days(y2, m2, d2)
    print(days2 - days1)