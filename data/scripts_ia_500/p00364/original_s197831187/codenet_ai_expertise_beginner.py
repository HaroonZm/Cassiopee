n, t = input().split()
n = int(n)
t = int(t)
ans = 0
for i in range(n):
    x, h = input().split()
    x = int(x)
    h = int(h)
    value = h * t / x
    if value > ans:
        ans = value
print(ans)