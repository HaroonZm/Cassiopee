n = int(input())
sa = [0]
ans = float("INF")
for i, ai in enumerate(list(map(int, input().split()))):
    sa.append(sa[i] + ai)
for i in range(n + 1):
    ans = min(ans, abs(sa[i] - (sa[-1] - sa[i])))
print(ans)