import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
C = Counter(A)
ans = 0
i = 0
while i < len(A):
    a = A[i]
    if C[a] == 0:
        i += 1
        continue
    r = (1 << a.bit_length()) - a
    if r != a:
        if C[r] > 0:
            ans += 1
            C[r] -= 1
    else:
        if C[r] >= 2:
            ans += 1
            C[r] -= 1
    C[a] -= 1
    i += 1
print(ans)