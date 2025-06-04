def days_in_year(year):
    if year % 3 == 0:
        return 20 * 10
    else:
        # 5 big months and 5 small months alternating, starting with big month
        return 5 * 20 + 5 * 19

def days_in_month(year, month):
    if year % 3 == 0:
        return 20
    else:
        # odd month = big month (20 days), even month = small month (19 days)
        if month % 2 == 1:
            return 20
        else:
            return 19

def days_since_start(year, month, day):
    days = 0
    # add complete years before the given year
    for y in range(1, year):
        days += days_in_year(y)
    # add complete months before the given month in the given year
    for m in range(1, month):
        days += days_in_month(year, m)
    # add days in the current month (day-1 because day 1 means zero full days passed)
    days += (day - 1)
    return days

n = int(input())
for _ in range(n):
    Y, M, D = map(int, input().split())
    millennium = (1000, 1, 1)
    days_birth = days_since_start(Y, M, D)
    days_millennium = days_since_start(millennium[0], millennium[1], millennium[2])
    print(days_millennium - days_birth)