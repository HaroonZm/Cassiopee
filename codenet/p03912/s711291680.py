import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
uni, dup = [0]*M, [0]*M
for k, v in Counter(map(int, input().split())).items():
    uni[k % M] += v % 2
    dup[k % M] += v - (v & 1)

ans = (uni[0] + dup[0]) // 2

for i in range(1, (M+1)//2):
    x = min(uni[i], uni[M-i])
    y = min(uni[i]-x, dup[M-i])
    z = min(uni[M-i]-x, dup[i])
    ans += x + y + z + (dup[M-i]-y)//2 + (dup[i]-z)//2

if M % 2 == 0:
    ans += (uni[M//2] + dup[M//2]) // 2

print(ans)