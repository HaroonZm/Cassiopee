n = int(input())
l = list(map(int, input().split()))
s = sum(l) / n
if s - int(s) < int(s) + 1 - s:
    s = int(s)
else:
    s = int(s) + 1
ans = 0
i = 0
while i < len(l):
    ans += (s - l[i]) ** 2
    i += 1
print(ans)