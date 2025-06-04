import sys
import bisect

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
acc = [0]*(N+1)
for i in range(N):
    acc[i+1] = acc[i]+a[i]

for j in range(M):
    idx = bisect.bisect_right(a, b[j])
    score = acc[idx]
    print("Yes" if score >= c[j] else "No")