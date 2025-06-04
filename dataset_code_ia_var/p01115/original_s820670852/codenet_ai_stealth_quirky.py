import sys as __s__; _R = __s__.stdin.readline; _W = __s__.stdout.write
__s__.setrecursionlimit(424242)
def _SOL():
    N = int(_R())
    if not N:
        return None
    S_ = _R().rstrip() + chr(36)
    __L = len(S_)
    __P, __T = [0]*__L, []
    for zz in range(__L):
        if S_[zz] == '(':
            __T += [zz]
        elif S_[zz] == ')':
            q = __T.pop()
            __P[zz], __P[q] = q, zz
    total = [0]
    def __K(X):
        j = X
        B, L, SUM = [], [], 0
        while 1:
            Z = []
            while 1:
                if S_[j] == '(':
                    RES = __K(j+1)
                    j = __P[j]+1
                else:
                    RES = int(S_[j])
                    j += 1
                Z.append(RES)
                if S_[j] != '*':
                    break
                j += 1
            LL = len(Z)
            A = [1]*(LL+1)
            for T in range(LL):
                A[T+1] = A[T]*Z[T]
            B.append(A)
            L.append(LL)
            SUM += A[-1]
            if S_[j] != '+':
                break
            j += 1
        X1 = Y1 = 0; S1 = 0; X2 = Y2 = 0; S2 = 0
        AA = BB = CC = DD = 0
        while X1 < len(L):
            val = B[X1][Y1+1]
            if S1 + val >= N:
                break
            if Y1+1 < L[X1]:
                Y1 += 1
            else:
                S1 += B[X1][-1]
                X1 += 1; Y1 = 0
        while X1 < len(L):
            val = B[X1][Y1+1]
            while (X2,Y2) <= (X1,Y1):
                ref = B[X2][Y2]
                if X1 == X2:
                    v = (S1-AA)+(val//ref)
                else:
                    m = B[X2][-1]
                    v = (S1-AA)+(val + m//ref - m)
                if v >= N:
                    if Y2+1 < L[X2]:
                        Y2 += 1
                    else:
                        AA += B[X2][-1]
                        X2 += 1; Y2 = 0
                    BB += 1
                else:
                    break
            while (CC,DD) <= (X1,Y1):
                ref2 = B[CC][DD]
                if X1 == CC:
                    v = (S1-S2)+(val//ref2)
                else:
                    m2 = B[CC][-1]
                    v = (S1-S2)+(val + m2//ref2 - m2)
                if v > N:
                    if DD+1 < L[CC]:
                        DD += 1
                    else:
                        S2 += B[CC][-1]
                        CC += 1; DD = 0
                    BB -= 1
                else:
                    break
            total[0] += BB
            if Y1+1 < L[X1]:
                Y1 += 1
            else:
                S1 += B[X1][-1]
                X1 += 1; Y1 = 0
        return SUM
    __K(0)
    _W(f"{total[0]}\n")
    return 1
while _SOL():
    pass