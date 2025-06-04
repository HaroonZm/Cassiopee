from sys import stdin
from itertools import islice

def get_prices(count, label):
    return sorted(
        (int(t[1]) for t in (stdin.readline().split() for _ in range(count)) if t[0] == label),
        reverse=True
    )

D = int(stdin.readline())

n1 = int(stdin.readline())
p1 = get_prices(n1, "D")

n2 = int(stdin.readline())
p2 = get_prices(n2, "DD")

cum1 = [0] + list(__import__('itertools').accumulate(p1))
cum2 = [0] + list(__import__('itertools').accumulate(p2))

best = 0
for d in range(D + 1):
    dd = (D - d) // 2
    if d <= len(p1) and dd <= len(p2):
        best = max(best, cum1[d] + cum2[dd])

print(best)