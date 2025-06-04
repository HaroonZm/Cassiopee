from sys import stdin
from itertools import count

def inpl(): return list(map(int, stdin.readline().split()))

N = int(stdin.readline())
A = inpl()
Ad = {a: i for i, a in enumerate(A)}
F = inpl()
C = [0]*N

for f in F:
    if (idx := Ad.get(f)) is not None:
        C[idx] += 1

if all(C):
    print("Yes")
else:
    print("No")
    print(*A)
    lack = next(i for i, v in enumerate(C) if v == 0)
    ans = [*A[:lack], A[lack-1], *A[lack+1:]]
    print(*ans)