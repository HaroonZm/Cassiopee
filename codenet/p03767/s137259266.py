N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
ans = 0
for i in range(1, len(a)-N):
    if i % 2 == 1:
        # print(a[i])
        ans += a[i]
print(ans)