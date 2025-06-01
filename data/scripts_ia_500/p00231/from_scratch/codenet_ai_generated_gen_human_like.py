while True:
    n = int(input())
    if n == 0:
        break
    people = []
    for _ in range(n):
        m, a, b = map(int, input().split())
        people.append((m, a, b))
    events = []
    for m, a, b in people:
        events.append((a, m))   # arrival: add weight
        events.append((b, -m))  # departure: remove weight
    events.sort(key=lambda x: (x[0], -x[1]))  # departures before arrivals at same time
    total_weight = 0
    broken = False
    for time, weight_change in events:
        total_weight += weight_change
        if total_weight > 150:
            broken = True
            break
    print("NG" if broken else "OK")