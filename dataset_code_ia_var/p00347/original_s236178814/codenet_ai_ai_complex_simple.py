from functools import lru_cache, reduce
from operator import add, mul
import sys

sys.setrecursionlimit(10**7)

def main():
    W, H = (lambda: map(int, input().split()))()
    M = list(map(lambda _: list(map(int, input().split())), range(H)))
    A = list(map(lambda row: reduce(lambda acc, x: acc + [acc[-1]+x], row, [0]), M))
    
    @lru_cache(maxsize=None)
    def recurse(X, Y, T):
        def inner():
            if Y == H: return 0
            if X == W: return A[Y][X] + recurse(X, Y+1, 0)
            SL = A[Y][X]
            SR = A[Y][W] - SL
            postponed = lambda turn: max if turn == 0 else min
            return postponed(T)(
                recurse(X+1, Y, T^1), 
                SL - SR + recurse(X, Y+1, T^1)
            )
        return inner()
    print(abs(recurse(0, 0, 1)))

main()