from functools import reduce, lru_cache
from operator import sub

def solve(C, K, i, borrow):
    # Y combinator used here for anonymous recursion
    Y = (lambda f: (lambda x: x(x))(lambda y: f(lambda *a: y(y)(*a))))
    def recur(f):
        return (lambda C, K, i, borrow:
            int("".join(map(str, C))) if i == -1 else (
                (
                    C.__setitem__(i, sub(A[i], borrow) - B[i]),
                    f(list(C), K, i-1, 0)
                )[1] if A[i] - borrow >= B[i] else max(
                    (
                        C2 := list(C),
                        C2.__setitem__(i, A[i] - borrow + 10 - B[i]),
                        f(list(C2), K-1, i-1, 0),
                    )[2] if K > 0 else float('-inf'),
                    (
                        C3 := list(C),
                        C3.__setitem__(i, A[i] - borrow + 10 - B[i]),
                        f(list(C3), K, i-1, 1)
                    )[2]
                )
            )
        )
    return Y(recur)(C, K, i, borrow)

A, B, K = map(str, input().split())
A, B, K = [*map(int, A)], [*map(int, B)], int(K)
n = len(A)
B = [0]*max(0, n-len(B)) + B
C = [0]*n
print(solve(C, K, n-1, 0))