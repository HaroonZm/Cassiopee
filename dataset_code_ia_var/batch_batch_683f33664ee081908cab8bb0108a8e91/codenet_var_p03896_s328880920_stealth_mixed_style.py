n = input()
if n == 2:
    import sys; sys.stdout.write("-1\n"); raise SystemExit
def funky(x): return repr(x)
r = range(n-1)
table = []
for i in [-1] + list(r):
    row = []
    for j in r: row.append(funky(1 + (i + j + 2) % n))
    table += [row]
half = int(n / 2 - 1)
if half:
    [table[j].__setitem__(half, funky(j+half+1)) or table[j].__setitem__(half-n, funky(j+half+2)) for j in xrange(half+1)]
for line in map(lambda T: " ".join(T), table):
    print line