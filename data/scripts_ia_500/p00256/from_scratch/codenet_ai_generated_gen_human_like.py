def is_leap_year(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def days_in_month(y, m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        return 29 if is_leap_year(y) else 28

def ymd_to_ordinal(y,m,d):
    # Convert Gregorian date to ordinal days from 2012.12.21 (day 0)
    # 2012.12.21 corresponds to day 0
    # Count days from 2012/12/21 to y/m/d
    # For efficiency, count full years + months + days.

    # If y == 2012, count months and days from Dec 21
    # For y > 2012, count full years since 2013 Jan 1 + days in 2012 from 12/21 to 12/31 (10 days)
    days = 0
    # Count full years
    for year in range(2012, y):
        # sum full year except if y == 2012 (then we count only from Dec 21)
        if year == 2012:
            # days from Dec 21 to Dec 31 inclusive: Dec 21-31 is 11 days but 21 is day 0 so 10 days
            days += 10
        else:
            days += 366 if is_leap_year(year) else 365

    # count months in Y year before m
    for month in range(1, m):
        days += days_in_month(y, month)
    days += d - 21  # subtract 21 from day, because day 21 is day 0
    return days

def ordinal_to_ymd(days):
    # Inverse of ymd_to_ordinal
    # Given days offset from 2012.12.21 (day 0), return y,m,d
    y = 2012
    d = days
    # Deduct year by year
    # First handle 2012: days 0 - 10 -> Dec 21 to Dec 31
    if d < 0:
        # No date before 2012.12.21 (problem limits)
        return None
    if d <= 10:
        # Still in 2012 Dec
        m = 12
        day = 21 + d
        return (y,m,day)
    d -= 10
    y += 1
    while True:
        days_in_year = 366 if is_leap_year(y) else 365
        if d < days_in_year:
            break
        d -= days_in_year
        y +=1
    # Now find month and day in year y
    m = 1
    while True:
        dim = days_in_month(y, m)
        if d < dim:
            break
        d -= dim
        m +=1
    return (y, m, d+1)

def maya_to_ordinal(b, ka, t, w, ki):
    # Calculate total days from Maya long count
    # Maya count 0.0.0.0.0 corresponds to 2012.12.21
    # Each unit in days:
    # kin = 1 day
    # winal = 20 kin = 20 days
    # tun = 18 winal = 360 days
    # katun = 20 tun = 7200 days
    # baktun = 20 katun = 144000 days
    return (b*144000 + ka*7200 + t*360 + w*20 + ki)

def ordinal_to_maya(days):
    # convert days offset from 2012.12.21 to maya long count
    b = days // 144000
    days %= 144000
    ka = days // 7200
    days %= 7200
    t = days // 360
    days %= 360
    w = days // 20
    ki = days % 20
    return (b, ka, t, w, ki)

def is_maya_date(s):
    parts = s.split('.')
    if len(parts) == 5:
        # Must check ranges
        try:
            b, ka, t, w, ki = map(int, parts)
            if 0 <= b < 13 and 0 <= ka < 20 and 0 <= t < 20 and 0 <= w < 18 and 0 <= ki < 20:
                return True
        except:
            return False
        return False
    return False

def is_gregorian_date(s):
    parts = s.split('.')
    if len(parts) == 3:
        try:
            y,m,d = map(int, parts)
            if 2012 <= y <= 10000000 and 1 <= m <= 12:
                dim = days_in_month(y,m)
                if 1 <= d <= dim:
                    return True
        except:
            return False
        return False
    return False

import sys

for line in sys.stdin:
    line=line.strip()
    if line == '#':
        break
    if is_gregorian_date(line):
        y,m,d = map(int, line.split('.'))
        days = ymd_to_ordinal(y,m,d)
        # Calculate days offset from 2012.12.21 (0.0.0.0.0)
        # days can be negative for date before 2012.12.21 but problem states input date >= 2012.12.21
        # Convert to Maya long count
        b,ka,t,w,ki = ordinal_to_maya(days)
        print(f"{b}.{ka}.{t}.{w}.{ki}")
    elif is_maya_date(line):
        b,ka,t,w,ki = map(int, line.split('.'))
        days = maya_to_ordinal(b,ka,t,w,ki)
        y,m,d = ordinal_to_ymd(days)
        print(f"{y}.{m}.{d}")
    else:
        # Ignore invalid input per problem statement, or no output needed
        pass