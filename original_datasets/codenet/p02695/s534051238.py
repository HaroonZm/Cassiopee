import itertools
n, m, q = map(int, input().split())
ls = []
for _ in range(q):
    a, b, c, d = map(int, input().split())
    ls.append((a, b, c, d))

def calc(x, ls):
    s = sum([d for a, b, c, d in ls if x[b - 1] - x[a - 1] == c])
    return s

ans = 0
cands = range(1, m+1)
c = itertools.combinations_with_replacement(cands, n)
for x in c:
    ans = max(ans, calc(x, ls))
print(ans)