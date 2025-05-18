from collections import Counter
def inpl(): return list(map(int, input().split()))
N = int(input())
A = inpl()
Ai = range(N)
Ad = {a:i for i, a in enumerate(A)}
F = inpl()

C = [0]*N
for f in F:
    C[Ad[f]] += 1

if not 0 in C:
    print("Yes")
else:
    print("No")
    print(*list(map(str, A)))
    lack = C.index(0)
    ans = A[:lack] + [A[lack-1]] + A[lack+1:]
    print(*ans)