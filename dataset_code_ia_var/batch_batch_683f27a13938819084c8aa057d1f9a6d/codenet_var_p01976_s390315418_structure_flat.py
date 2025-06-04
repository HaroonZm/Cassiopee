from collections import Counter

n = int(input())
a = input().split()
ans = ''
t1 = Counter()
t2 = Counter()
i = 0
while i < n:
    t1.update(a[i])
    t2.update(a[n-1-i])
    t3 = t1 & t2
    t1 -= t3
    t2 -= t3
    if t1 == t2:
        ans += str(i+1) + ' '
    i += 1
print(ans[:-1])