from itertools import product

n, x, m = map(int, raw_input().split())
h = [map(int, raw_input().split()) for i in xrange(m)]
ans = [-1]

for p in product(range(x + 1), repeat=n):
    for l, r, s in h:
        if s != sum(p[l - 1:r]):
            break
    else:
        if sum(ans) < sum(p):
            ans = p

print " ".join(map(str, ans))