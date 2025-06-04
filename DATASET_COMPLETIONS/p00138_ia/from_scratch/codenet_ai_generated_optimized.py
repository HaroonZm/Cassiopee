players = [tuple(input().split()) for _ in range(24)]
for i in range(24):
    p, t = players[i]
    players[i] = (int(p), float(t))

finalists = []
third_and_below = []

for i in range(3):
    group = players[i*8:(i+1)*8]
    group.sort(key=lambda x: x[1])
    finalists.extend(group[:2])
    third_and_below.extend(group[2:])

third_and_below.sort(key=lambda x: x[1])
finalists.extend(third_and_below[:2])

for p, t in finalists:
    print(p, f"{t:.2f}")