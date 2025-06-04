players = [tuple(input().split()) for _ in range(24)]
for i in range(24):
    players[i] = (int(players[i][0]), float(players[i][1]))
groups = [players[i*8:(i+1)*8] for i in range(3)]
top2 = []
rest = []
for g in groups:
    g_sorted = sorted(g, key=lambda x:x[1])
    top2.extend(g_sorted[:2])
    rest.extend(g_sorted[2:])
rest_sorted = sorted(rest, key=lambda x: x[1])
final = top2 + rest_sorted[:2]
for p in final:
    print(p[0], f"{p[1]:.2f}")