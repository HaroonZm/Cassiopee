import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
t = []
k = 0
for i in range(n):
    if k > 0 and a[i] == a[i-1]:
        t.append(k)
        k = 0
    k += 1
if k > 0:
    t.append(k)
ans = 0
k = 0
for i in range(len(t)):
    k += t[i]
    if i > 2:
        k -= t[i-3]
    if k > ans:
        ans = k
print(ans)