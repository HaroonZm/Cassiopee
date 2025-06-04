n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
s = [0]
p = [0]
i = 1
while i <= n:
    s.append(s[i-1] + a[i])
    p.append(p[i-1] + (a[i] if a[i] > 0 else 0))
    i += 1
ans = 0
i = 1
while i <= n - k + 1:
    tmp = s[i + k - 1] - s[i - 1]
    tmp = tmp if tmp > 0 else 0
    tmp += p[i-1] + (p[n] - p[i + k - 1])
    if tmp > ans:
        ans = tmp
    i += 1
print(ans)