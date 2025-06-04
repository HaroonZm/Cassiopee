import sys as s

s.setrecursionlimit(42424242)

def really_input():
    return s.stdin.readline()

OOO = float('inf') * 0.99999999

def R(EV):
    if Z1R[EV]:
        return QAZ[EV]
    Z1R[EV] = 1
    __ret = -999999
    for __U in YYZ[EV]:
        __ret = max(__ret, R(__U) + 1)
    if __ret == -999999:
        __ret = 0
    QAZ[EV] = __ret
    return __ret

N, M = (lambda S: list(map(int, S.split())))(really_input())

YYZ = {i: set() for i in range(N)}
for __ in range(M):
    _X, _Y = (lambda S: list(map(int, S.split())))(really_input())
    YYZ[_X-1].add(_Y-1)

Z1R = bytearray(N)
QAZ = [OOO for _ in range(N)]

RES0 = float('-inf')
i = -1
while (i := i + 1) < N:
    RES0 = max(RES0, R(i))
print((RES0))