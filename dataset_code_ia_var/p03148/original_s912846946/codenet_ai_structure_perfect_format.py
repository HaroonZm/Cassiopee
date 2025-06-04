from collections import Counter as ct

n, k = map(int, input().split())
td = [list(map(int, input().split())) for _ in range(n)]

kind = len(ct([x[0] for x in td]))
std = sorted(td, key=lambda x: x[1], reverse=True)
dup = []
eat_k = set()
ans = 0

for i in range(k):
    ans += std[i][1]
    if std[i][0] in eat_k:
        dup.append(std[i])
    eat_k.add(std[i][0])

ans += len(eat_k) ** 2
tmpa = ans

for i in range(k, n):
    if not dup:
        break
    if std[i][0] not in eat_k:
        t = dup.pop()
        tmpa -= t[1]
        tmpa += std[i][1]
        tmpa -= len(eat_k) ** 2
        eat_k.add(std[i][0])
        tmpa += len(eat_k) ** 2
        ans = max(tmpa, ans)

print(ans)