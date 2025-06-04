def to_seconds(hms):
    h, m, s = map(int, hms.split(':'))
    return h * 3600 + m * 60 + s

while True:
    n = int(input())
    if n == 0:
        break
    events = []
    for _ in range(n):
        dep, arr = input().split()
        dep_sec = to_seconds(dep)
        arr_sec = to_seconds(arr)
        # arrival event: -1 (train freed)
        events.append((arr_sec, -1))
        # departure event: +1 (train needed)
        events.append((dep_sec, +1))
    # Sort by time; if same time, arrival (-1) before departure (+1)
    events.sort(key=lambda x: (x[0], x[1]))
    current = 0
    max_trains = 0
    for _, e in events:
        current += e
        if current > max_trains:
            max_trains = current
    print(max_trains)