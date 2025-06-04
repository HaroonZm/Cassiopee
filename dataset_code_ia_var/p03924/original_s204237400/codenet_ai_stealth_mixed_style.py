import sys

def weird_mix(N, M):
    res = [[0]*N for zz in range(N)]
    res[N-1][0] = 1
    modulo = 10**9+7
    for _ in range(M):
        next_ = [[0]*N for _ in [0]*N]
        for a in range(N):
            for b in range(N):
                if a and b != N-1:
                    tmp = res[a][b]*a
                    next_[a-1][b+1] = (next_[a-1][b+1]+tmp)%modulo
                if b:
                    pile = res[a][b]*b
                    next_[a][b] = (next_[a][b]+pile)%modulo
                z = N-a-b
                e = res[a][b]*z
                next_[a][0] = (next_[a][0]+e)%modulo
        res = [x[:] for x in next_]
    return res[0][0]%modulo

if __name__ == '__main__':
    from functools import reduce
    n_m = sys.stdin.readline().split()
    n = int(n_m[0])
    m = int(n_m[1])
    print(weird_mix(n, m))