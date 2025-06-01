import sys

baktun_days = 20*20*18*20
katun_days = 20*18*20
tun_days = 18*20
winal_days = 20
kin_days = 1

def is_leap(y):
    return (y%400==0) or (y%4==0 and y%100!=0)

def days_in_month(y,m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        return 29 if is_leap(y) else 28

def gregorian_to_ordinal(y,m,d):
    # Count days from 2012.12.21 (day 0)
    # Count days from year 2012 to y-1
    day_count = 0
    for year in range(2012,y):
        day_count += 366 if is_leap(year) else 365
    for month in range(1,m):
        day_count += days_in_month(y,month)
    day_count += d - 21 if y==2012 and m==12 else d
    if y==2012 and m==12:
        day_count -= 21
    elif y==2012 and m<12:
        day_count -= 0 # invalid in input range
    elif y<2012:
        day_count -= 0 # invalid in input range
    return day_count

def ordinal_to_gregorian(n):
    y = 2012
    d = n
    while True:
        days_year = 366 if is_leap(y) else 365
        if d < days_year:
            break
        d -= days_year
        y += 1
    m = 1
    while True:
        dim = days_in_month(y,m)
        if d < dim:
            break
        d -= dim
        m += 1
    return y,m,d+1

def mayan_to_ordinal(b,ka,t,w,ki):
    return b*baktun_days + ka*katun_days + t*tun_days + w*winal_days + ki

def ordinal_to_mayan(n):
    b = n // baktun_days
    n %= baktun_days
    ka = n // katun_days
    n %= katun_days
    t = n // tun_days
    n %= tun_days
    w = n // winal_days
    ki = n % winal_days
    return b,ka,t,w,ki

for line in sys.stdin:
    line=line.strip()
    if line=="#":
        break
    if '.' not in line:
        continue
    parts=line.split('.')
    if len(parts)==5:
        b,ka,t,w,ki = map(int,parts)
        n = mayan_to_ordinal(b,ka,t,w,ki)
        y,m,d = ordinal_to_gregorian(n)
        print(f"{y}.{m}.{d}")
    elif len(parts)==3:
        y,m,d = map(int,parts)
        n = gregorian_to_ordinal(y,m,d)
        b,ka,t,w,ki = ordinal_to_mayan(n)
        print(f"{b}.{ka}.{t}.{w}.{ki}")