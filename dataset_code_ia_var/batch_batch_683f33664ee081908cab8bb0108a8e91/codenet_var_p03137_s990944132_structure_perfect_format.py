n, m = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
ans = []
for i in range(m - 1):
    ans.append(x[i + 1] - x[i])
ans.sort()
if n < m:
    print(sum(ans[:m - n]))
else:
    print(0)