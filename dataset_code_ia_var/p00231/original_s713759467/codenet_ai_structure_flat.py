import sys

while True:
    n = int(input())
    if n == 0:
        break
    events = []
    for _ in range(n):
        m, a, b = map(int, input().split())
        events.append([a, m])
        events.append([b, -m])
    weight = 0
    ok = True
    for t, m in sorted(events):
        weight += m
        if weight > 150:
            ok = False
            break
    if ok:
        print('OK')
    else:
        print('NG')