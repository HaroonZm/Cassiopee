n = int(input())
a = input().split()
w = input().split()

INF = 1000000000
x = [INF, INF]

for i in range(n):
    ai = int(a[i])
    wi = int(w[i])
    if wi < x[ai]:
        x[ai] = wi

ans = x[0] + x[1]
if ans >= INF:
    ans = 0
print(ans)