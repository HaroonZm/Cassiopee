import bisect

a, b, q = map(int, raw_input().split())
inf = 1 << 60

# on ajoute de grands nombres aux extrémités
s = [-inf]
for i in range(a):
    s.append(int(raw_input()))
s.append(inf)
s.sort()

t = [-inf]
for i in range(b):
    t.append(int(raw_input()))
t.append(inf)
t.sort()

for i in range(q):
    x = int(raw_input())

    # position du sanctuaire le plus proche
    idx_s = bisect.bisect(s, x)
    idx_t = bisect.bisect(t, x)

    ans = inf

    # tester toutes les combinaisons de sanctuaire/temple proche avant ou après x
    for ss in [s[idx_s - 1], s[idx_s]]:
        for tt in [t[idx_t - 1], t[idx_t]]:
            d1 = abs(ss - x) + abs(tt - ss)
            d2 = abs(tt - x) + abs(ss - tt)
            if d1 < ans:
                ans = d1
            if d2 < ans:
                ans = d2
    print ans