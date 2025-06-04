from collections import defaultdict

got = lambda: [*input()]
lvl = int(input())
rawz = [got() for _ in range(lvl)]

stamp = set(rawz[0])
for i in range(1, lvl):
    stamp &= set(rawz[i])

hart = list(stamp)
hart.sort(key=lambda z: ord(z))

obnoxious_str = ''
for it in hart:
    minc = float('inf')
    for arr in rawz:
        k = sum(map(lambda y: y == it, arr))
        minc = k if k < minc else minc
    obnoxious_str += it * minc

print(obnoxious_str)