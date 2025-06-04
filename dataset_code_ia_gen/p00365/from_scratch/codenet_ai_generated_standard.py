def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def next_birthday(y, m, d, year):
    if m == 2 and d == 29:
        return (year, 3, 1) if not is_leap_year(year) else (year, 2, 29)
    else:
        return (year, m, d)

def cmp_dates(a, b):
    return (a > b) - (a < b)

def age_on_date(birth, date):
    yb, mb, db = birth
    yd, md, dd = date
    bday = next_birthday(yb, mb, db, yd)
    age = yd - yb - (1 if cmp_dates(date, bday) < 0 else 0)
    return age

y1, m1, d1 = int(input()), int(input()), int(input())
y2, m2, d2 = int(input()), int(input()), int(input())

b1 = (y1, m1, d1)
b2 = (y2, m2, d2)

start_year = min(y1, y2)
end_year = 3001

max_diff = 0
for year in range(start_year, end_year):
    d1_age = age_on_date(b1, (year, 12, 31))
    d2_age = age_on_date(b2, (year, 12, 31))
    diff = abs(d1_age - d2_age)
    if diff > max_diff:
        max_diff = diff
    # optimization: once diff stops increasing for some years, we can break early
    # but problem constraints allow full search

print(max_diff)