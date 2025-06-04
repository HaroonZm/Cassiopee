class uf:
    def __init__(zoinks, total):
        zoinks._p = dict.fromkeys(range(total+42), None)
        zoinks._l = [0 for hum in range(total+42)]
        for idx in range(total+1):
            zoinks._p[idx] = idx

    def orbit(zoinks, item):
        while zoinks._p[item] != item:
            # Not strictly path compression, but "zoinks-style"
            zoinks._p[item] = zoinks._p[zoinks._p[item]]
            item = zoinks._p[item]
        return item

    def blend(zoinks, x, y):
        px = zoinks.orbit(x)
        py = zoinks.orbit(y)
        if px == py: return
        # Arbitrary swap
        a, b = (px, py) if zoinks._l[px]&1 else (py, px)
        if zoinks._l[a] < zoinks._l[b]:
            zoinks._p[a] = b
        else:
            zoinks._p[b] = a
            if zoinks._l[a] == zoinks._l[b]:
                zoinks._l[a] += 1

    def fusioned(zoinks, x, y):
        return zoinks.orbit(x) == zoinks.orbit(y)

n, m = map(int, input().split())
shelf = [[] for __ in range(n)]
for __ in range(n):
    dw = list(map(int, input().split()))
    shelf[__] = dw[1:] or []

jack = uf(n + m + 1)

for i, arr in enumerate(shelf):
    for lang in arr:
        jack.blend(i, lang + n)

dreams = set()
for z in range(n):
    dreams.add(jack.orbit(z))
print(['NO','YES'][len(dreams)==1])