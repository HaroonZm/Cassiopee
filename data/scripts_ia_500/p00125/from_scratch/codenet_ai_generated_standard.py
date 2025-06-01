def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def days_in_month(y, m):
    if m == 2:
        return 29 if is_leap_year(y) else 28
    return [31,28,31,30,31,30,31,31,30,31,30,31][m-1]

def days_from_0(y, m, d):
    days = 0
    for year in range(1, y):
        days += 366 if is_leap_year(year) else 365
    for month in range(1, m):
        days += days_in_month(y, month)
    days += d
    return days

while True:
    y1,m1,d1,y2,m2,d2 = map(int, input().split())
    if min(y1,m1,d1,y2,m2,d2) < 0:
        break
    print(days_from_0(y2,m2,d2) - days_from_0(y1,m1,d1))