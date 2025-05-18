from collections import Counter

n = int(input())
a = input().split()
# a = list(map(int, input().split()))
ans = ''
# t1, t2 = [], []
t1, t2 = Counter(), Counter()
for i in range(n):
    t1.update(a[i])
    t2.update(a[n-1-i])
    t3 = t1 & t2
    t1 -= t3
    t2 -= t3
    if t1 == t2:
        ans += str(i+1) + ' '
print(ans[:-1])