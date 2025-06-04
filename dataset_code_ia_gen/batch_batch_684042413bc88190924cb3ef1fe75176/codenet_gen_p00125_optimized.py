def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def days_in_month(y, m):
    if m == 2:
        return 29 if is_leap_year(y) else 28
    return 31 if m in {1,3,5,7,8,10,12} else 30

def days_from_start(y,m,d):
    days = d
    for month in range(1,m):
        days += days_in_month(y, month)
    for year in range(1,y):
        days += 366 if is_leap_year(year) else 365
    return days

while True:
    y1,m1,d1,y2,m2,d2 = map(int,input().split())
    if y1<0 or m1<0 or d1<0 or y2<0 or m2<0 or d2<0:
        break
    print(days_from_start(y2,m2,d2)-days_from_start(y1,m1,d1))