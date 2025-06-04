def to_minutes(h, m):
    return h * 60 + m

def in_range(t, start, end):
    if start <= end:
        return start <= t <= end
    else:
        return t >= start or t <= end

while True:
    n = int(input())
    if n == 0:
        break
    stats = {'lunch': [0,0], 'dinner': [0,0], 'midnight': [0,0]}
    for _ in range(n):
        time_str, prod = input().split()
        h, m = map(int, time_str.split(':'))
        prod = int(prod)
        start = to_minutes(h, m)
        end = start + prod
        # Wrap around midnight for end time
        if end >= 24*60:
            end -= 24*60

        if in_range(start, 11*60, 14*60+59):
            stats['lunch'][1] += 1
            if prod <= 8:
                stats['lunch'][0] += 1
        elif in_range(start, 18*60, 20*60+59):
            stats['dinner'][1] += 1
            if prod <= 8:
                stats['dinner'][0] += 1
        elif in_range(start, 21*60, 1*60+59):
            stats['midnight'][1] += 1
            if prod <= 8:
                stats['midnight'][0] += 1

    for period in ['lunch', 'dinner', 'midnight']:
        ok, total = stats[period]
        if total == 0:
            print(f"{period} no guest")
        else:
            print(f"{period} {ok * 100 // total}")