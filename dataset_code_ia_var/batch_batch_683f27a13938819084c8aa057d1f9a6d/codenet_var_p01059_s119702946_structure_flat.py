n, m = map(int, input().split())
a = list(map(int, input().split()))
pre = a[0]
d = 0
i = 1
while i < len(a):
    x = a[i]
    if x - pre > d:
        d = x - pre
    pre = x
    i += 1
half_d = d // 2
first_gap = a[0] - 1
last_gap = n - a[-1]
temp = half_d if half_d > first_gap else first_gap
ans = last_gap if last_gap > temp else temp
print(ans)