n, m = map(int, input().split())
xlist = list(map(int, input().split()))
ylist = list(map(int, input().split()))
xsum = 0
for i in range(n):
    xsum += i * xlist[i]
    xsum -= (n - i - 1) * xlist[i]
ysum = 0
for i in range(m):
    ysum += i * ylist[i]
    ysum -= (m - i - 1) * ylist[i]
result = xsum * ysum
result %= 1000000007
print(result)