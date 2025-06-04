import sys
from collections import Counter

def freq_op(A):
    counts = Counter(A)
    return [counts[a] for a in A]

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break

    A = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    seen = set()
    while True:
        B = freq_op(A)
        cnt += 1
        if B == A:
            break
        A = B

    print(cnt - 1)
    print(*A)