n, m = map(int, input().split())
a = list(map(int, input().split()))
s = 0
for x in a:
    s += x
r = n - s
if r >= 0:
    print(r)
else:
    print(-1)