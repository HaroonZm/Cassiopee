import sys

input = sys.stdin.readline

def read_values():
    return map(int, input().split())

def read_list():
    return list(read_values())

def func(N, mod):
    F = [1]
    for i in range(1, N + 1):
        F.append(F[-1] * i % mod)
    return F

INV = {}

def inv(a, mod):
    if a in INV:
        return INV[a]
    r = pow(a, mod - 2, mod)
    INV[a] = r
    return r

def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod

def main():
    N = int(input())
    F = [0] * N
    for i in range(N):
        P = int(input()) - 1
        F[P] = i

    res = 0
    tmp = 0
    pre = -1
    for f in F:
        if pre < f:
            tmp += 1
        else:
            res = max(res, tmp)
            tmp = 1
        pre = f
    res = max(res, tmp)
    print(N - res)

if __name__ == "__main__":
    main()