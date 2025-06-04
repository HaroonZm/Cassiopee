import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort(reverse=True)

count = {}
for x in A:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

ans = 0
for a in A:
    if count[a] == 0:
        continue
    k = 1
    while k <= a:
        k = k * 2
    r = k - a
    if r != a:
        if r in count and count[r] > 0:
            ans += 1
            count[r] -= 1
    else:
        if count[r] >= 2:
            ans += 1
            count[r] -= 1
    count[a] -= 1

print(ans)