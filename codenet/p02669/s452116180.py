from functools import lru_cache
import sys
def input():
    return sys.stdin.readline()[:-1]

def solve(N, A, B, C, D):
    @lru_cache(None)
    def f(N):
        if N == 0:
            return 0
        if N == 1:
            return D
        # すべて-1の遷移で0にしたケース
        ret = D * N

        q, r = divmod(N, 2)
        if r == 0:
            # 2で割り算
            ret = min(ret, f(q) + A)
        else:
            # -1して2で割り算、+1して2で割り算
            ret = min(ret, f(q) + A + D, f(q+1) + A + D)

        q, r = divmod(N, 3)
        if r == 0:
            # 3で割り算
            ret = min(ret, f(q) + B)
        elif r == 1:
            # -1して3で割り算
            ret = min(ret, f(q) + B + D)
        else:
            # +1して3で割り算
            ret = min(ret, f(q+1) + B + D)

        q, r = divmod(N, 5)
        if r == 0:
            # 5で割り算
            ret = min(ret, f(q) + C)
        elif r == 1:
            # -1して5で割り算
            ret = min(ret, f(q) + C + D)
        elif r == 2:
            # -2して5で割り算
            ret = min(ret, f(q) + C + D + D)
        elif r == 3:
            # +2して5で割り算
            ret = min(ret, f(q+1) + C + D + D)
        else:
            # +1して5で割り算
            ret = min(ret, f(q+1) + C + D)
        return ret
    return f(N)

T = int(input())
for _ in range(T):
    n,a,b,c,d = map(int, input().split())
    print(solve(n,a,b,c,d))