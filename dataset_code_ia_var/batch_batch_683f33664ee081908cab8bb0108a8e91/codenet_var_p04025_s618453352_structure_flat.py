n = int(input())
a = list(map(int, input().split()))
amax = max(a)
amin = min(a)
ans = 5 * 10**6
i = amin
while i <= amax:
    tmp = 0
    j = 0
    while j < n:
        tmp += (a[j] - i) ** 2
        j += 1
    if tmp < ans:
        ans = tmp
    i += 1
print(ans)