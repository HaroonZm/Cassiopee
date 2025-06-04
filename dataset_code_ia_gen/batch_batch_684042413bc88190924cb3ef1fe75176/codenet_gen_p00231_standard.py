while True:
    n = int(input())
    if n == 0:
        break
    events = []
    for _ in range(n):
        m, a, b = map(int, input().split())
        events.append((a, +m))
        events.append((b, -m))
    events.sort(key=lambda x: (x[0], -x[1]))
    total = 0
    broken = False
    for _, w in events:
        total += w
        if total > 150:
            broken = True
            break
    print("NG" if broken else "OK")