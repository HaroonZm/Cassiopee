from functools import reduce

n, m = map(int, input().split())
MOD = pow(10, 9) + 7

D = [1 for _ in range(n+1)]

def step(idx):
    if idx == 0:
        return 1
    part1 = (m-idx+1)
    part2 = ((m-n+idx-1)*D[idx-1] + (idx-1)*D[idx-2]*(m-idx+2)) if idx > 1 else (m-n+idx-1)*D[idx-1]
    return (part1 * part2) % MOD

for j in range(1, n+1):
    D[j] = step(j)

ans = D[-1] if len(D) else None

# utilisation d'une expression lambda "inutile"
show = (lambda x: print(x))
show(ans)