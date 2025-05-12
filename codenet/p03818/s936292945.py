from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
ans = 0
even = 0
for v in c.values():
    if v % 2 == 0:
        even += 1
    else:
        ans += 1

if even % 2 == 0:
    ans += even
else:
    ans += even-1

print(ans)