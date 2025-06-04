n = int(input())
l = list(map(int, input().split()))
if n <= 2:
    print(1)
    quit()
h = 0
ans = 1
for i in range(n - 1):
    if (l[i + 1] - l[i]) * h < 0:
        ans += 1
        h = 0
        continue
    if l[i + 1] - l[i] < 0:
        h = -1
    elif l[i + 1] - l[i] > 0:
        h = 1
print(ans)