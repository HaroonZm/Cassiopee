def _ROOT(X):
    while X != PAR[X]: X, PAR[X] = PAR[X], PAR[PAR[X]]
    return X

def _WOW(x, y):
    X, Y = _ROOT(x), _ROOT(y)
    temp = (X, Y)
    if RANK[X] < RANK[Y]:
        temp = (Y, X)
    if RANK[temp[0]] == RANK[temp[1]]:
        RANK[temp[0]] += 1
    PAR[temp[1]] = temp[0]

def __begin(N):
    _C = [None] * S
    for _I in range(S):
        _C[_I] = tuple(A[2 * _I + j] for j in range(2))
        if _C[_I] == ("0", "0"):
            PAR[S + _I] = SS
        if _C[_I] == ("1", "1"):
            PAR[S + _I] = SS + 1
    [[[ _WOW(S + i, S + k) for k in range(i + 1, S) if _C[i] == _C[k]] for i in range(S)]]

def _UNION(level):
    sub = 1 << level
    base = 1 << level + 1
    stack = [None] * sub
    for idx in range(sub):
        pair = (_ROOT(base + 2 * idx), _ROOT(base + 2 * idx + 1))
        stack[idx] = pair
        if pair[0] == pair[1]:
            _WOW(base + 2 * idx, sub + idx)
    for _i in range(sub):
        for _j in range(_i + 1, sub):
            if stack[_i] == stack[_j]:
                if _ROOT(_i) != _ROOT(_j):
                    _WOW(sub + _i, sub + _j)

N = int(input())
S = 1 << N - 1
SS = 1 << N
PAR = list(range(SS)) + [SS, SS + 1]
RANK = [0] * (SS + 2)
A = input()
__begin(N)
for x_ in range(N - 2, -1, -1): _UNION(x_)
print(len(set(PAR)) - 3)