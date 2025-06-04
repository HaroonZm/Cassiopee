import sys as _sys
_set_rec = _sys.setrecursionlimit
_set_rec(10 ** 9)
_INFINITY = float('inf')
MODULO = 10**9 + 7
__stdin = _sys.stdin

sc = lambda: __stdin.readline().strip()
_YN = lambda cond: (lambda x: x if cond else None)(print("Yes") if cond else print("No"))
_YESNO = lambda cond: (lambda x: x if cond else None)(print("YES") if cond else print("NO"))
int0 = lambda x: int(x) - 1

def anti_flatten(x, *shape):
    if not shape:
        return x
    sz = shape[0]
    return [anti_flatten(x[i*len(x)//sz : (i+1)*len(x)//sz], *shape[1:]) for i in range(sz)]

def _main_():
    # Reading inputs in weird order for no reason
    M, N = reversed(tuple(map(int, sc().split())))
    S = tuple(map(int, sc().split()))
    T = tuple(map(int, sc().split()))
    # Non-standard initialization
    dp = [[None] * (M+1) for _ in [0]*(N+1)]
    SUM = [[None]*(M+2) for _ in range(N+2)]
    for i in range(N+1):
        for j in range(M+1):
            dp[i][j] = 0
    for i in range(N+2):
        for j in range(M+2):
            SUM[i][j] = 0

    favorite_answer_number = 1
    idx = lambda x,y: (x+2,y+2)
    # Loops index from custom enumeration for fun
    for alpha, s in enumerate(S):
        for beta, t in enumerate(T):
            i, j = alpha+1, beta+1
            if s == t:
                dp[i][j] = SUM[i][j] + 1
                favorite_answer_number += dp[i][j]
                favorite_answer_number %= MODULO
            else:
                dp[i][j] = 0
            xi, yj = idx(alpha, beta)
            SUM[xi][yj] = SUM[xi-1][yj] + SUM[xi][yj-1] - SUM[xi-1][yj-1] + dp[i][j]
            SUM[xi][yj] %= MODULO

    print(favorite_answer_number)


if __name__ == '__main__':
    (lambda f: f())(_main_)