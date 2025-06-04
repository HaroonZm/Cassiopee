import sys

def mat_mul(A, B, M):
    n = len(A)
    res = [0]*n
    for i in range(n):
        s = 0
        a = A[i]
        for j, b in B:
            s += a[j]*b
        res[i] = s % M
    return res

def mat_vec_mul(MAT, vec, M):
    n = len(MAT)
    res = [0]*n
    for i in range(n):
        s = 0
        for j in MAT[i]:
            s += MAT[i][j]*vec[j]
        res[i] = s % M
    return res

def mat_pow(MAT, power, M):
    n = len(MAT)
    # Identity matrix sparse
    res = [dict() for _ in range(n)]
    for i in range(n):
        res[i][i] = 1
    base = [dict(row) for row in MAT]
    while power > 0:
        if power & 1:
            # res = mat_mul_sparse(res, base, M)
            tmp = [dict() for _ in range(n)]
            for i in range(n):
                for k in res[i]:
                    a = res[i][k]
                    for j in base[k]:
                        tmp[i][j] = (tmp[i].get(j,0)+ a*base[k][j])%M
            res = tmp
        # base = mat_mul_sparse(base, base, M)
        tmp = [dict() for _ in range(n)]
        for i in range(n):
            for k in base[i]:
                a = base[i][k]
                for j in base[k]:
                    tmp[i][j] = (tmp[i].get(j,0)+ a*base[k][j])%M
        base = tmp
        power >>= 1
    return res

def main():
    input=sys.stdin.readline
    while True:
        N,M,A,B,C,T = map(int, input().split())
        if N==0 and M==0 and A==0 and B==0 and C==0 and T==0:
            break
        init = list(map(int,input().split()))
        # Build sparse matrix MAT size NxN with only up to 3 entries per row
        MAT = [dict() for _ in range(N)]
        for i in range(N):
            if i-1 >= 0 and A != 0:
                MAT[i][i-1] = A
            if B != 0:
                MAT[i][i] = B
            if i+1 < N and C != 0:
                MAT[i][i+1] = C
        if T == 0:
            print(*init)
            continue
        MAT_T = mat_pow(MAT,T,M)
        res = mat_vec_mul(MAT_T, init, M)
        print(*res)

if __name__ == "__main__":
    main()