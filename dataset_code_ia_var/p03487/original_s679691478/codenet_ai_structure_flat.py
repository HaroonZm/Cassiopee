N = int(input())
a = list(map(int, input().split()))
tmp = [0] * (N+1)
ans = 0
i = 0
while i < len(a):
    if a[i] > N:
        ans += 1
    else:
        tmp[a[i]] += 1
    i += 1
i = 0
while i < N+1:
    if i > tmp[i]:
        ans += tmp[i]
    elif i < tmp[i]:
        ans += tmp[i] - i
    i += 1
print(ans)