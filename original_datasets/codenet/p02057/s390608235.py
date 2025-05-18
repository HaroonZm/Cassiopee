from collections import Counter
from itertools import accumulate
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = max(A)
table = [0]*(K+1)

table[0] = M
for b, v in Counter(B).items():
    for j in range(b, K+1, b):
        table[j] -= b*v
    for j in range(b+1, K+1, b):
        table[j] += b*v
table = list(accumulate(table))
table[0] = 0
table = list(accumulate(table))

print(sum(table[a] for a in A))