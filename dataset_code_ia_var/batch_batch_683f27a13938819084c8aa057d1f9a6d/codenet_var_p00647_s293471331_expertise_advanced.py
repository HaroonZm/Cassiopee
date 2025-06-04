from sys import stdin
from collections import Counter

def get_period(tm):
    if 1100 <= tm < 1500:
        return 'lunch'
    elif 1800 <= tm < 2100:
        return 'dinner'
    elif 2100 <= tm or tm < 200:
        return 'midnight'
    return None

periods = ['lunch', 'dinner', 'midnight']
while True:
    line = stdin.readline()
    if not line:
        break
    N = int(line)
    if N == 0:
        break
    total = Counter()
    good = Counter()
    for _ in range(N):
        s0, s1 = stdin.readline().split()
        h, m = map(int, s0.split(":"))
        tm = 100 * h + m
        m1 = int(s1)
        delta = m1 - m if m1 >= m else m1 + 60 - m
        period = get_period(tm)
        if period:
            total[period] += 1
            if delta <= 8:
                good[period] += 1
    for p in periods:
        print(f"{p} {100*good[p]//total[p] if total[p] else 'no guest'}")