n, m = map(int, input().split())
x = [int(y) for y in input().split()]
x.sort()
if n >= m:
    print('0')
else:
    y = []
    for i in range(m - 1):
        y.append(x[i + 1] - x[i])
    y.sort()
    ans = sum(y)
    for i in range(n - 1):
        ans -= y[-(i + 1)]
    print(ans)