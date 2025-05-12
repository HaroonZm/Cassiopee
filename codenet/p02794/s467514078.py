n = int(input())
ab = {i: [] for i in range(n)}
for j in range(n - 1):
    a, b = [int(i) - 1 for i in input().split()]
    ab[a].append((b, j))
    ab[b].append((a, j))

def dfs(a, b, d=[], c=-1):
    if a == b:
        return d
    for i in ab[a]:
        if i[0] == c:
            continue
        e = dfs(i[0], b, d + [i[1]], a)
        if len(e) != 0:
            return set(e)
    return set()

m = int(input())
ms = []
for _ in range(m):
    u, p = [int(i) - 1 for i in input().split()]
    ms.append(dfs(u, p))

ans = 0
for i in range(1 << m):
    k = 0
    a = set()
    for j in range(m):
        if (i >> j) & 1 == 1:
            k += 1
            a |= ms[j]
    if k % 2 == 1:
        ans += 2 ** (n - 1 - len(a))
    elif k != 0:
        ans -= 2 ** (n - 1 - len(a))
            
print(2**(n-1)-ans)