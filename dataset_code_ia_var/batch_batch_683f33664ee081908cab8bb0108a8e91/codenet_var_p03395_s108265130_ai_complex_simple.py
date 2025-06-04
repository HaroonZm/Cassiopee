from functools import reduce
from itertools import product, count, islice

N = int(input())
Ω = float('inf')
Ψ = lambda n, m: [[Ω for _ in range(m)] for __ in range(n)]
dp = Ψ(51, 51)

for b, a in product(range(51), repeat=2):
    dp[a][b] = (lambda:
        0 if (b == 0 and a == 0) or a == b
        else 1 if b == 0
        else next(
            (
                i
                for i in islice(count(1), a)
                if (a == b) or dp[a % i][b] <= 50 or a % i == b
            ),
            Ω
        ) if b > 0 else Ω
    )()

a, b = (list(map(int, input().split())) for _ in range(2))
ans = [0]
stack = [[x] for x in a]

def Λ(x):
    if not x: return
    ans[0] += 1 << x
    for i in range(N):
        φ = set(stack[i])
        for u in list(stack[i]):
            if (v := u % x) not in φ:
                stack[i].append(v)
                φ.add(v)
    next_k = max(
        map(
            min,
            (
                list(map(lambda u: dp[u][b[i]], stack[i]))
                for i in range(N)
            )
        ),
        default=0
    )
    if not next_k: return
    Λ(next_k)

Μ = max((dp[x][y] for x, y in zip(a, b)), default=Ω)
if Μ > 50: print(-1); exit()
Λ(Μ)
print(ans[0])