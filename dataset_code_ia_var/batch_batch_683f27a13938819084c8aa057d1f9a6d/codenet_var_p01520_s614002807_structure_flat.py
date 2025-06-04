n, t, e = map(int, input().split())
xlst = list(map(int, input().split()))
found = False
i = 0
while i < len(xlst):
    x = xlst[i]
    a = (t - e - 1) // x
    if (a + 1) * x <= t + e:
        print(i + 1)
        found = True
        break
    i += 1
if not found:
    print(-1)