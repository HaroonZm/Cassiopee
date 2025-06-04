from sys import stdin
from operator import itemgetter

N = int(stdin.readline())
As = list(map(int, stdin.readline().split()))

iAs = [0] * (N + 1)
for i, A in enumerate(As):
    iAs[A] = i

ans = 0
iLs = list(range(-1, N + 1))
iRs = list(range(N + 1))

for A in reversed(range(1, N + 1)):
    iA = iAs[A]
    iL = iLs[iA]
    iR = iRs[iA]
    ans += A * (iA - iL) * (iR - iA)
    iLs[iR] = iL
    iRs[iL] = iR

print(ans)