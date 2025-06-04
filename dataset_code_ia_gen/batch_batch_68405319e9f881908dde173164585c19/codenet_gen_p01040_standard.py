def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def weekday(y, m, d):
    if m < 3:
        y -= 1
        m += 12
    return (y + y//4 - y//100 + y//400 + (13*m + 8)//5 + d) % 7

def next_month(y, m):
    if m == 12:
        return y+1, 1
    return y, m+1

Y1, M1, D1, Y2, M2, D2 = map(int, input().split())

# Adjust start date to 13th of that month or next month if passed
if D1 > 13:
    Y1, M1 = next_month(Y1, M1)
elif D1 < 13:
    pass
else:
    # D1 == 13, start here
    pass

count = 0
y, m = Y1, M1

while True:
    # if date > end date, break
    if (y, m, 13) > (Y2, M2, D2):
        break
    # Determine if this date is valid (month length)
    if m == 2:
        maxd = 29 if is_leap_year(y) else 28
    elif m in [4,6,9,11]:
        maxd = 30
    else:
        maxd = 31
    if 13 <= maxd:
        if (y, m, 13) >= (Y1, M1, D1):
            if weekday(y, m, 13) == 5: # 0=Sunday, so 5=Friday
                count += 1
    y, m = next_month(y, m)

print(count)