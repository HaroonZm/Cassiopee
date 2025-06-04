n, m = input().split()
n = int(n)
m = int(m)

xy = []
for i in range(m):
    a, b = input().split()
    a = int(a)
    b = int(b)
    xy.append([a, b])

ans = []
for i in range(n+1):
    ans.append(1)

prev = []
for i in range(n+1):
    prev.append(0)

xy.sort()

for i in range(len(xy)):
    x = xy[i][0]
    y = xy[i][1]
    temp = ans[y] + ans[y+1] - prev[y]
    ans[y] = temp
    ans[y+1] = temp
    prev[y] = temp

result = []
for i in range(1, n+1):
    result.append(str(ans[i]))

print(" ".join(result))